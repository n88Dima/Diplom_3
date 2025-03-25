from pages.password_page import PasswordRecoveryPage
from conftest import driver
import allure
from data import Urls

class TestPasswordRecovery:

    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_button_recovery_password(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_button_personal_account()
        password_recovery_page.wait_button_recovery_password()
        password_recovery_page.click_button_recovery_password()
        assert password_recovery_page.get_url() == Urls.FORGOT_PASSWORD_URL

    @allure.description('Ввод почты и клик по кнопке «Восстановить»')
    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_email_click_recovery_password(self, driver, create_user):
        password_recovery_page = PasswordRecoveryPage(driver)

        user_data, response_data,_ = create_user


        password_recovery_page.click_button_personal_account()
        password_recovery_page.wait_button_recovery_password()
        password_recovery_page.click_button_recovery_password()

        password_recovery_page.enter_email_recovery_password(user_data['email'])
        password_recovery_page.click_button_recovery()
        password_recovery_page.wait_displaying_save()

        assert password_recovery_page.get_url() == Urls.RESET_PASSWORD_URL

    @allure.description('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_email_click_eye_icon(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_button_personal_account()
        password_recovery_page.wait_button_recovery_password()
        password_recovery_page.click_button_recovery_password()
        password_recovery_page.click_button_recovery()
        password_recovery_page.click_eye_icon()

        assert password_recovery_page.check_active_password()