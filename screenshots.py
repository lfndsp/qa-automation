from pathlib import Path


def save_screenshot(driver, name="failure"):
    folder = Path("screenshots")
    folder.mkdir(exist_ok=True)
    path = folder / f"{name}.png"
    driver.save_screenshot(str(path))
    return str(path)
