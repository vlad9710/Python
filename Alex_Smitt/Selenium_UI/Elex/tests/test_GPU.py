from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.authorization import Login_page
from pages.main_page import Main_page
from pages.search_page import Search_page


def test_select_product():
    o = Options()
    o.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=o)

    login = Login_page(driver)
    login.autorization()

    ssl = Main_page(driver)
    ssl.select_search_line("Видеокарта")

    sp = Search_page(driver)
    sp.activate_checkbox("//input[@data-max='7000']")
    sp.activate_checkbox("//input[@value='powercolor']")
    sp.apply()
    sp.assert_result("")
