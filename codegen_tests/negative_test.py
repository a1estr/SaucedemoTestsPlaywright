from playwright.sync_api import expect


def test_filling_customer_info(page):
    # Перейдем на страницу логина
    page.goto("https://www.saucedemo.com/")

    # Залогинимся
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")

    # Добавим товар в корзину
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.screenshot(path="screenshots\item_in_cart_added.png")
    expect(page.locator("[data-test=\"shopping-cart-badge\"]")).to_contain_text("1")

    # Перейдем в корзину
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.screenshot(path="screenshots\item_in_cart.png")
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Your Cart")
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Bike Light")
    expect(page.locator("[data-test=\"item-quantity\"]")).to_contain_text("1")

    # Перейдем на страницу заполнения информации о покупателе
    page.locator("[data-test=\"checkout\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Your Information")

    # Проверим появление ошибок при незаполненных полях
    page.locator("[data-test=\"continue\"]").click()
    page.screenshot(path="screenshots\empty_fields.png")
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Error: First Name is required")
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("test")
    page.locator("[data-test=\"continue\"]").click()
    page.screenshot(path="screenshots\only_first_name.png")
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Error: Last Name is required")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("test")
    page.locator("[data-test=\"continue\"]").click()
    page.screenshot(path="screenshots\last_and_first_names.png")
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Error: Postal Code is required")