from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.product_card_page import Product_card

class Basket_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # Locators


    # Getters


    # Actions


    # Methods
    def assert_price(self, locator, price):
        price_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator)))
        assert (price_1.text.replace('₽', '').replace(' ', '')) == price

    def assert_title(self, locator, title):
        title_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator)))
        print(title_1.text)
        print(title)
        assert title_1.text == title
