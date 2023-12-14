import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Search_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # Locators
    detailed_directory_mode = ".//*[@data-meta-name='ViewSwitcherVariant__list']/.."
    slider_2 = "//div[@data-meta-name='FilterListGroupsLayout']//div[@class='rc-slider-handle rc-slider-handle-2']"

    # Getters
    # Найти слайдер максимальной цены
    def get_slider_2(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.slider_2)))

    # Найти карточку товара
    def get_product_from_list(self, number):
        product_from_list = f"//div[@class='edhylph0 app-catalog-1ljlt6q e3tyxgd0']/a[{number}]//span[@class='e1ys5m360 e106ikdt0 app-catalog-1bu1ack e1gjr6xo0']"
        elem = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, product_from_list)))
        return elem

    # Actions
    # Method
    # Переместить слайдер максимальной цены
    def move_slider_2(self, x, y):
        slider_2 = self.get_slider_2()
        self.actions.click_and_hold(slider_2).perform()
        time.sleep(1)  # Пауза на 1 секунду
        self.actions.move_by_offset(x, y).release().perform()

    # Проверить количество карточек
    def check_list_count(self, count):
        elem = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ehanbgo0 app-catalog-127ajd9 e1loosed0']")))
        get_count = elem.get_attribute('data-meta-row-count')
        assert str(count) == str(get_count)

    # Перейти на страницу карточки товара
    def choose_product_from_list(self, number):
        self.get_product_from_list(number).click()
