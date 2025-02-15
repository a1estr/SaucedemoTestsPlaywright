from playwright.sync_api import expect


def test_remove_item_from_cart(page):
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
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.screenshot(path="screenshots\item_in_cart.png")
    expect(page.locator("[data-test=\"shopping-cart-badge\"]")).to_contain_text("1")

    # Уберем товар из корзины
    page.locator("[data-test=\"remove-sauce-labs-backpack\"]").click()
    page.screenshot(path="screenshots\item_not_cart.png")
    expect(page.locator("[data-test=\"shopping-cart-badge\"]")).not_to_be_visible()