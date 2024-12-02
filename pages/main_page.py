import time

import allure

import data
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Открываем главную страницу')
    def get_to_main_page(self):
        self.get_to_url(data.MAIN_PAGE_URL)

    @allure.step('Переход в конструктор по клику на «Конструктор»')
    def click_constructor_button(self):
        self.get_to_url(data.LOGIN_PAGE_URL)
        if data.DRIVER_NAME == 'chrome':
            self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        else:
            self.click_to_element_for_firefox(MainPageLocators.CONSTRUCTOR_BUTTON)
        return self.get_text_from_element(MainPageLocators.FILLING_TAB)

    @allure.step('Клик на «Лента заказов»')
    def click_order_feed_button(self):
        self.get_to_main_page()
        if data.DRIVER_NAME == 'chrome':
            self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)
        else:
            self.click_to_element_for_firefox(MainPageLocators.ORDER_FEED_BUTTON)
        return self.return_current_url()

    @allure.step('Клик на ингредиент')
    def click_on_ingredient(self):
        self.get_to_main_page()
        self.implicitly_wait()
        self.click_virtual_mouse(MainPageLocators.INGREDIENT_BUN)
        return self.get_text_from_element(MainPageLocators.OPEN_MODAL_WINDOW_WITH_INGREDIENT_DETAILS)

    @allure.step('Клик на крест в модальном окне')
    def click_on_x_button_in_modal_window(self):
        # time.sleep(2)
        self.click_virtual_mouse(MainPageLocators.CLOSE_MODAL_WINDOW_BUTTON)
        return self.check_invisibility_of_element_located(MainPageLocators.OPEN_MODAL_WINDOW_WITH_INGREDIENT_DETAILS)

    @allure.step('Добавление ингредиента в заказ (переносим ингредиент в корзину - конструктор бургера)')
    def drag_and_drop_ingredient_into_the_cart(self):
        if data.DRIVER_NAME == 'chrome':
            self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.BURGER_CONSTRUCTOR_CART)
        else:
            self.drag_and_drop_element_for_firefox(MainPageLocators.INGREDIENT_BUN,
                                                   MainPageLocators.BURGER_CONSTRUCTOR_CART)

    @allure.step('Проверка каунтера ингредиента')
    def check_ingredient_counter(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_BUN_COUNTER)

    @allure.step('Клик на кнопку «Оформить заказ»')
    def click_make_order_button(self):
        if data.DRIVER_NAME == 'chrome':
            self.click_to_element(MainPageLocators.MAKE_ORDER_BUTTON)
        else:
            self.click_to_element_for_firefox(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Проверка создания заказа')
    def check_an_order_was_create(self):
        return self.get_text_from_element(MainPageLocators.OPEN_MODAL_WINDOW_WITH_ORDER_CONFIRM)

    @allure.step('Берём номер заказа')
    def get_new_order_number(self):
        return self.get_text_from_element(MainPageLocators.NEW_ORDER_NUMBER)

    @allure.step('Создание заказа')
    def make_an_order(self):
        self.drag_and_drop_ingredient_into_the_cart()
        self.click_make_order_button()
        self.click_on_x_button_in_modal_window()

    @allure.step('Создаем заказ и берём его номер')
    def make_an_order_and_get_number(self):
        self.drag_and_drop_ingredient_into_the_cart()
        self.click_make_order_button()
        self.implicitly_wait()
        self.check_an_order_was_create()
        new_order_number = self.get_new_order_number()
        self.click_on_x_button_in_modal_window()
        return new_order_number
