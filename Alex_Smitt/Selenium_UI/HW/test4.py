from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import test3
import math

# Инициализация вебдрейвера и переход на сайт. Придание опции чтобы не закрывался браузер
o = Options()
o.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=o)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Создание переменных логин + пароль
standart_user = "standard_user"
password = "secret_sauce"

# Производится вход в аккаунт пользователя
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(standart_user)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
driver.find_element(By.XPATH, "//input[@id='login-button']").click()

# Добавляем товар в корзину
driver.find_element(By.XPATH, f"//div[@class='inventory_list']/div[{test3.product}]//button[@class='btn btn_primary btn_small btn_inventory ']").click()
price_1 = driver.find_element(By.XPATH, f"//div[@class='inventory_list']/div[{test3.product}]//div[@class='inventory_item_price']").text.replace('$', '')  # Записываем цену первой карточки и обрезаем первый символ в виде доллара

# Осуществляем переход в корзину
driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

# Подтверждаем заказ
driver.find_element(By.XPATH, "//button[@id='checkout']").click()

# Заполняем ФИО покупателя
driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("Ivan")
driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys("Petrov")
driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys("123456")

driver.find_element(By.XPATH, "//*[@id='continue']").click()

# Производим проверку суммы заказа
price_2 = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']").text.replace('Item total: $', '')  # Записываем сумму заказа, обрезая первые 12 символов
assert math.isclose(float(price_1), float(price_2))

# Завершение заказа
driver.find_element(By.XPATH, "//button[@id='finish']").click()

# Проверка что заказ оформлен успешно
assert driver.find_element(By.XPATH, "//h2[@class='complete-header']").text == "Thank you for your order!"
