from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest
from allure import step


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Драйвер для запуска тестов. "
                                                            "Доступные драйверы: chrome, firefox"
    )


@step('Запуск веб-драйвера')
@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    driver_path = Path(__file__).parent.parent / "driver"  # Запускать тесты нужно из корня проекта
    if browser_name == "chrome":
        service = ChromeService(executable_path=str(driver_path / "chromedriver.exe"))
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FirefoxService(executable_path=str(driver_path / "geckodriver.exe"))
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}")
    yield driver
    driver.quit()
