from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:

    # заголовок формы восстановления пароля:
    TITLE_FORM_RECOVERY_PASSWORD = By.XPATH, '//h2[text()="Восстановление пароля"]'

    # поле для ввода эл.почты:
    EMAIL_INPUT_RECOVERY_PASSWORD = By.XPATH, '//label[text()="Email"]/parent::div/input'

    # кнопка "Восстановить":
    RECOVERY_PASSWORD_BUTTON = By.XPATH, '//button[text()="Восстановить"]'

    # ссылка "Восстановить пароль":
    RECOVERY_PASSWORD_LINK = By.XPATH, '//a[text()="Восстановить пароль"]'

    # кнопка показать/скрыть в поле "Пароль":
    PASSWORD_HIDE_BUTTON = By.XPATH, '//div[contains(@class,"input__icon-action")]'

    # кнопка "Сохранить":
    SAVE_BUTTON = By.XPATH, '//button[text()="Сохранить"]'

    # активное поле "Пароль", подсвеченное:
    PASSWORD_INPUT_ACTIVE = By.XPATH, '//label[text()="Пароль"]/parent::div/input[@type="text"]'
