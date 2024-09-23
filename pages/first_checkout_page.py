from pages.base_page import BasePage
from locators.locators import FirstCheckoutPageLocators
from work_data import data
from allure import step


class FirstCheckoutPage(BasePage):
    '''Такая реализация позволяет либо передать свои значения, либо испоользовать дефолтное'''

    def __init__(self, driver):
        super().__init__(driver)
        self.element = FirstCheckoutPageLocators
        self.data = data

    @step('Ввод имени')
    def enter_first_name(self, first_name=None):
        if first_name is None:
            first_name = self.data.FIRST_NAME
        response = self.find_element(self.element.FIRST_NAME_FIELD).send_keys(first_name)
        return response

    @step('Ввод фамилии')
    def enter_last_name(self, last_name=None):
        if last_name is None:
            last_name = self.data.LAST_NAME
        response = self.find_element(self.element.LAST_NAME_FIELD).send_keys(last_name)
        return response

    @step('Ввод почтового индекса')
    def enter_postal_code(self, postal_code=None):
        if postal_code is None:
            postal_code = self.data.POSTAL_CODE
        response = self.find_element(self.element.POSTAL_CODE_FIELD).send_keys(postal_code)
        return response

    @step('Поиск кнопки продолжить("Continue")')
    def find_continue_button(self):
        return self.find_element(self.element.CONTINUE_BUTTON)

    @step('Заполнение формы')
    def filling_form(self):
        self.enter_first_name()
        self.enter_last_name()
        self.enter_postal_code()
