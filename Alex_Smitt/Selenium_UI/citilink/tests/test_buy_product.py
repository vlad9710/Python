from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.authorization import Login_page
from pages.main_page import Main_page
from pages.search_page import Search_page
from base.base_class import Base
from pages.product_card_page import Product_card
from pages.basket_page import Basket_page
from pages.order_registration_page import Order_registration


def test_select_product():
    o = Options()
    o.add_experimental_option("detach", True)
    o.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=o)

    # Создание переменных
    login = Login_page(driver)
    main = Main_page(driver)
    sp = Search_page(driver)
    bc = Base(driver)
    pc = Product_card(driver)
    bp = Basket_page(driver)
    oreg = Order_registration(driver)

    login.autorization()  # Открытие сайта
    sp.choose_product_from_list(1)  # Выбрать элемент из списка. В параметрах передать порядковый номер
    pc.get_product_title()  # Записать наименование товара
    pc.get_product_price()  # Записать цену товара
    pc.place_order()  # оформить заказ
    """насчет метода не особо уверен. По хорошему бы его вынести в какое-то другое место. Но идей нет, пока что сделал так"""
    bp.assert_price("//*[@class='e1ys5m360 e106ikdt0 css-zmmgir e1gjr6xo0']")  # Сравнить цену с записанной на предыдущих шагах
    bp.assert_title("//span[@class='e1ys5m360 e106ikdt0 css-175fskm e1gjr6xo0']")  # Сравнить название товара с записанным на предыдущих шагах
    bp.get_go_to_registration()  # Перейти к оформлению
    bp.assert_price("//*[@class='e1ys5m360 e106ikdt0 css-zmmgir e1gjr6xo0']")  # Сравнить цену с записанной на предыдущих шагах
    bp.assert_title("//span[@class='e27li280 e106ikdt0 css-1qo2d1j e1gjr6xo0']")  # Сравнить название товара с записанным на предыдущих шагах
    oreg.input_first_name("Vasya")  # Вставить имя
    oreg.input_last_name("Pypkin")  # Вставить фамилию
    oreg.input_telephone_number("+78524458056")  # Вставить номер телефона
    oreg.click_choose_point()  # Перейти на список пунктов самовывоза
    oreg.click_select_point()  # Выбрать пункт самовывоза
    sp.activate_checkbox("//input[@id='contactPaymentConfirm']")
