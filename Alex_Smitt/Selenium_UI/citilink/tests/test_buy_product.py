from pages.authorization import Login_page
from pages.main_page import Main_page
from pages.search_page import Search_page
from base.base_class import Base
from pages.basket_page import Basket_page
from pages.product_card_page import Product_card


def test_buy_product(driver):
    # Инициализация страниц
    login = Login_page(driver)
    main = Main_page(driver)
    search_page = Search_page(driver)
    base = Base(driver)
    product_card = Product_card(driver)
    basket_page = Basket_page(driver)

    # Авторизация
    login.autorization()

    # Выбор продукта
    search_page.choose_product_from_list(1)
    base.click_element("//div[@class='ehanbgo0 app-catalog-127ajd9 e1loosed0']/div[1]//a[@class='app-catalog-9gnskf e1259i3g0']")
    product_title = product_card.get_product_title()
    product_price = product_card.get_product_price()
    print(product_price, product_title)

    # Добавление в корзину
    base.click_element("//span[@class='app-catalog-19y4hmw e1fnp08x0']")

    # Переход в корзину
    base.click_element("//div[@class='css-ass1ds egfuobq0']//button[@class='e4uhfkv0 css-gh3izc e4mggex0']")

    # Проверка цены и названия продукта в корзине
    basket_page.assert_price("//span[@class='e1j9birj0 e106ikdt0 css-zmmgir e1gjr6xo0']", product_price)
    basket_page.assert_title("//span[@class='e1ys5m360 e106ikdt0 css-175fskm e1gjr6xo0']", product_title)

    # Перейти к оформлению заказа
    base.click_element("//button[@class='e4uhfkv0 css-ch34l1 e4mggex0']")

    # Ввод информации о пользователе
    base.input_value("//input[@name='contact-form_firstName']", "Vasya")
    base.input_value("//input[@name='contact-form_lastName']", "Pypkin")
    base.input_value("//input[@name='contact-form_phone']", "+78524458056")

    """ Оставил закомментированым, поскольку на одной машине подтягивает геолокацию, на другой нет
    # Выбор пункта самовывоза
    oreg.click_choose_point()  # Перейти на список пунктов самовывоза
    oreg.click_select_point()  # Выбрать пункт самовывоза
    """

    # Активация чекбокса "Данные указаны верно"
    base.click_element("//span[@class='e11v1gn60 css-389ojc elcxude0']")
