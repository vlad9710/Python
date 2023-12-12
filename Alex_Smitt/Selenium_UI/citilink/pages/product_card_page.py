from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Product_card(Base):
    title = None
    price = None
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # Locators
    product_title = "//div[@class='ehanbgo0 app-catalog-127ajd9 e1loosed0']/div[1]//a[@class='app-catalog-9gnskf e1259i3g0']"
    product_price = "//div[@class='ehanbgo0 app-catalog-127ajd9 e1loosed0']/div[1]//span[@class='e1j9birj0 e106ikdt0 app-catalog-j8h82j e1gjr6xo0']"
    order_product = "//div[@class='ehanbgo0 app-catalog-127ajd9 e1loosed0']/div[1]//button[@data-meta-name='Snippet__cart-button']"

    # Getters
    def get_product_title(self):  # Получить название продукта
        Product_card.title = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_title))).text
        return Product_card.title

    def get_product_price(self):  # Получить цену продукта
        Product_card.price = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))
        return Product_card.price.text.replace(' ', '')

    def get_order_product(self):  # Получить кнопку получения заказа
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.order_product)))

    # Actions
    def place_order(self):  # Оформить заказ
        self.get_order_product().click()
