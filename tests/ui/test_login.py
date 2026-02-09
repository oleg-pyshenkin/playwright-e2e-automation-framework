from playwright.sync_api import expect
from config.config import VALID_USER, VALID_PASSWORD


def test_successful_login(login_page):
    login_page.open()
    login_page.login(VALID_USER, VALID_PASSWORD)
    expect(login_page.page.locator(".inventory_list")).to_be_visible()

