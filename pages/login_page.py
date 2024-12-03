import allure

import data
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Ждем, когда пропадет overlay')
    def wait_for_overlay_to_disappear(self):
        self.wait_for_element_to_disappear(LoginPageLocators.OVERLAY_ON_LOGIN_PAGE)

    @allure.step('Авторизация существующего пользователя')
    def login_existing_user(self):
        self.get_to_url(data.LOGIN_PAGE_URL)
        self.add_text_to_field(LoginPageLocators.EMAIL_INPUT_AUTH, data.EXISTING_USER['email'])
        self.add_text_to_field(LoginPageLocators.PASSWORD_INPUT_AUTH, data.EXISTING_USER['password'])
        self.wait_for_overlay_to_disappear()
        if data.DRIVER_NAME == 'chrome':
            self.click_to_element(LoginPageLocators.LOGIN_BUTTON_AUTH)
        else:
            self.click_to_element_for_firefox(LoginPageLocators.LOGIN_BUTTON_AUTH)

    @allure.step('Авторизуем созданного пользователя')
    def login_new_user(self):
        self.get_to_url(data.LOGIN_PAGE_URL)
        self.add_text_to_field(LoginPageLocators.EMAIL_INPUT_AUTH, data.USER_DATA['email'])
        self.add_text_to_field(LoginPageLocators.PASSWORD_INPUT_AUTH, data.USER_DATA['password'])
        self.wait_for_overlay_to_disappear()
        if data.DRIVER_NAME == 'chrome':
            self.click_to_element(LoginPageLocators.LOGIN_BUTTON_AUTH)
        else:
            self.click_to_element_for_firefox(LoginPageLocators.LOGIN_BUTTON_AUTH)
