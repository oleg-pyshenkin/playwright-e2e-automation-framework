from config.config import Config

class TestData:
    BASE_URL = Config.BASE_URL  # This was causing the error
    VALID_USER = Config.VALID_USER
    VALID_PASSWORD = Config.VALID_PASSWORD
    
    FIRST_NAME = "Oleg"
    LAST_NAME = "QA"
    POSTAL_CODE = "12345"
    INVALID_PASSWORD = "wrong_password"