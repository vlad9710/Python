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
    button_add_to_basket = "//span[@class='app-catalog-19y4hmw e1fnp08x0']"
    button_go_to_basket = "//div[@class='css-ass1ds egfuobq0']//button[@class='e4uhfkv0 css-gh3izc e4mggex0']"
    button_go_to_checkout = "//button[@class='e4uhfkv0 css-ch34l1 e4mggex0']"

    # Getters
    def get_product_title(self):  # Получить название продукта
        title = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_title))).text
        return title

    def get_product_price(self):  # Получить цену продукта
        price = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_price))).text
        return price.replace(' ', '')

    def get_add_to_basket(self):  # Получить кнопку получения заказа
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_basket)))

    def get_go_to_basket(self):  # Оформить заказ
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_go_to_basket)))
    def get_go_to_checkout(self):  # Оформить заказ
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_go_to_checkout)))

    # Actions
    def add_to_basket(self):  # Оформить заказ
        self.get_add_to_basket().click()

    def click_go_to_basket(self):  # Оформить заказ
        self.get_go_to_basket().click()

    def go_to_checkout(self):
        self.get_go_to_checkout().click()


