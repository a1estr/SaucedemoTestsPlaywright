from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    ITEM_NAME_IN_OVERVIEW = ".inventory_item_name"
    FINISH_BUTTON = "#finish"

    def get_items_in_overview(self):
        return self.get_elements(self.ITEM_NAME_IN_OVERVIEW)

    def complete_order(self):
        self.click_element(self.FINISH_BUTTON)