import pytest
from playwright.sync_api import expect
from utils.test_data import TestData


@pytest.mark.parametrize("username,password,should_pass", [
    (TestData.VALID_USER, TestData.VALID_PASSWORD, True),
    ("standard_user", "wrong_pass", False),
    ("locked_out_user", "secret_sauce", False)
])

def test_login_parametrize(login_page, username, password, should_pass):
    login_page.open()
    login_page.login(username, password)

    if should_pass:
        expect(login_page.page.locator(".inventory_list")).to_be_visible()
    else:
        expect(login_page.page.locator(login_page.ERROR_MESSAGE)).to_be_visible()