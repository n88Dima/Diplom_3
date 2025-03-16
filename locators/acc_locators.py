from selenium.webdriver.common.by import By

class AccountLocators:
    # Кнопка личный кабинет
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')

    # Кнопки для входа в аккаунт
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')
    LOGIN_INPUT = (By.XPATH, '//input[@name="name"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="Пароль"]')
    EXIT_BUTTON = (By.XPATH, '//button[contains(text(),"Выход")]') # Кнопка Выход
    
    HISTORY_ORDER = (By.XPATH, '//a[contains(text(),"История заказов")]') # Кнопка история заказов

    CREATE_ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]') #оформить заказ