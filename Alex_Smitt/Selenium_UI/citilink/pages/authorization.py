from base.base_class import Base


class Login_page(Base):
    url = "https://www.citilink.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    def autorization(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
