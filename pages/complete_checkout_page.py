from pages.base_page import BasePage
from locators.locators import CompleteCheckoutPageLocators
from allure import step


class CompleteCheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.element = CompleteCheckoutPageLocators

    @step('Поиск подтверждения успешного завершения покупки')
    def proof_of_purchase(self):
        return self.find_element(self.element.COMPLETE_MESSAGE)
