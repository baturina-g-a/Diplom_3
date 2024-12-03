from selenium.webdriver.common.by import By


class MainPageLocators:

    # кнопка «Войти в аккаунт»:
    LOGIN_BUTTON_FROM_MAIN_PAGE = By.XPATH, '//button[text()="Войти в аккаунт"]'

    # кнопка "Личный кабинет" в хедере:
    PROFILE_BUTTON = By.XPATH, '//p[text()="Личный Кабинет"]'

    # кнопка "Оформить заказ":
    MAKE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'

    # кнопка "Конструктор" в хедере:
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]'

    # кнопка "Лента заказов" в хедере:
    ORDER_FEED_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]'

    # ингредиент булка:
    INGREDIENT_BUN = By.XPATH, '//p[text()="Краторная булка N-200i"]/parent::a/p[contains(@class,"BurgerIngredient")]'

    # счетчик булки:
    INGREDIENT_BUN_COUNTER = By.XPATH, '//img[@alt = "Краторная булка N-200i"]/preceding-sibling::div/p'

    # таб "Начинки" в конструкторе бургеров:
    FILLING_TAB = By.XPATH, '//span[text() = "Начинки"]'

    # открытое модальное окно с деталями ингредиента:
    OPEN_MODAL_WINDOW_WITH_INGREDIENT_DETAILS = By.XPATH, ('//section[contains(@class,"modal_opened")]/div/div/h2['
                                                           'text()="Детали ингредиента"]')

    # корзина, конструктор бургера (зона добавления ингредиентов):
    BURGER_CONSTRUCTOR_CART = By.XPATH, '//ul[contains(@class,"BurgerConstructor_basket")]'

    # модальное окно подтверждения создания заказа:
    OPEN_MODAL_WINDOW_WITH_ORDER_CONFIRM = By.XPATH, ('//section[contains(@class,"modal_opened")]/div/div/div/p[text('
                                                      ')="Ваш заказ начали готовить"]')

    # номер заказа из модального окна:
    NEW_ORDER_NUMBER = By.XPATH, '//h2[contains(@class,"Modal_modal__title_shadow")]'

    # крест в модальном окне:
    CLOSE_MODAL_WINDOW_BUTTON = By.XPATH, ('//section[contains(@class,"modal_opened")]/div//*[name()="svg" and '
                                           '@xmlns="http://www.w3.org/2000/svg" and contains(@fill,"F2F2F3")]')

    # overlay:
    MODAL_OVERLAY = '//div[@class="Modal_modal_overlay__x2ZCr"]'
