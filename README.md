Playwright E2E Automation Framework
Project Overview

This project is a Playwright-based end-to-end automation framework for testing a demo e-commerce website (https://www.saucedemo.com
).
It demonstrates a QA engineer’s skills in:

UI test automation using Playwright

Page Object Model (POM)

Python OOP and clean code

Test data management

Test organization with pytest

Project Structure
playwright-e2e-automation-framework/
├─ pages/                 # Page Object classes
│  ├─ base_page.py
│  ├─ login_page.py
│  ├─ cart_page.py
│  └─ checkout_page.py
├─ tests/                 # Test scripts
│  ├─ ui/
│  │  ├─ test_login.py
│  │  ├─ test_checkout.py
│  │  └─ test_cart.py
├─ utils/
│  └─ test_data.py        # Test data constants
├─ config.py              # Base URLs, valid users, passwords
├─ pytest.ini             # Pytest configuration
├─ requirements.txt       # Python dependencies
└─ README.md

Setup

Clone the project

git clone <your-repo-url>
cd playwright-e2e-automation-framework


Create a virtual environment

python3 -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows


Install dependencies

pip install -r requirements.txt


Install Playwright browsers

playwright install

Running Tests

Run all UI tests

pytest -v


Run a single test file

pytest tests/ui/test_login.py -v


View screenshots
If a test fails, screenshots are saved in the screenshots/ folder.

Test Coverage

Login Tests: Valid login, invalid login, locked out user

Cart Tests: Add/remove items, cart badge check

Checkout Tests: Fill customer info, continue, finish, verify order success

API tests are not implemented in this version.

Test Data

Stored in utils/test_data.py:

class TestData:
    VALID_USER = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    INVALID_PASSWORD = "wrong_password"
    LOCKED_USER = "locked_out_user"
    FIRST_NAME = "Oleg"
    LAST_NAME = "QA"
    POSTAL_CODE = "12345"

Config

Stored in config.py:

class Config:
    BASE_URL = "https://www.saucedemo.com/"
    VALID_USER = "standard_user"
    VALID_PASSWORD = "secret_sauce"