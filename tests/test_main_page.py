import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка перехода в конструктор бургеров по клику на кнопку «Конструктор»')
    @allure.description('Проверяем, что клик по кнопке «Конструктор» в хедере ведёт на главную страницу с '
                        'конструктором бургеров, находим таб «Начинки»')
    def test_move_to_constructor_by_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        assert main_page.click_constructor_button() == 'Начинки'

    @allure.title('Проверка перехода в ленту заказов по клику на кнопку «Лента заказов»')
    @allure.description('Проверяем, что клик по кнопке «Лента заказов» в хедере ведёт на страницу ленты заказов, '
                        'сравниваем текущий URL с ожидаемым')
    def test_move_to_order_feed_by_click_on_order_feed_button(self, driver):
        main_page = MainPage(driver)
        assert main_page.click_order_feed_button() == 'https://stellarburgers.nomoreparties.site/feed'

    @allure.title('Проверка открытия модального окна с деталями ингредиента по клику на ингредиент')
    @allure.description('Проверяем, что при клике на ингредиент открывается модальное окно с деталями ингредиента, '
                        'находим заголовок «Детали ингредиента»')
    def test_opened_window_with_ingredient_details_by_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        assert main_page.click_on_ingredient() == 'Детали ингредиента'

    @allure.title('Проверка закрытия модального окна с деталями ингредиента по клику кнопку закрыть(х)')
    @allure.description('Проверяем, что при клике на кнопку закрыть(х) модальное окно с деталями ингредиента '
                        'закрывается, проверяем что на странице нет открытого модального окна')
    def test_close_window_with_ingredient_details_by_click_on_x_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        assert main_page.click_on_x_button_in_modal_window() is True

    @allure.title('Проверка увеличения каунтера ингредиента при добавлении ингредиента в корзину')
    @allure.description('Проверяем, что при добавлении ингредиента в корзину его каунтер увеличивается, на примере '
                        'булочек, проверям, что добовляются сразу две')
    def test_ingredient_counter_increased_when_ingredient_added_to_cart(self, driver):
        main_page = MainPage(driver)
        main_page.get_to_main_page()
        main_page.drag_and_drop_ingredient_into_the_cart()
        assert main_page.check_ingredient_counter() == '2'

    @allure.title('Проверка, что авторизованный пользователь может создать заказ')
    @allure.description('Проверяем, что авторизованный пользователь может добавить ингредиенты в корзину и нажать на '
                        'кнопку «Оформить заказ», при этом открывается модальное окно с подтверждением создания '
                        'заказа, находим подтверждающий текст в модальном окне')
    def test_authorized_user_can_make_an_order(self, driver, create_and_delete_user):
        login_page = LoginPage(driver)
        login_page.login_new_user()
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient_into_the_cart()
        main_page.click_make_order_button()
        assert main_page.check_an_order_was_create() == 'Ваш заказ начали готовить'
