import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage


@pytest.mark.parametrize(
    ("name", "password"), [
        ('standard_user', 'secret_sauce'),
        ('locked_out_user', 'secret_sauce'),
        ('problem_user', 'secret_sauce'),
        ('performance_glitch_user', 'secret_sauce'),
    ]
)
def test_valid_login(page, name, password):
    login_page = LoginPage(page)
    login_page.get_login_page()
    login_page.enter_username(name)
    login_page.enter_password(password)
    login_page.click_login()
    login_page.screenshot("test_valid_login_" + name)
    if name == 'locked_out_user':
        assert login_page.get_error_message() == "Epic sadface: Sorry, this user has been locked out.", \
            "Ошибка: логин удался"
    else:
        expect(page.locator("[data-test=\"title\"]")).to_be_visible()
