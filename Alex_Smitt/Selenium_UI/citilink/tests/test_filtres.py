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

    login.autorization()  # Открытие сайта
    main.select_search_line("Видеокарта")  # Ввод данных в поисковик
    sp.activate_detailed_directory_mode()  # Активация детального режима
    sp.move_slider_2(-200, 0)  # Настройка фильтров максимальной цены
    bc.scroll_page(0, 1000)  # Скроллинг страницы вниз
    sp.activate_checkbox("//div[@data-meta-value='4,5 и выше']")  # Активация фильтров
    sp.activate_checkbox("//div[@data-meta-value='POWERCOLOR']")
    bc.scroll_page(0, -1000)  # Скроллинг страницы вверх

    sp.check_list_count(1)  # Сравнение результатов
