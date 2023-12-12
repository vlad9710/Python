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
    first_popular_elem = "//a[@data-meta-category='cardId-1']"

    # Getters
    def get_search_line(self):  # Найти поисковую строку
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.search_line)))

    # Actions
    def input_search_line(self, user_request):  # Ввести значение в поисковую строку
        self.get_search_line().send_keys(user_request)

    # Methods
    def select_search_line(self, user_text):  # Произвести поиск по введенному значению в поисковой строке
        self.input_search_line(user_text)
        self.get_search_line().send_keys(Keys.ENTER)
