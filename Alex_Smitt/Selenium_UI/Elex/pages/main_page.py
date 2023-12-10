from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    search_line = "//input[@type='search']"

    # Getters
    def get_search_line(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.search_line)))

    def get_elem_by_locator(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.search_line)))
    # Actions
    def input_search_line(self, user_request):
        self.get_search_line().send_keys(user_request)

    # Methods
    def select_search_line(self, user_text):
        self.get_current_url()
        self.input_search_line(user_text)
        self.get_search_line().send_keys(Keys.ENTER)

    def assert_result(self, result, locator):
        loc = self.get_elem_by_locator(locator)
