from pages.functional_page import FunctionsPage
from conftest import driver
import allure
from data import Urls

class TestFunctions:

    @allure.title(f'Проверка что будет {Urls.BASE_URL} клику на «Конструктор»')
    def test_click_button_constructor(self, driver):
        func = FunctionsPage(driver)

        func.wait_button_constructor()
        func.click_button_constructor()
        assert func.check_url() == Urls.BASE_URL

    @allure.title('Переход в Лента заказов')
    def test_click_order_feed(self, driver):
        func = FunctionsPage(driver)

        func.wait_button_constructor()
        func.click_button_order_feed()
        assert func.check_displaying_title_feed_order()

    @allure.title('Проверка что будет открыто окно с информацией о булочке')
    def test_click_ingredient(self, driver):
        func = FunctionsPage(driver)
        func.click_ingredient()
        assert func.check_ingredient_info()


    @allure.title('Закрытие окна с информацией о булочке')
    def test_ingredient_closed(self, driver):
        func = FunctionsPage(driver)

        func.click_ingredient()
        func.wait_close()
        func.click_close()
        assert func.check_closed

    @allure.title('Каунтер +2 если добавить булку в конструктор')
    def test_drag_and_drop_ingredient(self, driver):
        func = FunctionsPage(driver)

        func.wait_bun()
        func.drag_and_drop_ingredient_to_burger_area()
        assert func.get_count_of_ingredients() == '2'

    @allure.title('Оформление заказа залогинниным пользователем')
    def test_order_login_user(self, driver, create_user):
        func = FunctionsPage(driver)

        func.wait_button_constructor()
        func.login_to_account(create_user)

        func.wait_bun()
        func.drag_and_drop_ingredient_to_burger_area()
        func.click_order()
        assert func.check_order