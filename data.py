# переменная для присвоения драйвера
DRIVER_NAME = None

# адреса основных страниц
MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/'
LOGIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/login'
PASSWORD_RECOVERY_PAGE_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'
ORDER_FEED_PAGE = 'https://stellarburgers.nomoreparties.site/feed'

# URL основных эндпоинтов для АПИ (создание и удаление пользователя)
CREATE_USER_URL = 'api/auth/register'
DELETE_USER_URL = 'api/auth/user'

# данные для авторизации существующего пользователя
EXISTING_USER = {
    "email": "bga14@yandex.ru",
    "password": "password1"
}

# данные, сохраненные при генерации для нового пользователя
USER_DATA = None

# состояние списка заказов "В работе", когда все заказы выполнены
STATUS_ORDER_IN_PROGRESS = 'Все текущие заказы готовы!'
