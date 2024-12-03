import allure

import data
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.profile_page import ProfilePage


class OrderFeedPage(ProfilePage):

    @allure.step('Открываем страницу «Лента заказов»')
    def get_to_order_feed_page(self):
        self.get_to_url(data.ORDER_FEED_PAGE)

    @allure.step('Клик на заказ')
    def click_on_order(self):
        self.get_to_order_feed_page()
        if data.DRIVER_NAME == 'chrome':
            self.click_to_element(OrderFeedPageLocators.LAST_ORDER_IN_ORDERS_FEED)
        else:
            self.click_to_element_for_firefox(OrderFeedPageLocators.LAST_ORDER_IN_ORDERS_FEED)
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_COMPONENTS_IN_MODAL_WINDOW_WITH_ORDER_DETAILS)

    @allure.step('Находим заказ пользователя из раздела «История заказов» на странице «Лента заказов»')
    def find_order_from_user_order_history_on_order_feed_page(self):
        order_number = self.get_order_number_from_user_orders_history()
        self.get_to_order_feed_page()
        orders_list = self.find_elements_with_wait(OrderFeedPageLocators.ORDER_NUMBER_IN_ORDERS_FEED)
        result = None
        for order in orders_list:
            numbers = order.text
            if order_number == numbers:
                result = True
        return result

    @allure.step('Берём показатель счетчика «Выполнено за всё время»')
    def get_counter_number_of_complete_all_time_orders(self):
        self.get_to_order_feed_page()
        return self.get_text_from_element(OrderFeedPageLocators.ALL_TIME_ORDERS_COUNTER)

    @allure.step('Берём показатель счетчика «Выполнено за сегодня»')
    def get_counter_number_of_complete_today_orders(self):
        self.get_to_order_feed_page()
        return self.get_text_from_element(OrderFeedPageLocators.TODAY_ORDERS_COUNTER)

    @allure.step('Находим номер заказа после его оформления в разделе «В работе»')
    def find_order_number_in_the_in_progress_list(self):
        order_number = "0" + self.make_an_order_and_get_number()
        self.get_to_order_feed_page()
        self.check_that_text_is_in_element(OrderFeedPageLocators.ORDERS_LIST_IN_PROGRESS,
                                           data.STATUS_ORDER_IN_PROGRESS)
        self.check_that_text_is_not_in_element(OrderFeedPageLocators.ORDERS_LIST_IN_PROGRESS,
                                               data.STATUS_ORDER_IN_PROGRESS)
        self.wait_presence_of_element_located(OrderFeedPageLocators.ORDERS_LIST_IN_PROGRESS)
        orders_in_progress_list = self.find_elements_with_wait(OrderFeedPageLocators.ORDERS_LIST_IN_PROGRESS)
        result = None
        for order in orders_in_progress_list:
            numbers = order.text
            if order_number in numbers:
                result = True
        return result
