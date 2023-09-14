import time
from .pages.product_page import ProductPage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math




 

@pytest.mark.parametrize('promo_offer', ['0','1','2','3','4','5','6', pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_basket(browser,promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"



    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.add_to_basket()        # выполняем метод страницы — переходим на страницу логина
    print('Add basket')
#    time.sleep(3)
    page.solve_quiz_and_get_code()
    
    page.true_name()
    page.true_price()

    
