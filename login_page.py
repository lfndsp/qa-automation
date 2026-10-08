from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button.secondary.radius")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        element = self.driver.find_element(*self.USERNAME)
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = self.driver.find_element(*self.PASSWORD)
        element.clear()
        element.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_flash_message(self):
        return self.driver.find_element(*self.FLASH_MESSAGE).text

    def is_logged_in(self):
        return bool(self.driver.find_elements(*self.LOGOUT_BUTTON))
