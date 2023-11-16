from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def sould_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BUTTON_GO_TO_DECOR),\
        "Button is presented, but should not be"
        
    def sould_be_empty_basket_message(self):
        assert self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY).text\
        == 'Ваша корзина пуста Продолжить покупки', "Error basket message"
        

