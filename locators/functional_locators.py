from selenium.webdriver.common.by import By

class FunctionalLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[contains(text(),"Конструктор")]') # Кнопка Конструктор
    
    BUTTON_FEED_ORDERS = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')  # Кнопка Лента заказов
    TITLE_FEED_ORDERS = (By.XPATH, '//h1[contains(text(),"Лента заказов")]') # Заголовок Лента заказов

    BUN = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]') # Ингредиент Флюоресцентная булка R2-D3
    BUN_INFO = (By.XPATH, '//h2[contains(text(),"Детали ингредиента")]') # Детали Флюоресцентная булка R2-D3
    INGREDIENT_MODAL_CLOSED = (By.XPATH, '//button[@type="button" and contains(@class, "Modal_modal__close_modified__3V5XS")]') # Крестик

    BURGER_AREA = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]') # Область для перетаскивания в бургера

    # Счётчик у булочки
    COUNTER_BUN = (By.XPATH,'.//a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p[@class="counter_counter__num__3nue1"][1]')

    # Кнопки для входа в аккаунт
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')
    LOGIN_INPUT = (By.XPATH, '//input[@name="name"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="Пароль"]')
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')

    # Кнопка Оформить заказ
    CREATE_ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')

    # Ваш заказ начали готовить
    MSG_START_ORDER = (By.XPATH, '//p[contains(text(),"Ваш заказ начали готовить")]')