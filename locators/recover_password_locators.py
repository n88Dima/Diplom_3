from selenium.webdriver.common.by import By

class PasswordRecLocators:
    BUTTON_RECOVERY_PASSWORD = (By.XPATH, '//a[contains(text(),"Восстановить пароль")]') #восстановление пароля
    RECOVERY_PASSWORD = (By.CLASS_NAME, 'input__textfield') #Поле ввода пароля
    BUTTON_RECOVERY = (By.XPATH, '//button[contains(text(),"Восстановить")]') #Кнопка Восстановить
    SAVE_RECOVERY = (By.XPATH, '//button[contains(text(),"Сохранить")]') #Кнопка Сохранить
    EYE_ICON = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]') #Раскрытие пароля

    # Активное поле ввода пароля
    ACTIVE_PASSWORD = (By.XPATH, '//div[contains(@class, "input_status_active")]')

    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')