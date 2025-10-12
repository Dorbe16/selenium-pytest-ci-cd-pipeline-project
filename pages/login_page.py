from selenium.webdriver.common.by import By
import time
class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):

        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button.radius").click()
        try:
            # Apasă ESC pentru a închide popup-ul
            from selenium.webdriver.common.keys import Keys
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        except:
            pass  # Dacă nu există popup, continuă normal

    def logout(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@href='/logout']").click()
        time.sleep(2)

    def get_flash_message(self):

        return self.driver.find_element(By.ID, "flash").text

