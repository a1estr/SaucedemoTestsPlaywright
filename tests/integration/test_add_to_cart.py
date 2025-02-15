import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.parametrize(
    ("item_name", "item_in_cart"), [
        ("backpack", "Sauce Labs Backpack"),
        ("bike-light", "Sauce Labs Bike Light"),
        ("bolt-t-shirt", "Sauce Labs Bolt T-Shirt"),
        ("fleece-jacket", "Sauce Labs Fleece Jacket"),
        ("onesie", "Sauce Labs Onesie"),
        ("add-to-cart-test.allthethings()-t-shirt-(red)",
         "Test.allTheThings() T-Shirt (Red)"
         )
    ]
)
def test_add_to_cart(page, item_name, item_in_cart):
    # Залогинимся и перейдем на страницу с товарами
    login_page = LoginPage(page)
    login_page.valid_login(name="standard_user",
                           password="secret_sauce"
                           )

    # Добавим товар в корзину
    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart(item_name)

    # Проверим, что корзина не пустая
    inventory_page.screenshot("test_add_to_cart_cart_badge_" + item_name)
    assert inventory_page.items_in_cart_count() == "1", "Число товаров в корзине != 1"

    # Перейдем в корзину
    inventory_page.open_cart()
    assert "cart" in page.url, "Страница с корзиной не открылась"

    # Проверим, что товар присутствует в корзине
    cart_page = CartPage(page)
    inventory_page.screenshot("test_add_to_cart_item_in_cart_" + item_name)
    assert cart_page.get_item_name_in_cart() == item_in_cart, \
        "Товар не был добавлен в корзину"
    assert cart_page.items_in_cart_count() == "1", "Число товаров в корзине != 1"
