from utils.test_data.login_data import TestData  
import pytest

@pytest.mark.smoke
def test_smoke_login(login_page):
    login_page.open()
    login_page.login(TestData.VALID_USER, TestData.VALID_PASSWORD)