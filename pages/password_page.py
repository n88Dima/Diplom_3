from locators.recover_password_locators import PasswordRecLocators
from pages.base_page import BasePage
import allure

class PasswordRecoveryPage(BasePage):
    @allure.step('Ожидание кнопки «Восстановить пароль»')
    def wait_button_recovery_password(self):
        self.wait_visibility_element(PasswordRecLocators.BUTTON_RECOVERY_PASSWORD)

    @allure.step('Клик по кнопке «Восстановить пароль»')
    def click_button_recovery_password(self):
        self.click_element(PasswordRecLocators.BUTTON_RECOVERY_PASSWORD)

    @allure.step('Ожидание кнопки поля почты')
    def wait_email_recovery_password(self):
        self.wait_visibility_element(PasswordRecLocators.RECOVERY_PASSWORD)

    @allure.step('Ввод почты')
    def enter_email_recovery_password(self, test_mail):
        self.enter_text(PasswordRecLocators.RECOVERY_PASSWORD, test_mail)

    @allure.step('Клик по кнопке «Восстановить»')
    def click_button_recovery(self):
        self.click_element(PasswordRecLocators.BUTTON_RECOVERY)

    @allure.step('Проверить наличие на странице кнопки сохранить')
    def wait_displaying_save(self):
        return self.wait_visibility_element(PasswordRecLocators.SAVE_RECOVERY)

    @allure.step('Клик по иконке открытия пароля')
    def click_eye_icon(self):
        self.click_element(PasswordRecLocators.EYE_ICON)

    @allure.step('Проверить что поле пароль активно')
    def check_active_password(self):
        return self.check_displaying_element(PasswordRecLocators.ACTIVE_PASSWORD)

    @allure.step('Получить ссылку текущей страницы')
    def check_url(self):
        return self.get_url()
    
    @allure.step('Ожидание кнопки «Личный кабинет»')
    def wait_button_personal_account(self):
        self.wait_clickable_element(PasswordRecLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Клик по кнопке «Личный кабинет»')
    def click_button_personal_account(self):
        self.click_element(PasswordRecLocators.BUTTON_PERSONAL_ACCOUNT)