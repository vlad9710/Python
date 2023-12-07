from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Search_page(Base):
    def __init__(self, driver, checkbox):
        super().__init__(driver)
        self.checkbox = checkbox
        self.driver = driver

    # Locators
    confirm = "//button[@data-role='filters-submit']"
    result = "//div[@data-product='8c12d3e8-2d96-11ec-8f06-00155d8ed20b']"

    # Getters
    def get_checkbox(self, checkbox):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkbox)))

    def get_confirm(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.confirm)))

    # Actions
    # Methods
    def activate_checkbox(self, checkbox):
        self.get_checkbox(checkbox)

    def apply(self):
        self.get_confirm()

    def assert_result(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good URL')
