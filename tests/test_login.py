from pages.login_page import LoginPage

def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in page.get_flash_message()

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("wrong", "wrong")
    assert "Your username is invalid!" in page.get_flash_message()

def test_logout(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")
    page.logout()
    assert "You logged out of the secure area!" in page.get_flash_message()
