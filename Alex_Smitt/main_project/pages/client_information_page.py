from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Client_information_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions
    def input_first_name(self, user_name):
        self.get_first_name().send_keys(user_name)

    def input_last_name(self, user_password):
        self.get_last_name().send_keys(user_password)

    def input_postal_code(self, user_postal_code):
        self.get_postal_code().send_keys(user_postal_code)

    def click_continue_button(self):
        self.get_continue_button().click()

    # Methods
    def input_information(self):
        self.get_current_url()
        self.input_first_name('Ivan')
        self.input_last_name('Pypkin')
        self.input_postal_code('777')
        self.click_continue_button()
