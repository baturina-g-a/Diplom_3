from selenium.webdriver.common.by import By


class LoginPageLocators:

    # поле для ввода эл.почты:
    EMAIL_INPUT_AUTH = (By.XPATH, '//label[text()="Email"]/parent::div/input')

    # поле для ввода пароля:
    PASSWORD_INPUT_AUTH = (By.XPATH, '//label[text()="Пароль"]/parent::div/input')

    # кнопка "Войти":
    LOGIN_BUTTON_AUTH = By.XPATH, '//button[text()="Войти"]'

    # overlay:
    OVERLAY_ON_LOGIN_PAGE = By.XPATH, '//div[@class="Modal_modal_overlay__x2ZCr"]'
