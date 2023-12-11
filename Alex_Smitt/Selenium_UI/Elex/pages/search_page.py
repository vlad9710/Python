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
    def get_detailed_directory_mode(self):  # Найти кнопку переключения каталога в детальный режим
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.detailed_directory_mode)))

    def get_slider_2(self):  # Найти слайдер максимальной цены
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.slider_2)))

    def get_checkbox(self, checkbox):  # Найти чекбокс
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, checkbox)))

    # Actions
    def activate_detailed_directory_mode(self):  # Активировать кнопку переключения каталога в детальном режиме
        self.get_detailed_directory_mode().click()

    def activate_checkbox(self, checkbox):  # Активировать чекбокс
        self.get_checkbox(checkbox).click()

    # Method
    def move_slider_2(self, x, y):  # Переместить слайдер максимальной цены
        slider_2 = self.get_slider_2()
        self.actions.click_and_hold(slider_2).perform()
        time.sleep(1)  # Пауза на 1 секунду
        self.actions.move_by_offset(x, y).release().perform()

    def assert_result(self, count):  # Проверить количество найденного товара
        elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ehanbgo0 app-catalog-127ajd9 e1loosed0']")))
        get_count = elem.get_attribute('data-meta-row-count')
        assert str(count) == str(get_count)
