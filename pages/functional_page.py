from locators.functional_locators import FunctionalLocators
from pages.base_page import BasePage
import allure

class FunctionsPage(BasePage):
    @allure.step('Ожидание кнопки «Конструктор»')
    def wait_button_constructor(self):
        self.wait_visibility_element(FunctionalLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по кнопке «Конструктор»')
    def click_button_constructor(self):
        self.click_element(FunctionalLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по кнопке «Лента заказов»')
    def click_button_order_feed(self):
        self.click_element(FunctionalLocators.BUTTON_FEED_ORDERS)

    @allure.step('Проверить наличие на странице заголовка «Лента заказов»')
    def check_displaying_title_feed_order(self):
        return self.check_displaying_element(FunctionalLocators.TITLE_FEED_ORDERS)

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        self.click_element(FunctionalLocators.BUN)

    @allure.step('Открытие карточки ингредиента')
    def check_ingredient_info(self):
        return self.check_displaying_element(FunctionalLocators.BUN_INFO)

    @allure.step('Клик по крестику')
    def click_close(self):
        self.click_element(FunctionalLocators.INGREDIENT_MODAL_CLOSED)

    @allure.step('Ожидание крестика')
    def wait_close(self):
        self.wait_clickable_element(FunctionalLocators.INGREDIENT_MODAL_CLOSED)

    @allure.step('Проверить отсутствие крестика')
    def check_closed(self):
        return not self.check_displaying_element(FunctionalLocators.INGREDIENT_MODAL_CLOSED)

    @allure.step('Перетаскивание ингредиента в конструктор')
    def drag_and_drop_ingredient_to_burger_area(self):
        source_element = self.driver.find_element(*FunctionalLocators.BUN)
        target_element = self.driver.find_element(*FunctionalLocators.BURGER_AREA)

        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Получить количество ингредиентов')
    def get_count_of_ingredients(self):
        return self.get_text_element(FunctionalLocators.COUNTER_BUN)

    @allure.step('Ожидание булочки')
    def wait_bun(self):
        self.wait_clickable_element(FunctionalLocators.BUN)

    @allure.step('Вход в аккаунт')
    def login_to_account(self, create_user):
        user_data, _, _ = create_user 
        email = user_data["email"]
        password = user_data["password"]


        self.click_element(FunctionalLocators.BUTTON_PERSONAL_ACCOUNT)
        self.enter_text(FunctionalLocators.LOGIN_INPUT, email)
        self.enter_text(FunctionalLocators.PASSWORD_INPUT, password)
        self.click_element(FunctionalLocators.LOGIN_BUTTON)
        

    @allure.step('Оформить заказ')
    def click_order(self):
        self.click_element(FunctionalLocators.CREATE_ORDER)

    @allure.step('Проверить появление окна заказа')
    def check_order(self):
        return self.check_displaying_element(FunctionalLocators.CREATE_ORDER)

    @allure.step('Получить ссылку текущей страницы')
    def check_url(self):
        return self.get_url()