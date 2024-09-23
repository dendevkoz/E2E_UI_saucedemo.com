from pages.base_page import BasePage
from locators.locators import ProductCardLocators
from allure import step


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.elements = ProductCardLocators

    @step('Поиск товара')
    def find_product(self):
        return self.find_element(self.elements.PRODUCT)

    @step('Добавление товара в корзину')
    def find_button_add_to_cart(self):
        return self.find_element(self.elements.ADD_TO_CART_BUTTON)


    @step('Поиск кнопки "Корзина"')
    def find_cart_button(self):
        cart_button = self.find_element(self.elements.CART_ICON)
        return cart_button



