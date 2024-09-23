from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.first_checkout_page import FirstCheckoutPage
from pages.last_checkout_page import LastCheckoutPage
from pages.complete_checkout_page import CompleteCheckoutPage
import allure

'''Можно реализовать иным способом, но я не знаю стандарты компании'''


def test_shop(browser):
    login_page_step = LoginPage(browser)
    product_page_step = ProductPage(browser)
    cart_page_step = CartPage(browser)
    first_checkout_page = FirstCheckoutPage(browser)
    last_checkout_page = LastCheckoutPage(browser)
    complete_checkout_page = CompleteCheckoutPage(browser)
    login_page_step.go_to_site()
    with allure.step('Авторизация пользователя'):
        login_page_step.filling_form()
        login_page_step.find_user_authorization_button().click()
    with allure.step('Добавление товара в корзину'):
        product_page_step.wait_to_url('/inventory')
        product_page_step.find_button_add_to_cart().click()
    with allure.step('Переход в раздел "Корзина'):
        product_page_step.find_cart_button().click()
    with allure.step('Проверка, что товар добавлен '):
        product_in_cart = cart_page_step.find_product_in_cart()
        assert product_in_cart is not None
    with allure.step('Переход к оформлению покупки'):
        cart_page_step.find_checkout_button().click()
    with allure.step('Cледующий шаг оформления'):
        first_checkout_page.filling_form()
        first_checkout_page.find_continue_button().click()
    with allure.step('Завершение покупки'):
        last_checkout_page.find_finish_button().click()
    with allure.step('Подтверждение покупки'):
        complete = complete_checkout_page.proof_of_purchase().text
        assert complete == 'Thank you for your order!'
