from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Order_registration(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # Locators
    first_name = "//input[@name='contact-form_firstName']"
    last_name = "//input[@name='contact-form_lastName']"
    telephone_number = "//input[@name='contact-form_phone']"
    choose_point = "//button[@class='e4uhfkv0 css-a9m9r e4mggex0']"
    select_point = "//div[@class='css-db6o6g ekqustz0']/div[1]//button[@data-meta-name='SelfDeliveryStoresList__select-button']"

    # Getters
    def get_first_name(self):  # Найти поле ввода имени
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):  # Найти поле ввода фамилии
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_telephone_number(self):  # Найти поле ввода номера телефона
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.telephone_number)))

    def get_choose_point(self):  # Найти поле ввода номера телефона
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.choose_point)))

    def get_select_point(self):  # Найти поле ввода номера телефона
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_point)))

    # Actions
    def input_first_name(self, name):  # Ввести значение в поле ввода имени
        self.get_first_name().send_keys(name)

    def input_last_name(self, surname):  # Ввести значение в поле ввода фамилии
        self.get_last_name().send_keys(surname)

    def input_telephone_number(self, tel_number):  # Ввести значение в поле ввода номера телефона
        self.get_telephone_number().send_keys(tel_number)

    def click_choose_point(self):  # Выбрать пункт самовывоза
        self.get_choose_point.click()

    def click_select_point(self):  # Выбрать пункт самовывоза
        self.get_select_point.click()
    # Methods
