from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADRESS = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    
class ProductPageLocators():
    VIUY_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BUTTON_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    NAME_PRODUCT = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

class BasketPageLocators():
    NAME_PRODUCT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    BUTTON_GO_TO_DECOR = (By.CSS_SELECTOR, "#content_inner > div.form-group.clearfix > div > div > a")
    MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BUTTON_BASKET = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")



