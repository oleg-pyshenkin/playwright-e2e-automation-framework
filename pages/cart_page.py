from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_to_cart_backpack_btn = "[data-test='add-to-cart-sauce-labs-backpack']"
        self.cart_icon = ".shopping_cart_link"
        self.remove_backpack_btn = "[data-test='remove-sauce-labs-backpack']"
        self.cart_badge = "[data-test='shopping_cart_badge']"

    def add_backpack_to_cart(self):
        self.click(self.add_to_cart_backpack_btn)

    def open_cart(self):
        self.click(self.cart_icon)

    def remove_backpack_from_cart(self):
        self.click(self.remove_backpack_btn)

    def get_cart_count(self):
        return self.get_text(self.cart_badge)

    def is_cart_badge_visible(self):
        return self.is_visible(self.cart_badge)
    
