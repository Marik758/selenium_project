from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators
class ProductPage(BasePage):
    def add_to_basket(self):
        self.name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        self.price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_basket.click()

    def true_name(self):
        name_in_basket = self.browser.find_element(*BasketPageLocators.NAME_PRODUCT).text
        assert self.name_product == name_in_basket, "Invalid name"
        print('Good')
        
    def true_price(self):
        price_in_basket = self.browser.find_element(*BasketPageLocators.PRICE_PRODUCT).text
        assert self.price_product == price_in_basket, "Invalid price"
        print('Good 2')
    
