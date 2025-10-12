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
    time.sleep(3)
    login_message = page.get_flash_message()
    print(f"Message after login: {login_message}")
    page.logout()

    for i in range(10):
        time.sleep(1)
        curr_message = page.get_flash_message()
        print(f"Attempt {i+1}: {curr_message}")
        if "logged out" in curr_message.lower():
            break
    final_message = page.get_flash_message()
    print(f"Final message: {final_message}")
    assert "You logged out of the secure area!" in final_message
    #time.sleep(2)
    #assert "You logged out of the secure area!" in page.get_flash_message()
