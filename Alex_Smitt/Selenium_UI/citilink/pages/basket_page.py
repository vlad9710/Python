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
    go_to_registration = "//button[@class='e4uhfkv0 css-ch34l1 e4mggex0']"

    # Getters
    def get_go_to_registration(self):  # Оформить заказ
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.go_to_registration)))

    # Actions
    def click_go_to_registration(self):  # Оформить заказ
        self.get_go_to_registration().click()

    # Methods
    def assert_price(self, locator):
        price_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator)))
        assert (price_1.text.replace('₽', '').replace(' ', '')) == Product_card.price

    def assert_title(self, locator):
        title_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator)))
        assert title_1.text == Product_card.title
