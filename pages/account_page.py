from locators.acc_locators import AccountLocators
from pages.base_page import BasePage
import allure

class AccountPage(BasePage):

    @allure.step('Вход в аккаунт')
    def login_to_account(self, create_user):
        user_data, _, _ = create_user 
        email = user_data["email"]
        password = user_data["password"]


        self.click_element(AccountLocators.BUTTON_PERSONAL_ACCOUNT)
        self.enter_text(AccountLocators.LOGIN_INPUT, email)
        self.enter_text(AccountLocators.PASSWORD_INPUT, password)
        self.click_element(AccountLocators.LOGIN_BUTTON)

    @allure.step('Ожидание кнопки «Войти»')
    def wait_button_account(self):
        self.wait_clickable_element(AccountLocators.LOGIN_BUTTON)

    @allure.step('Клик по кнопке «Войти»')
    def click_button_account(self):
        self.click_element(AccountLocators.LOGIN_BUTTON)

    @allure.step('Ожидание кнопки «Личный кабинет»')
    def wait_button_personal_account(self):
        self.wait_clickable_element(AccountLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Клик по кнопке «Личный кабинет»')
    def click_button_personal_account(self):
        self.click_element(AccountLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Ожидание кнопки «История заказов»')
    def wait_history_order(self):
        self.wait_clickable_element(AccountLocators.HISTORY_ORDER)

    @allure.step('Клик кнопки «История заказов»')
    def click_history_order(self):
        self.click_element(AccountLocators.HISTORY_ORDER)

    @allure.step('Клик кнопки «Выход»')
    def click_exit(self):
        self.click_element(AccountLocators.EXIT_BUTTON)

    @allure.step('Получить ссылку текущей страницы')
    def check_url(self):
        return self.get_url()