import allure

from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:

    @allure.title('Проверка открытия модального окна с деталями заказа по клику на заказ')
    @allure.description('Проверяем, что при клике на заказ открывается модальное окно с деталями заказа, '
                        'находим раздел «Состав»')
    def test_opened_window_with_order_details_by_click_on_order(self, driver):
        order_feed_page = OrderFeedPage(driver)
        assert order_feed_page.click_on_order() == 'Cостав'

    @allure.title('Проверка, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента '
                  'заказов»')
    @allure.description('Проверяем, что номер заказа из истории конкретного пользователя есть в списке всех заказов '
                        'на странице «Лента заказов», находим этот номер в ленте')
    def test_that_order_from_user_orders_history_are_in_order_feed(self, driver, create_and_delete_user):
        login_page = LoginPage(driver)
        login_page.login_new_user()
        order_feed_page = OrderFeedPage(driver)
        assert order_feed_page.find_order_from_user_order_history_on_order_feed_page() is True

    @allure.title('Проверка, что при создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    @allure.description('Проверяем, что при создании нового заказа счётчик «Выполнено за всё время» увеличивается, '
                        'сравниваем значение счетчика до и после создания заказа')
    def test_counter_of_completed_all_time_orders_increases_after_created_new_order(self, driver):
        order_feed_page = OrderFeedPage(driver)
        counter_before = order_feed_page.get_counter_number_of_complete_all_time_orders()
        login_page = LoginPage(driver)
        login_page.login_existing_user()
        order_feed_page.make_an_order()
        counter_after = order_feed_page.get_counter_number_of_complete_all_time_orders()
        assert int(counter_after) > int(counter_before)

    @allure.title('Проверка, что при создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    @allure.description('Проверяем, что при создании нового заказа счётчик «Выполнено за сегодня» увеличивается, '
                        'сравниваем значение счетчика до и после создания заказа')
    def test_counter_of_completed_today_orders_increases_after_created_new_order(self, driver):
        order_feed_page = OrderFeedPage(driver)
        counter_before = order_feed_page.get_counter_number_of_complete_today_orders()
        login_page = LoginPage(driver)
        login_page.login_existing_user()
        order_feed_page.make_an_order()
        counter_after = order_feed_page.get_counter_number_of_complete_today_orders()
        assert int(counter_after) > int(counter_before)

    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе «В работе»')
    @allure.description('Проверяем, что после создании нового заказа его номер появляется в разделе «В работе» на '
                        'странице «Лента заказов», проверяем, что номер заказа из модального окна есть в нужном списке')
    def test_that_order_number_in_progress_list(self, driver, create_and_delete_user):
        login_page = LoginPage(driver)
        login_page.login_new_user()
        order_feed_page = OrderFeedPage(driver)
        assert order_feed_page.find_order_number_in_the_in_progress_list() is True
