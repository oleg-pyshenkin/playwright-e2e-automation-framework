import pytest
from config.config import VALID_USER, VALID_PASSWORD

@pytest.mark.smoke
def test_smoke_login(login_page):
    login_page.open()
    login_page.login(VALID_USER, VALID_PASSWORD)

    assert "inventory" in login_page.page.url