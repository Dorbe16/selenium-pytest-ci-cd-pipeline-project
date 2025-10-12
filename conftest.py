import os, pytest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
#modificare
#modif2
#modif8
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")
    parser.addoption("--grid", action="store", default="http://localhost:4444/wd/hub", help="Selenium Grid URL")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    grid_url = request.config.getoption("--grid")

    if browser == "chrome":
        options = ChromeOptions()
        options.set_capability("browserName", "chrome")
        options.add_argument("--incognito")
    elif browser == "firefox":
        options = FirefoxOptions()
        options.set_capability("browserName", "firefox")
    else:
        raise ValueError("Unsupported browser!")

    driver = Remote(command_executor=grid_url, options=options)
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
