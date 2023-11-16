from .base_page import BasePage
from .locators import LoginPageLocators
from faker import Faker

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        
    
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_ADRESS).send_keys(email)
        input_pass = self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        input_pass2 = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD).send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button_register.click()

        


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current url is default"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN_FORM is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER_FORM is not presented"
