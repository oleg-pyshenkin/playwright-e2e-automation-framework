# conftest.py
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture
def login_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login = LoginPage(page)
        yield login
        browser.close()
