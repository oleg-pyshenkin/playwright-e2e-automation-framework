from playwright.sync_api import expect
from utils.config_loader import Config
from pages.base_page import BasePage

config = Config(env="dev")

class CartPage(BasePage):
    ADD_BACKPACK_BTN = "[data-test='add-to-cart-sauce-labs-backpack']"
    CART_ICON = ".shopping_cart_link"
    REMOVE_BACKPACK_BTN = "[data-test='remove-sauce-labs-backpack']"
    CART_BADGE = "[data-test='shopping_cart_badge']"

    def __init__(self, page):
        super().__init__(page)

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BTN)
        expect(self.page.locator(self.REMOVE_BACKPACK_BTN)).to_be_visible()

    def open_cart(self):
        self.click(self.CART_ICON)

    def remove_backpack_from_cart(self):
        self.click(self.REMOVE_BACKPACK_BTN)

    def get_cart_count(self):
        badge = self.page.locator(self.CART_BADGE)
        if badge.count() == 0:
            return 0
        return int(badge.inner_text())

    def is_cart_badge_visible(self):
        return self.get_cart_count() > 0
