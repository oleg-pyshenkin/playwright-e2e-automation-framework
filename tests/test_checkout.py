from playwright.sync_api import expect

def test_checkout_flow(login_page, cart_page, checkout_page):
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    cart_page.add_backpack_to_cart()
    cart_page.open_cart()

    checkout_page.start_checkout()
    checkout_page.fill_customer_info("Oleg", "P", "1234567")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    expect(checkout_page.order_success_message()).to_be_visible()

