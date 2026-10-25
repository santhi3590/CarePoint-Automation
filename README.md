# CarePoint Automation

## Project Overview
CarePoint Automation is a web form automation testing project developed using Python, Selenium WebDriver, and Pytest. It uses the Page Object Model (POM) to organize reusable page methods and automated test cases.

**Note:** This project currently automates a public practice form on QA Practice; it is not connected to a real hospital booking system.

## Technologies Used
- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- pytest-html

## Project Structure
- `config/` - Project settings and website URL
- `data/` - Test data
- `pages/` - Page Object classes and reusable methods
- `reports/` - HTML test reports
- `screenshots/` - Screenshots captured when tests fail
- `tests/` - Automated test cases and fixtures
- `utils/` - Helper functions

## Test Scenarios
- Verify that the website opens successfully
- Verify first name entry
- Verify last name entry
- Verify email entry
- Verify submit button interaction
- Verify invalid email field configuration
- Verify missing first name validation
- Verify missing phone number validation

## How to Run

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the tests:

```bash
python -m pytest tests/test_carepoint.py -v
```

Generate an HTML report:

```bash
python -m pytest tests/test_carepoint.py -v --html=reports/report.html --self-contained-html
```

## Test Results
Latest test run: **8 passed**

## Screenshots
Screenshots are automatically saved