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

    login = Login_page(driver)
    login.autorization()

    ssl = Main_page(driver)
    ssl.select_search_line("Видеокарта")



    sp = Search_page(driver)
    sp.assert_result('Видеокарта MSI NVIDIA  GeForce RTX 3060 RTX 3060 VENTUS 2X 12G OC')
    sp.move_slider_2(-200, 0)

    bc = Base(driver)
    bc.scroll_page(0, 1000)

    sp.activate_checkbox("//div[@data-meta-value='4,5 и выше']")
    sp.activate_checkbox("//div[@data-meta-value='POWERCOLOR']")

    bc.scroll_page(0, -1000)
    sp.assert_result("Видеокарта PowerColor AMD  Radeon RX 6400 AXRX 6400 4GBD6-DH")
