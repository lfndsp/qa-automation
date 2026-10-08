# QA Automation Portfolio

A Selenium + Pytest UI automation project demonstrating basic software QA automation skills.

## Tech Stack
- Python 3.10+
- Selenium
- Pytest
- pytest-html

## Test Site
https://the-internet.herokuapp.com/login

## Test Coverage
- Valid login
- Invalid username
- Invalid password
- Empty credentials

## How to Run

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
pytest --html=report.html --self-contained-html
```

## Project Structure

All Python files are kept in the repository root to make uploading through the GitHub web interface simple.

This project demonstrates functional testing, negative testing, parameterized tests, Page Object Model concepts, defect validation, and failure screenshots.
