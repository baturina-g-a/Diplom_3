import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    @allure.step('Инициализируем драйвер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу')
    def get_to_url(self, url):
        self.driver.get(url)

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Поиск элементов с ожиданием')
    def find_elements_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Клик по элементу, когда он стал кликабелен')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Ждем присутствия элемента на странице')
    def wait_presence_of_element_located(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Клик по элементу для FireFox')  # взяла метод с вебинара, возможно, надо будет поправить под себя
    def click_to_element_for_firefox(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click(element).perform()

    @allure.step('Вводим текст в поле')
    def add_text_to_field(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получаем текст из элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Ждём, когда элемент станет невидимым')
    def wait_for_element_to_disappear(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element(locator))

    @allure.step('Возвращаем текущий URL')
    def return_current_url(self):
        return self.driver.current_url

    @allure.step('Кликаем виртуальной мышкой')
    def click_virtual_mouse(self, locator):
        action = ActionChains(self.driver)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        action.click(on_element=element).perform()

    @allure.step('Проверяем, что элемента нет на странице')
    def check_invisibility_of_element_located(self, locator):
        if WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator)):
            return True
        else:
            return False

    @allure.step('Берём и перетаскиваем элемент')
    def drag_and_drop_element(self, locator_from, locator_to):
        element_from = self.find_element_with_wait(locator_from)
        element_to = self.find_element_with_wait(locator_to)
        action = ActionChains(self.driver)
        action.drag_and_drop(element_from, element_to).perform()

    @allure.step('Берём и перетаскиваем элемент в FireFox')
    def drag_and_drop_element_for_firefox(self, locator_from, locator_to):
        self.find_element_with_wait(locator_from)
        self.find_element_with_wait(locator_to)
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script("""
        var source = arguments[0];
        var target = arguments[1];
        var evt = document.createEvent("DragEvent");
        evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        source.dispatchEvent(evt);
        evt = document.createEvent("DragEvent");
        evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        target.dispatchEvent(evt);
        evt = document.createEvent("DragEvent");
        evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        target.dispatchEvent(evt);
        evt = document.createEvent("DragEvent");
        evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        target.dispatchEvent(evt);
        evt = document.createEvent("DragEvent");
        evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        source.dispatchEvent(evt);
        """, element_from, element_to)

    @allure.step('Проверяем, что текст есть в элементе')
    def check_that_text_is_in_element(self, locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))

    @allure.step('Проверяем, что текст пропал из элемента')
    def check_that_text_is_not_in_element(self, locator, text):
        WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(locator, text))

    @allure.step('Неявное ожидание')
    def implicitly_wait(self):
        self.driver.implicitly_wait(5)
