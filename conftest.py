import os
import pathlib
import pytest

from selenium import webdriver

from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
#modif
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=os.getenv("BROWSER","chrome"), help="Browser: chrome or firefox, if empty run chrome")
    parser.addoption("--grid", action="store", default=os.getenv("GRID_URL",""), help="Selenium Grid URL (example: http://localhost:4444/wd/hub), if empty run locally")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()
    grid_url = request.config.getoption("--grid")
    is_CI = os.getenv("CI", "false").lower() == "true"

    if browser == "chrome":
        options = ChromeOptions()
        if is_CI:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--incognito")
        options.set_capability("pageLoadStrategy", "normal")
    elif browser == "firefox":
        options = FirefoxOptions()
        if is_CI:
            options.add_argument("-headless")
        options.set_capability("pageLoadStrategy", "normal")
    else:
        raise ValueError("Unsupported browser!")

    if grid_url:
        driver = Remote(command_executor=grid_url, options=options)
    else:
        if browser == "chrome":
            driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Firefox(options=options)


    driver.set_page_load_timeout(30)
    yield driver
    driver.quit()


#def driver():
    #options = Options()
    #options.add_argument("--headless=new")
    #options.add_argument("--no-sandbox")
    #options.add_argument("--disable-dev-shm-usage")
    #service = Service(ChromeDriverManager().install(), options=options)
    #driver = webdriver.Chrome(service=service)
    #driver.implicitly_wait(5)
    #yield driver
    #driver.quit
