from pages.login_page import LoginPage
import time
def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()
    time.sleep(2)
    page.login("tomsmith", "SuperSecretPassword!")
    time.sleep(2)
    assert "You logged into a secure area!" in page.get_flash_message()

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.open()
    time.sleep(2)
    page.login("wrong", "wrong")
    time.sleep(2)
    assert "Your username is invalid!" in page.get_flash_message()

def test_logout(driver):
    page = LoginPage(driver)
    page.open()
    time.sleep(2)
    page.login("tomsmith", "SuperSecretPassword!")
    time.sleep(2)
    page.logout()
    time.sleep(2)
    assert "You logged out of the secure area!" in page.get_flash_message()
