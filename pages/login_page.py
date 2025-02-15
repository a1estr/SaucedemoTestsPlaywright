from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = "[data-test=\"username\"]"
    PASSWORD_INPUT = "[data-test=\"password\"]"
    LOGIN_BUTTON = "[data-test=\"login-button\"]"
    ERROR_MESSAGE = "[data-test=\"error\"]"

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text_content()

    def get_login_page(self):
        return self.open_url("https://www.saucedemo.com/")

    def valid_login(self, name, password):
        self.get_login_page()
        self.enter_username(name)
        self.enter_password(password)
        self.click_login()