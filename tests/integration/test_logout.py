import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.parametrize(
    ("name", "password"), [
        ('standard_user', 'secret_sauce'),
        ('performance_glitch_user', 'secret_sauce'),
        ('problem_user', 'secret_sauce'),
        ('error_user', 'secret_sauce'),
        ('visual_user', 'secret_sauce')
    ]
)
def test_logout(page, name, password):
    login_page = LoginPage(page)

    # Залогинимся на сайт
    login_page.valid_login(name, password)
    inventory_page = InventoryPage(page)
    inventory_page.screenshot("test_logout_inv_page_" + name)

    # Откроем выпадающее меню
    inventory_page.open_side_bar()

    # Нажнем кнопку Logout
    inventory_page.logout()
    login_page.screenshot("test_logout_login_page_" + name)
    expect(login_page.find_element(login_page.LOGIN_BUTTON)).to_be_visible()
