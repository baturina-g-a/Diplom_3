import allure

from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class TestProfilePage:

    @allure.title('Проверка перехода в личный кабинет по клику на кнопку «Личный кабинет»')
    @allure.description('Проверяем, что клик по кнопке «Личный кабинет» в хедере ведёт на страницу личный кабинет, '
                        'находим активную вкладку «Профиль»')
    def test_move_to_profile_by_click_on_profile_button(self, driver):
        login_page = LoginPage(driver)
        login_page.login_existing_user()
        profile_page = ProfilePage(driver)
        assert profile_page.click_profile_button() == 'Профиль'

    @allure.title('Проверка перехода в раздел «История заказов»')
    @allure.description('Проверяем, что по клику на вкладку «История заказов» открывается история заказов '
                        'пользователя, проверяем, что вкладке «История заказов» стала активной')
    def test_move_to_orders_history(self, driver):
        login_page = LoginPage(driver)
        login_page.login_existing_user()
        profile_page = ProfilePage(driver)
        assert profile_page.click_orders_history_button() == 'История заказов'

    @allure.title('Проверка выход из аккаунта по клику на кнопку «Выход»')
    @allure.description('Проверяем, что по клику по кнопке «Выход» в личном кабинете, происходит выход из аккаунта и '
                        'переход на страницу авторизации, находим кнопку «Войти»')
    def test_account_logout_by_click_logout_button(self, driver):
        login_page = LoginPage(driver)
        login_page.login_existing_user()
        profile_page = ProfilePage(driver)
        assert profile_page.click_logout_button() == 'Войти'
