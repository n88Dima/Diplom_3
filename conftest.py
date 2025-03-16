import pytest
import requests
from selenium import webdriver
from faker import Faker
from data import Urls

fake = Faker()

@pytest.fixture(params=['chrome', 'firefox']) 
def driver(request):
    match request.param: 
        case 'chrome':
            options = webdriver.ChromeOptions()
            browser = webdriver.Chrome(options=options)
        case 'firefox':
            options = webdriver.FirefoxOptions()
            browser = webdriver.Firefox(options=options)
        case _:
            raise ValueError(f"Unsupported browser: {request.param}") 
        
    browser.get(Urls.BASE_URL)

    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def create_user():
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }

    response = requests.post(Urls.REGISTER_USER, json=user_data)
    response_data = response.json()

    yield user_data, response_data, response.status_code

    access_token = response_data['accessToken']
    requests.delete(Urls.DELETE_USER, headers={'Authorization': access_token})