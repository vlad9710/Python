import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # Метод определяющий URL страницы
    def get_current_url(self):
        get_url = self.driver.current_url
        return get_url

    # Метод определяющий заголовок страницы
    def get_page_title(self, word, result):
        value_word = word.text
        assert value_word == result

    # Метод сохраняющий скриншот
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        file_name = f"screenshot_{now_date}.png"
        self.driver.save_screenshot(f'screen\\{file_name}')

    # Метод определяющий текущий URL
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result

    # Метод проивзодящий скроллинг страницы
    def scroll_page(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    # Метод производящий клик по элементу
    def click_element(self, locator):
        elem = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, locator)))
        return elem.click()

    # Метод получения текста элемента
    def get_text(self, locator):
        elem = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, locator)))
        return elem.text

    # Метод ввода значения в элемент
    def input_value(self, locator, value):
        elem = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, locator)))
        elem.send_keys(value)
