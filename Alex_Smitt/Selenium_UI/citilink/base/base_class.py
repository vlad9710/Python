import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    # Метод определяющий URL страницы
    def get_current_url(self):
        get_url = self.driver.current_url

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