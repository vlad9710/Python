from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Autorization import Login_page


class Test_1:
    def test_select_product(self):
        o = Options()
        o.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=o)
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        # Создание переменных логин + пароль
        d = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]
        password = "secret_sauce"

        for i in range(len(d)):
            Login_page(driver).autorization(d[i], password)  # Вызов функции авторизации, передача логина и пароля
            try:
                # Проверка наличия элемента ошибки ввода логина и пароля
                driver.find_element(By.XPATH, "//h3[@data-test='error']")
            except NoSuchElementException:
                # Код, который нужно выполнить, если элемент не найден
                print(f"Тест для пользователя {d[i]} пройден")
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[ @ id = 'react-burger-menu-btn']"))).click()  # Раскрытие бургер меню
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']"))).click()  # Выход
            else:
                # Код, который нужно выполнить, если элемент найден
                print(f"Тест для пользователя {d[i]} пройден")
                driver.refresh()


Test_1().test_select_product()
