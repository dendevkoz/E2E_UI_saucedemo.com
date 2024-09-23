from pages.base_page import BasePage
from locators.locators import CartPageLocators
from allure import step

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.element = CartPageLocators

    @step('Поиск товара в корзине')
    def find_product_in_cart(self):
        return self.find_element(self.element.PRODUCT_IN_CART)

    @step('Переход к оформлению заказа')
    def find_checkout_button(self):
        return self.find_element(self.element.CHECKOUT_BUTTON)

