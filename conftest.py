import pytest
from selenium import webdriver
from locators import MainPageLocators, AuthPageLocators
from urls import URLS
from data import User


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def get_login_driver(driver):
    driver.get(URLS.BASE_URL)
    driver.find_element(*MainPageLocators.personal_account_but).click()
    driver.find_element(*AuthPageLocators.email_input).send_keys(User.email)
    driver.find_element(*AuthPageLocators.password_input).send_keys(User.password)
    driver.find_element(*AuthPageLocators.login_account_but).click()
