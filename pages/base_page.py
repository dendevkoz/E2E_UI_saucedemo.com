from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from work_data import data
from allure import step


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = data.BASE_URL

    @step('Переход на сайт')
    def go_to_site(self):
        return self.driver.get(self.url)

    @step('Поиск элемента')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Элемент не был найден: {locator}")

    @step('Ожидание URL')
    def wait_to_url(self, url):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains(url))
