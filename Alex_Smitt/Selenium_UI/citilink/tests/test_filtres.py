from pages.authorization import Login_page
from pages.main_page import Main_page
from pages.search_page import Search_page
from base.base_class import Base


def test_filtres(driver):
    # Создание переменных
    login = Login_page(driver)
    main = Main_page(driver)
    search_page = Search_page(driver)
    base = Base(driver)

    # Открытие сайта и вход в систему
    login.autorization()

    # Ввод данных в поисковую строку
    main.select_search_line("Видеокарта")

    # Активация детального режима
    base.click_element(".//*[@data-meta-name='ViewSwitcherVariant__list']/..")

    # Настройка фильтров максимальной цены
    search_page.move_slider_2(-200, 0)

    # Скроллинг страницы вниз
    base.scroll_page(0, 1000)

    # Активация фильтров
    base.click_element("//div[@data-meta-value='4,5 и выше']")
    base.click_element("//div[@data-meta-value='POWERCOLOR']")

    # Скроллинг страницы вверх
    base.scroll_page(0, -1000)

    # Сравнение результатов
    search_page.check_list_count(1)
