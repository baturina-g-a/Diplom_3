import allure
import pytest
import requests
from selenium import webdriver

import data
import helpers


@allure.step('Фикстура драйвера')
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=chrome_options)
        data.DRIVER_NAME = 'chrome'
        yield driver
    else:
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=firefox_options)
        driver.maximize_window()
        data.DRIVER_NAME = 'firefox'
        yield driver
        driver.quit()


@pytest.fixture()
def create_and_delete_user():
    payload = helpers.generate_random_user_data()
    response = requests.post(f'{data.MAIN_PAGE_URL}{data.CREATE_USER_URL}', json=payload)
    response = response.json()
    yield response['accessToken']
    requests.delete(f'{data.MAIN_PAGE_URL}{data.DELETE_USER_URL}',
                    headers={'Authorization': response['accessToken']})
