import requests
import pytest 

@pytest.mark.api
def test_api_login():
    url = "https://www.saucedemo.com"
    response = requests.get(url)
    assert response.status_code == 200