import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from login_page import LoginPage
from screenshots import save_screenshot


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")

    assert page.is_logged_in(), "User should be logged in with valid credentials"


def test_invalid_username(driver):
    page = LoginPage(driver)
    page.open()
    page.login("invalid_user", "SuperSecretPassword!")

    message = page.get_flash_message()
    assert "Your username is invalid!" in message


def test_invalid_password(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "WrongPassword")

    message = page.get_flash_message()
    assert "Your password is invalid!" in message


@pytest.mark.parametrize(
    "username,password",
    [
        ("", ""),
        ("tomsmith", ""),
        ("", "SuperSecretPassword!"),
    ],
)
def test_empty_credentials(driver, username, password):
    page = LoginPage(driver)
    page.open()
    page.login(username, password)

    message = page.get_flash_message()
    assert "invalid" in message.lower()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            save_screenshot(driver, item.name)
