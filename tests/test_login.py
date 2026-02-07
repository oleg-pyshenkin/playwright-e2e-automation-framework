from playwright.sync_api import expect

def test_successful_login(login_page):
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    expect(login_page.page.locator(".inventory_list")).to_be_visible()

