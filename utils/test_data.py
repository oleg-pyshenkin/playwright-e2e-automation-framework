import requests
from config.config import VALID_USER, VALID_PASSWORD

class TestData:
    USERNAME = VALID_USER
    PASSWORD = VALID_PASSWORD

    FIRST_NAME = "Oleg"
    LAST_NAME = "QA"
    POSTAL_CODE = "12345"

    INVALID_PASSWORD = "wrong_password"

    
    def test_api_login():
        url = "https://www.saucedemo.com"
        response = requests.get(url)
        assert response.status_code == 200
