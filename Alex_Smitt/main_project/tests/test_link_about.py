from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.autorization import Login_page
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish
from pages.main_page import Main_page
from pages.payment import Payment


def test_link_about():
    o = Options()
    o.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=o)

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.select_menu_about()
