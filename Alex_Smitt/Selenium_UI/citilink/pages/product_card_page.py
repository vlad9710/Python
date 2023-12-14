from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Product_card(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # Locators
    product_title = "//h1[@class='e1ubbx7u0 eml1k9j0 app-catalog-tn2wxd e1gjr6xo0']"
    product_price = "//span[@class='e1j9birj0 e106ikdt0 app-catalog-1f8xctp e1gjr6xo0']"

    # Getters
    def get_product_title(self):  # Получить название продукта
        title = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_title)))
        return title.text

    def get_product_price(self):  # Получить цену продукта
        price = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))
        return price.text.replace('₽', '').replace(' ', '')
    # Actions
