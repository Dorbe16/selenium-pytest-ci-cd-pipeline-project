from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        # Așteaptă și completează username
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.clear()
        username_field.send_keys(username)

        # Completează password
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)

        # Click pe butonul de login
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Așteaptă ca login-ul să se complete (URL să conțină /secure)
        self.wait.until(EC.url_contains("/secure"))

    def logout(self):
        # Așteaptă explicit ca butonul de logout să fie prezent ȘI clickable
        logout_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/logout']"))
        )

        # Click pe logout
        logout_button.click()

        # Așteaptă ca URL-ul să se schimbe înapoi la /login
        self.wait.until(EC.url_contains("/login"))

        # Așteaptă explicit ca mesajul de logout să apară în flash
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, "flash"),
                "logged out"
            )
        )

    def get_flash_message(self):
        # Așteaptă ca flash message să fie vizibil
        flash_element = self.wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        # Returnează textul fără simbolul × de închidere
        return flash_element.text.replace('×', '').strip()