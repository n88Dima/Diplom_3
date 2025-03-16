from selenium.webdriver.common.by import By

class OrderLocators:
    ORDER_IN_FEED = (By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[1]') # Заказ из списка
    ORDER_INFO = (By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4.Modal_modal__P3_V5") # Окно с заказом
    ORDER_EXIT_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK") # Кнопка закрытия оформления заказа
    HISTORY_ORDER = (By.XPATH, '//a[contains(text(),"История заказов")]') # Кнопка история заказов
    HISTORY_ORDER_NUMBER = (By.XPATH, "//p[@class='text text_type_digits-default']") # Номер заказа в истории заказов
    FEED_ORDER_NUMBER = (By.XPATH, "(//p[@class='text text_type_digits-default'])[1]") # Номер заказа в ленте заказов
    ORDER_ALL_TIME = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]") # Выполнено за все время
    ORDER_TODAY = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]") # Выполнено за сегодня
    ORDER_NUMBER = (By.XPATH,"//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq') and contains(@class, 'Modal_modal__title__2L34m')]") # Номер заказа в окне после оформления
    ORDER_NUMBER_WORK = (By.XPATH,"//li[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2')]") # Номер заказа в окне после оформления
    
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')


    

    BUTTON_FEED_ORDERS = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')  # Кнопка Лента заказов
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[contains(text(),"Конструктор")]') # Кнопка Конструктор
    
    BUN = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]') # Ингредиент Флюоресцентная булка R2-D3
    BURGER_AREA = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]') # Область для перетаскивания в бургера

     # Кнопки для входа в аккаунт
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')
    LOGIN_INPUT = (By.XPATH, '//input[@name="name"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="Пароль"]')

    # Кнопка Оформить заказ
    CREATE_ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')