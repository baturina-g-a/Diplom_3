import allure

import data
from locators.profile_page_locators import ProfilePageLocators
from pages.main_page import MainPage


class ProfilePage(MainPage):

    @allure.step('Клик на «Личный кабинет»')
    def click_profile_button(self):
        self.find_element_with_wait(ProfilePageLocators.PROFILE_BUTTON)
        self.implicitly_wait()
        if data.DRIVER_NAME == 'chrome':
            self.click_to_element(ProfilePageLocators.PROFILE_BUTTON)
            self.click_virtual_mouse(ProfilePageLocators.PROFILE_BUTTON)
        else:
            self.click_to_element_for_firefox(ProfilePageLocators.PROFILE_BUTTON)
            self.click_virtual_mouse(ProfilePageLocators.PROFILE_BUTTON)
        return self.get_text_from_element(ProfilePageLocators.ACTIVE_PROFILE_BUTTON)

    @allure.step('Клик на кнопку «История заказов»')
    def click_orders_history_button(self):
        self.click_profile_button()
        if data.DRIVER_NAME == 'chrome':
            self.click_to_element(ProfilePageLocators.ORDERS_HISTORY_BUTTON)
        else:
            self.click_to_element_for_firefox(ProfilePageLocators.ORDERS_HISTORY_BUTTON)
        return self.get_text_from_element(ProfilePageLocators.ACTIVE_ORDERS_HISTORY_BUTTON)

    @allure.step('Клик на кнопку «Выход»')
    def click_logout_button(self):
        self.click_profile_button()
        if data.DRIVER_NAME == 'chrome':
            self.click_to_element(ProfilePageLocators.LOGOUT_BUTTON)
        else:
            self.click_to_element_for_firefox(ProfilePageLocators.LOGOUT_BUTTON)
        return self.get_text_from_element(ProfilePageLocators.LOGIN_BUTTON_AUTH)

    @allure.step('Берём номер заказа из истории заказов пользователя')
    def get_order_number_from_user_orders_history(self):
        self.make_an_order()
        self.click_orders_history_button()
        return self.get_text_from_element(ProfilePageLocators.LAST_ORDER_IN_HISTORY)
