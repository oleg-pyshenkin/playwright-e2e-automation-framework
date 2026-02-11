from pages.base_page import BasePage
from utils.config_loader import Config

config = Config(env="dev")

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_btn = "[data-test='checkout']"
        self.first_name_input = "[data-test='firstName']"
        self.last_name_input = "[data-test='lastName']"
        self.postal_code_input = "[data-test='postalCode']"
        self.continue_btn = "[data-test='continue']"
        self.finish_btn = "[data-test='finish']"
        self.success_message = ".complete-header" 

    def start_checkout(self):
        self.click(self.checkout_btn)

    def fill_customer_info(self, first_name_input, last_name_input, postal_code_input):
        self.fill(self.first_name_input, first_name_input)
        self.fill(self.last_name_input, last_name_input)
        self.fill(self.postal_code_input, postal_code_input)

    def continue_checkout(self):
        self.click(self.continue_btn)   

    def finish_checkout(self):
        self.click(self.finish_btn)

    def get_success_message(self):
        return self.get_text(self.success_message)
