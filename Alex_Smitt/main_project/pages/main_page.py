from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    select_product_1 = f"//div[@class='inventory_list']/div[1]//button[@class='btn btn_primary btn_small btn_inventory ']"
    cart = "//a[@class='shopping_cart_link']"
    menu = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"

    # Getters
    def get_select_product_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))

    # Actions
    def click_select_product_1(self):
        self.get_select_product_1().click()

    def click_cart(self):
        self.get_cart().click()

    def click_menu(self):
        self.get_menu().click()
    def click_link_about(self):
        self.get_link_about().click()

    # Methods
    def select_product(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_link_about()
        self.assert_url('https://saucelabs.com/')
