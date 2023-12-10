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
    slider_2 = "//div[@data-meta-name='FilterListGroupsLayout']//div[@class='rc-slider-handle rc-slider-handle-2']"

    # Getters
    def get_slider_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.slider_2)))

    # Method
    def activate_checkbox(self, checkbox):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, checkbox))).click()

    def move_slider_2(self, x, y):
        slider_2 = self.get_slider_2()
        self.actions.click_and_hold(slider_2).perform()
        time.sleep(1)  # Пауза на 1 секунду
        self.actions.move_by_offset(x, y).release().perform()

    # def assert_result(self, result):
    #     get_text = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='ehanbgo0 app-catalog-1yt54f0 e1loosed0']/div[1]"))).text
    #     print(result)
    #     print(get_text)
    #     # assert result == get_text
    #     print('Good result')


    def assert_result(self, result):
        # get_text = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='ehanbgo0 app-catalog-1yt54f0 e1loosed0']/div[1]"))).text
        get_text = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '{result}')]")))
        print(result)
        print(get_text)
        # assert result == get_text
        print('Good result')