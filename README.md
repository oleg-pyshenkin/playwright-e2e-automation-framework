# Playwright Automation Framework (Python)

A professional-grade test automation framework built with **Python, Playwright, and Pytest**, designed for scalable and maintainable automation projects. 

This project demonstrates real-world automation skills including UI and API testing, clean code, object-oriented design, and robust test architecture.

---

## Key Features

- UI automation using Playwright
- API testing using Requests
- Page Object Model (POM) for maintainable UI tests
- BasePage abstraction for reusable functionality
- Pytest fixtures for setup and teardown
- Stable selectors using `data-test` attributes
- Clear project structure for UI, API, and smoke tests
- Ready for integration with CI/CD pipelines

---

## Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.13 |
| UI Automation | Playwright |
| Test Framework | Pytest |
| API Testing | Requests |
| Design Patterns | Page Object Model, OOP |
| Version Control | Git, GitHub |
| Operating Systems | macOS / Linux / Windows |

---

## Project Structure
playwright-e2e-automation-framework/
│
├── pages/ # Page Objects containing locators and UI logic
├── tests/
│ ├── ui/ # UI test cases
│ ├── api/ # API test cases
│ └── smoke/ # Smoke tests
├── utils/ # Helper functions and test data
├── config/ # Environment configuration files
├── conftest.py # Global fixtures for Pytest
├── pytest.ini # Pytest configuration
├── requirements.txt # Python dependencies
└── README.md


---

## Test Scenarios Implemented

### UI Tests
- Login (positive and negative cases)
- Product selection
- Add and remove items from cart
- Checkout process
- Verification of UI elements and business logic

### API Tests
- Basic REST API validation
- Response status code and body checks
- Integration with test data layer

### Smoke Tests
- Critical user flows verification
- Quick validation of core functionality

---

## Running Tests

### Install Dependencies

```bash
pip install -r requirements.txt
playwright install


### Install Dependencies

```bash
pip install -r requirements.txt
playwright install


## Running Tests

Run UI Tests Only
pytest tests/ui

Run API Tests Only
pytest tests/api

Run Smoke Tests
pytest tests/smoke
