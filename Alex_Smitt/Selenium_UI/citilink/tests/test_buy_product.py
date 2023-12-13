from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

    # Инициализация страниц
    login = Login_page(driver)
    main = Main_page(driver)
    search_page = Search_page(driver)
    base = Base(driver)
    product_card = Product_card(driver)
    basket_page = Basket_page(driver)
    order_registration = Order_registration(driver)

    # Авторизация
    login.autorization()

    # Выбор продукта
    search_page.choose_product_from_list(1)
    base.click_element("//div[@class='ehanbgo0 app-catalog-127ajd9 e1loosed0']/div[1]//a[@class='app-catalog-9gnskf e1259i3g0']")
    product_title = product_card.get_product_title()
    product_price = product_card.get_product_price()

    # Добавление в корзину
    product_card.add_to_basket()

    # Переход в корзину
    product_card.click_go_to_basket()

    # Проверка цены и названия продукта в корзине
    basket_page.assert_price("//span[@class='e1j9birj0 e106ikdt0 css-zmmgir e1gjr6xo0']", product_price)
    basket_page.assert_title("//span[@class='e1ys5m360 e106ikdt0 css-175fskm e1gjr6xo0']", product_title)

    # Перейти к оформлению заказа
    product_card.go_to_checkout()

    # Ввод информации о пользователе
    order_registration.input_first_name("Vasya")
    order_registration.input_last_name("Pypkin")
    order_registration.input_telephone_number("+78524458056")

    """ Оставил закомментированым, поскольку на одной машине подтягивает геолокацию, на другой нет
    # Выбор пункта самовывоза
    oreg.click_choose_point()  # Перейти на список пунктов самовывоза
    oreg.click_select_point()  # Выбрать пункт самовывоза
    """

    # Активация чекбокса "Данные указаны верно"
    search_page.activate_checkbox("//span[@class='e11v1gn60 css-389ojc elcxude0']")
