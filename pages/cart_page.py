from pages.base_page import BasePage


class CartPage(BasePage):
    ITEM_NAME_IN_CART = ".inventory_item_name"
    CART_BADGE = "[data-test=\"shopping-cart-badge\"]"
    CHECKOUT = "#checkout"

    def get_item_name_in_cart(self):
        return self.find_element(self.ITEM_NAME_IN_CART).text_content()

    def items_in_cart_count(self):
        return self.find_element(self.CART_BADGE).text_content()

    def get_items_in_cart(self):
        return self.get_elements(self.ITEM_NAME_IN_CART)

    def checkout_order(self):
        self.click_element(self.CHECKOUT)