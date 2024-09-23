from selenium.webdriver.common.by import By


'''Поиск по 'ID' не сильно хорошо, но реализовано для экономии времени'''


class UserLoginLocators:
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')


class ProductCardLocators:
    PRODUCT = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")


class CartPageLocators:
    PRODUCT_IN_CART = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    CHECKOUT_BUTTON = (By.ID, "checkout")


class FirstCheckoutPageLocators:
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")


class LastCheckoutPageLocators:
    FINISH_BUTTON = (By.ID, "finish")


class CompleteCheckoutPageLocators:
    COMPLETE_MESSAGE = (By.CLASS_NAME, "complete-header")
