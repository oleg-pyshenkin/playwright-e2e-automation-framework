class CartPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_backpack_btn = "[data-test='add-to-cart-sauce-labs-backpack']"
        self.cart_icon = ".shopping_cart_link"
        self.remove_backpack_btn = "[data-test='remove-sauce-labs-backpack']"
        self.cart_badge = "[data-test='shopping_cart_badge']"

    def add_backpack_to_cart(self):
        self.page.locator(self.add_to_cart_backpack_btn).click()

    def open_cart(self):
        self.page.click(self.cart_icon)

    def remove_backpack_from_cart(self):
        self.page.click(self.remove_backpack_btn)

    def get_cart_count(self):
        return self.page.locator(self.cart_badge).inner_text()

    def is_cart_badge_visible(self):
        return self.page.locator(self.cart_badge).is_visible()
    
