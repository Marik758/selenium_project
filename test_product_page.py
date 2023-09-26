import time
from .pages.product_page import ProductPage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math




 

#@pytest.mark.parametrize('promo_offer', ['0','1','2','3','4','5','6', pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
#def test_guest_can_add_product_to_basket(browser,promo_offer):

#    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"

#def test_guest_can_add_product_to_basket(browser):
#
#    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{1}"
#
#
#    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#    page.open()                      # открываем страницу
#    page.add_to_basket()        # выполняем метод страницы — переходим на страницу логина
#    print('Add basket')
##    time.sleep(3)
#    page.solve_quiz_and_get_code()
#
#    page.true_name()
#    page.true_price()
#
#    page.success_message_should_disappear()
    
@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


    page = ProductPage(browser, link, 0)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_to_basket()        # выполняем метод страницы — переходим на страницу логина
        
    page.should_not_be_success_message()

    

    
def test_guest_cant_see_success_message(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


    page = ProductPage(browser, link, 0)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


    page = ProductPage(browser, link, 0)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_to_basket()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
