import pytest
from pages.login_page import LoginPage


@pytest.fixture
def opened_login_page(page):
    login_page = LoginPage(page)
    login_page.get_login_page()
    return login_page


def test_empty_fields(opened_login_page):
    opened_login_page.click_login()
    opened_login_page.screenshot("test_empty_fields_message")
    assert opened_login_page.get_error_message() == "Epic sadface: Username is required"


def test_filled_username(opened_login_page):
    opened_login_page.enter_username("standard_user")
    opened_login_page.click_login()
    opened_login_page.screenshot("test_filled_username_message")
    assert opened_login_page.get_error_message() == "Epic sadface: Password is required"
    opened_login_page.screenshot("test_filled_username_message")


def test_filled_password(opened_login_page):
    opened_login_page.enter_password("secret_sauce")
    opened_login_page.click_login()
    opened_login_page.screenshot("test_filled_password_message")
    assert (opened_login_page.get_error_message() ==
            "Epic sadface: Username is required")


def test_invalid_credentials(opened_login_page):
    opened_login_page.enter_username("test")
    opened_login_page.enter_password("test")
    opened_login_page.click_login()
    opened_login_page.screenshot("test_invalid_credentials_message")
    assert (opened_login_page.get_error_message() ==
            "Epic sadface: Username and password do not match any user in this service")
