from utils.test_data.login_data import TestData
import pytest

@pytest.mark.ui
def test_login_with_wrong_password(login_page):
    login_page.open()
    login_page.login(TestData.VALID_USER, "wrong_password")

    assert "Epic sadface" in login_page.get_error_message()

    