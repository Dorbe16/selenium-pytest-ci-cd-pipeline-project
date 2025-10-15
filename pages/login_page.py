from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.CSS_SELECTOR, "button.radius")
    FLASH = (By.ID, "flash")
    LOGOUT = (By.XPATH, "//a[@href='/logout']")
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME))

    def login(self, username, password):

        usern = self.wait.until(EC.visibility_of_element_located(self.USERNAME))
        passw = self.wait.until(EC.visibility_of_element_located(self.PASSWORD))
        submit = self.wait.until(EC.visibility_of_element_located(self.SUBMIT))
        #self.driver.find_element(By.ID, "username").send_keys(username)
        #self.driver.find_element(By.ID, "password").send_keys(password)
        #self.driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        usern.clear()
        usern.send_keys(username)
        passw.clear()
        passw.send_keys(password)
        submit.click()

        self.wait.until(EC.visibility_of_element_located(self.FLASH))

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT)).click()
        self.wait.until(EC.visibility_of_element_located(self.FLASH))

    def get_flash_message(self):

        #return self.driver.find_element(By.ID, "flash").text
        return self.wait.until(EC.visibility_of_element_located(self.FLASH)).text

