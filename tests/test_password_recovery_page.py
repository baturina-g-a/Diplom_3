import allure

from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecoveryPage:

    @allure.title('Проверка клика по кнопке «Восстановить пароль» на странице авторизации')
    @allure.description('Проверяем, что клик по кнопке «Восстановить пароль» на странице авторизации ведёт на '
                        'страницу восстановления пароля, находим заголовок формы «Восстановление пароля»')
    def test_click_password_recovery_button_opens_password_recovery_page(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        assert (password_recovery_page.click_password_recovery_button_opens_password_recovery_page() ==
                'Восстановление пароля')

    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить»')
    @allure.description('Проверяем, что после ввода почты в поле «Email» и клика по кнопке «Восстановить» открывается '
                        'форма для ввода и сохранения нового пароля, находим кнопку «Сохранить» в форме')
    def test_enter_email_and_click_password_recovery_button_password_field_appears(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.enter_email_in_field_email()
        assert password_recovery_page.click_password_recovery_button() == 'Сохранить'

    @allure.title('Проверка клика по кнопке показать/скрыть пароль (иконка глаза)')
    @allure.description('Проверяем, что клик по кнопке показать/скрыть пароль (иконка глаза) в поле «Пароль» делает '
                        'поле активным — подсвечивает его')
    def test_click_password_hide_button_activates_field_password(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        assert password_recovery_page.click_password_hide_button() == 'text'
