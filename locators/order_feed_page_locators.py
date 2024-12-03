from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    # последний заказ из ленты заказов:
    LAST_ORDER_IN_ORDERS_FEED = By.XPATH, '//li[contains(@class,"OrderHistory_list") and last()]'

    # открытое модальное окно с деталями заказа:
    OPEN_MODAL_WINDOW_WITH_ORDER_DETAILS = By.XPATH, '//section[contains(@class,"modal_opened")]'

    # состав заказа в модальном окне с деталями заказа:
    ORDER_COMPONENTS_IN_MODAL_WINDOW_WITH_ORDER_DETAILS = By.XPATH, ('//section[contains(@class,"modal_opened")]//p['
                                                                     'text()="Cостав"]')

    # номер заказа в ленте заказов:
    ORDER_NUMBER_IN_ORDERS_FEED = By.XPATH, '//p[@class="text text_type_digits-default"]'

    # счётчик заказов "Выполнено за всё время":
    ALL_TIME_ORDERS_COUNTER = By.XPATH, ('//p[text()="Выполнено за все время:"]/parent::div/p[contains(@class,'
                                         '"OrderFeed_number")]')

    # счётчик заказов "Выполнено за сегодня":
    TODAY_ORDERS_COUNTER = By.XPATH, ('//p[text()="Выполнено за сегодня:"]/parent::div/p[contains(@class,'
                                      '"OrderFeed_number")]')

    # список заказов "В работе":
    ORDERS_LIST_IN_PROGRESS = By.XPATH, '//ul[contains(@class,"OrderFeed_orderListReady")]/li[contains(@class,"text")]'
