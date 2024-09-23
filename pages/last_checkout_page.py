from pages.base_page import BasePage
from locators.locators import LastCheckoutPageLocators
from allure import step


class LastCheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.element = LastCheckoutPageLocators

    @step('Поиск кнопки "Finish"')
    def find_finish_button(self):
        return self.find_element(self.element.FINISH_BUTTON)
