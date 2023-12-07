from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):
    url = "https://www.saucedemo.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    username = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    main_word = "//span[@class='title']"

    # Getters
    def get_username(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.username)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions
    def input_username(self, user_name):
        self.get_username().send_keys(user_name)

    def input_password(self, user_password):
        self.get_password().send_keys(user_password)

    def click_login_button(self):
        self.get_login_button().click()

    def autorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_username('standard_user')
        self.input_password('secret_sauce')
        self.click_login_button()
        self.get_page_title(self.get_main_word(), 'Products')
