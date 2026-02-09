from playwright.sync_api import expect
from utils.test_data import TestData



def test_successful_login(login_page):
    login_page.open()
    login_page.login(TestData.VALID_USER, TestData.VALID_PASSWORD)
    expect(login_page.page.locator(".inventory_list")).to_be_visible()

