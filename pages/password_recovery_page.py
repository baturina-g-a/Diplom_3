import allure

import data
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):

    @allure.step('Открываем страницу восстановления пароля по ссылке')
    def get_to_password_recovery_page(self):
        self.get_to_url(data.PASSWORD_RECOVERY_PAGE_URL)

    @allure.step('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def click_password_recovery_button_opens_password_recovery_page(self):
        self.get_to_url(data.LOGIN_PAGE_URL)
        if data.DRIVER_NAME == 'chrome':
            self.click_to_element(PasswordRecoveryPageLocators.RECOVERY_PASSWORD_LINK)
        else:
            self.click_to_element_for_firefox(PasswordRecoveryPageLocators.RECOVERY_PASSWORD_LINK)
        return self.get_text_from_element(PasswordRecoveryPageLocators.TITLE_FORM_RECOVERY_PASSWORD)

    @allure.step('Ввод почты в поле «Email»')
    def enter_email_in_field_email(self):
        self.get_to_password_recovery_page()
        self.add_text_to_field(PasswordRecoveryPageLocators.EMAIL_INPUT_RECOVERY_PASSWORD, data.EXISTING_USER['email'])

    @allure.step('Клик по кнопке «Восстановить»')
    def click_password_recovery_button(self):
        if data.DRIVER_NAME == 'chrome':
            self.implicitly_wait()
            self.click_to_element(PasswordRecoveryPageLocators.RECOVERY_PASSWORD_BUTTON)
        else:
            self.click_to_element_for_firefox(PasswordRecoveryPageLocators.RECOVERY_PASSWORD_BUTTON)
        return self.get_text_from_element(PasswordRecoveryPageLocators.SAVE_BUTTON)

    @allure.step('Клик по кнопке показать/скрыть пароль')
    def click_password_hide_button(self):
        self.enter_email_in_field_email()
        self.click_password_recovery_button()
        if data.DRIVER_NAME == 'chrome':
            self.click_to_element(PasswordRecoveryPageLocators.PASSWORD_HIDE_BUTTON)
        else:
            self.click_to_element_for_firefox(PasswordRecoveryPageLocators.PASSWORD_HIDE_BUTTON)
        return self.find_element_with_wait(PasswordRecoveryPageLocators.PASSWORD_INPUT_ACTIVE).get_attribute('type')
