from selenium.webdriver.common.by import By


class ProfilePageLocators:

    # кнопка "Личный кабинет" в хедере:
    PROFILE_BUTTON = By.XPATH, '//p[text()="Личный Кабинет"]'

    # активная кнопка "Профиль" в личном кабинете:
    ACTIVE_PROFILE_BUTTON = By.XPATH, '//a[contains(@class,"Account_link_active") and text()="Профиль"]'

    # активная кнопка "История заказов" в личном кабинете:
    ACTIVE_ORDERS_HISTORY_BUTTON = By.XPATH, '//a[contains(@class,"Account_link_active") and text()="История заказов"]'

    # кнопка "История заказов":
    ORDERS_HISTORY_BUTTON = By.XPATH, '//a[text()="История заказов"]'

    # номер последнего заказа в списке заказов во вкладке "История заказов":
    LAST_ORDER_IN_HISTORY = By.XPATH, '//p[@class="text text_type_digits-default" and last()]'

    # кнопка "Выход" в личном кабинете:
    LOGOUT_BUTTON = By.XPATH, '//button[text()="Выход"]'

    # кнопка "Войти":
    LOGIN_BUTTON_AUTH = By.XPATH, '//button[text()="Войти"]'
