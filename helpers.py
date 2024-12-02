import random
import string

import allure

from faker import Faker

import data


@allure.step('Создание данных для нового пользователя')
def generate_random_user_data():
    letters = string.ascii_lowercase
    random_string_password = ''.join(random.choice(letters) for i in range(8))
    random_string_name = ''.join(random.choice(letters) for i in range(8))
    fake = Faker()
    new_email = fake.email()
    payload = {
        "email": new_email,
        "password": random_string_password,
        "name": random_string_name
    }
    data.USER_DATA = payload
    return data.USER_DATA
