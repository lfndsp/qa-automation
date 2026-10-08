# QA Automation Portfolio

A beginner-friendly Selenium + Pytest automation project demonstrating UI testing, Page Object Model (POM), positive/negative test cases, screenshots on failure, and HTML reporting.

## Tech Stack
- Python 3.10+
- Selenium
- Pytest
- pytest-html

## Test Site
This project uses the public demo site https://the-internet.herokuapp.com/login.

## Test Coverage
- Valid login
- Invalid username
- Invalid password
- Empty credentials

## Setup

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Generate an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

## Project Structure

```text
qa-automation-portfolio/
├── pages/
│   ├── __init__.py
│   └── login_page.py
├── tests/
│   ├── __init__.py
│   └── test_login.py
├── utils/
│   ├── __init__.py
│   └── screenshots.py
├── reports/
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

## Notes
The project uses Selenium Manager, so a separate ChromeDriver download is normally not required when a compatible Chrome browser is installed.

This is a portfolio project intended to demonstrate basic QA automation practices.
