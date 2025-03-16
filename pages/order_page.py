from locators.order_locators import OrderLocators
from pages.base_page import BasePage
import allure
import time

class OrderFeed(BasePage):
    @allure.step('Ожидание кнопки Лента заказов')
    def wait_order_feed(self):
        self.wait_visibility_element(OrderLocators.BUTTON_FEED_ORDERS)

    @allure.step('Клик по кнопке Лента заказов')
    def click_order_feed(self):
        self.click_element(OrderLocators.BUTTON_FEED_ORDERS)

    @allure.step('Клик по заказу')
    def click_order_in_feed(self):
        self.click_element(OrderLocators.ORDER_IN_FEED)

    @allure.step('Проверить наличие на странице окна заказа')
    def check_displaying_order_info(self):
        return self.check_displaying_element(OrderLocators.ORDER_INFO)

    @allure.step('Перетаскивание ингредиента в конструктор')
    def drag_and_drop_ingredient_to_burger_area(self):
        source_element = self.driver.find_element(*OrderLocators.BUN)
        target_element = self.driver.find_element(*OrderLocators.BURGER_AREA)

        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Ожидание булочки')
    def wait_bun(self):
        self.wait_clickable_element(OrderLocators.BURGER_AREA)

    @allure.step('Вход в аккаунт')
    def login_to_account(self, create_user):
        user_data, _, _ = create_user 
        email = user_data["email"]
        password = user_data["password"]


        self.click_element(OrderLocators.BUTTON_PERSONAL_ACCOUNT)
        self.enter_text(OrderLocators.LOGIN_INPUT, email)
        self.enter_text(OrderLocators.PASSWORD_INPUT, password)
        self.click_element(OrderLocators.LOGIN_BUTTON)


    @allure.step('Клик по созданию заказа')
    def click_order_create_button(self):
        self.click_element(OrderLocators.CREATE_ORDER)

    @allure.step('Клик по крестику закрытия окна с заказом')
    def click_order_exit_button(self):
        self.wait_clickable_element(OrderLocators.ORDER_EXIT_BUTTON)
        time.sleep(3)
        self.click_element(OrderLocators.ORDER_EXIT_BUTTON)

    @allure.step('Клик по Личный кабинет')
    def click_order_personal_account(self):
        self.wait_clickable_element(OrderLocators.BUTTON_PERSONAL_ACCOUNT)
        self.click_element(OrderLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Клик по История заказов')
    def click_history_order(self):
        self.wait_clickable_element(OrderLocators.HISTORY_ORDER)
        self.click_element(OrderLocators.HISTORY_ORDER)


    @allure.step('Получить номер заказа из истории')
    def text_history_order_number(self):
        self.wait_clickable_element(OrderLocators.HISTORY_ORDER_NUMBER)
        return self.get_text_element(OrderLocators.HISTORY_ORDER_NUMBER)

    @allure.step('Получить номер заказа из истории')
    def text_feed_order_number(self):
        self.wait_clickable_element(OrderLocators.FEED_ORDER_NUMBER)
        return self.get_text_element(OrderLocators.FEED_ORDER_NUMBER)

    @allure.step('Получить количество заказов за всё время')
    def text_order_all_time(self):
        self.wait_clickable_element(OrderLocators.ORDER_ALL_TIME)
        return self.get_text_element(OrderLocators.ORDER_ALL_TIME)

    @allure.step('Получить количество заказов за сегодня')
    def text_order_today(self):
        self.wait_clickable_element(OrderLocators.ORDER_TODAY)
        return self.get_text_element(OrderLocators.ORDER_TODAY)

    @allure.step('Клик по Конструктор')
    def click_constractor(self):
        self.wait_clickable_element(OrderLocators.CONSTRUCTOR_BUTTON)
        self.click_element(OrderLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Получить номер заказа после оформления')
    def text_order_number(self):
        self.wait_clickable_element(OrderLocators.ORDER_NUMBER)
        time.sleep(7)
        return self.get_text_element(OrderLocators.ORDER_NUMBER)

    @allure.step('Получить номер заказа в работе')
    def text_order_number_work(self):
        self.wait_clickable_element(OrderLocators.ORDER_NUMBER_WORK)
        return self.get_text_element(OrderLocators.ORDER_NUMBER_WORK)