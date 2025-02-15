class BasePage():
    def __init__(self, page):
        self.page = page

    def open_url(self, url):
        self.page.goto(url, wait_until="networkidle")

    def find_element(self, locator):
        return self.page.locator(locator)

    def get_elements(self, locator):
        return self.page.locator(locator).all()

    def click_element(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.fill(text)

    def screenshot(self, text):
        self.page.screenshot(path=f"screenshots\{text}.png", full_page=True)
