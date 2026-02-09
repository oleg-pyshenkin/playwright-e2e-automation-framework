from playwright.sync_api import expect
from utils.test_data import TestData


def test_checkout_flow(login_page, cart_page, checkout_page):
    login_page.open()
    login_page.login(TestData.VALID_USER, TestData.VALID_PASSWORD)

    cart_page.add_backpack_to_cart()

    cart_page.open_cart()
    checkout_page.start_checkout()
    checkout_page.fill_customer_info("Oleg", "P", "12345")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    assert checkout_page.get_success_message() == "Thank you for your order!"


