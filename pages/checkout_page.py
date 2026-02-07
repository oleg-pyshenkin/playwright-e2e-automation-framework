class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.checkout_btn = "[data-test='checkout']"
        self.first_name_input = "[data-test='firstName']"
        self.last_name_input = "[data-test='lastName']"
        self.postal_code_input = "[data-test='postalCode']"
        self.continue_btn = "[data-test='continue']"
        self.finish_btn = "[data-test='finish']"

    def start_checkout(self):
        self.page.click(self.checkout_btn)

    def fill_customer_info(self, first_name_input, last_name_input, postal_code_input):
        self.page.fill(self.first_name_input, first_name_input)
        self.page.fill(self.last_name_input, last_name_input)
        self.page.fill(self.postal_code_input, postal_code_input)

    def continue_checkout(self):
        self.page.click(self.continue_btn)

    def finish_checkout(self):
        self.page.click(self.finish_btn)