from pages.base_page import BasePage
from locators.locators import UserLoginLocators
from work_data import data
from allure import step


class LoginPage(BasePage):
    '''Такая реализация позволяет либо передать свои значения, либо испоользовать дефолтное'''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.elements = UserLoginLocators
        self.data = data

    @step('Ввод логина')
    def enter_username(self, user_name=None):
        if user_name is None:
            user_name = self.data.USERNAME
        response = self.find_element(self.elements.USERNAME_FIELD).send_keys(user_name)
        return response

    @step('Ввод пароля')
    def enter_password(self, password=None):
        if password is None:
            password = self.data.PASSWORD
        response = self.find_element(self.elements.PASSWORD_FIELD).send_keys(password)
        return response

    @step('Заполнение формы авторизации')
    def filling_form(self):
        self.enter_username()
        self.enter_password()

    @step('Поиск кнопки авторизации')
    def find_user_authorization_button(self):
        return self.find_element(self.elements.LOGIN_BUTTON)

