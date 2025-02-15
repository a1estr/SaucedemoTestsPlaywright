from pages.base_page import BasePage


class InventoryPage(BasePage):
    CART_CONTAINER = "[data-test=\"shopping-cart-link\"]"
    ITEM_NAME = "[data-test=\"inventory-item-name\"]"
    TEST_ALL_THINGS_ITEM = "[data-test=\"add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)\"]"
    CART_BADGE = "[data-test=\"shopping-cart-badge\"]"
    BURGER_MENU = "#react-burger-menu-btn"
    LOGOUT_BUTTON = "#logout_sidebar_link"
    SIDEBAR_MENU = ".bm-menu"
    ITEMS_LIST = ["Sauce Labs Backpack",
                  "Sauce Labs Bike Light",
                  "Sauce Labs Bolt T-Shirt",
                  "Sauce Labs Fleece Jacket",
                  "Sauce Labs Onesie",
                  "Test.allTheThings() T-Shirt (Red)"
                  ]
    DROPDOWN_SORT = "[data-test=\"product-sort-container\"]"
    PRICE = ".inventory_item_price"
    PRICES_LIST = [29.99, 9.99, 15.99, 49.99, 7.99, 15.99]

    def add_to_cart(self, item_name):
        if "test" not in item_name:
            self.click_element(f"#add-to-cart-sauce-labs-{item_name}")
        else:
            self.click_element(self.TEST_ALL_THINGS_ITEM)

    def items_in_cart_count(self):
        return self.find_element(self.CART_BADGE).text_content()

    def open_cart(self):
        self.click_element(self.CART_CONTAINER)

    def open_side_bar(self):
        self.click_element(self.BURGER_MENU)

    def logout(self):
        self.click_element(self.LOGOUT_BUTTON)

    def get_items_list(self):
        return self.ITEMS_LIST

    def get_all_items_list(self):
        items = self.get_elements(self.ITEM_NAME)
        items_list = []
        for item in items:
            items_list.append(item.text_content())
        return items_list

    def get_all_prices_list(self):
        prices = self.get_elements(self.PRICE)
        prices_list = []
        for price in prices:
            price_float = float(price.text_content().strip("$"))
            prices_list.append(price_float)
        return prices_list

    def select_sorting(self, sorting_option):
        self.find_element(self.DROPDOWN_SORT).select_option(sorting_option)