from pages.account_page import AccountPage
from conftest import driver
import allure
from data import Urls

class TestPersonalAccount:

    @allure.title('Переход на «Личный кабинет»')
    def test_personal_account(self, driver, create_user):
        account_page = AccountPage(driver)

        account_page.wait_button_account()
        account_page.login_to_account(create_user)

        account_page.wait_button_personal_account()
        account_page.click_button_personal_account()

        account_page.wait_history_order()

        assert account_page.check_url() == Urls.PROFILE_URL

    @allure.title('Переход в раздел «История заказов»')
    def test_history_order(self, driver, create_user):
        account_page = AccountPage(driver)

        account_page.wait_button_account()
        account_page.login_to_account(create_user)

        account_page.wait_button_personal_account()
        account_page.click_button_personal_account()

        account_page.wait_history_order()
        account_page.click_history_order()

        assert account_page.check_url() == Urls.ORDER_HISTORY_URL

    @allure.title('Выход из аккаунта')
    def test_exit_order(self, driver, create_user):
        account_page = AccountPage(driver)

        account_page.wait_button_account()
        account_page.login_to_account(create_user)

        account_page.wait_button_personal_account()
        account_page.click_button_personal_account()

        account_page.wait_history_order()
        account_page.click_exit()

        assert account_page.get_url() == Urls.PROFILE_URL