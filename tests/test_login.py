from data import User
from conftest import driver
from locators import MainPageLocators, AuthPageLocators, RegistrationPageLocators, RecoverPageLocators
from urls import URLS
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def test_login_by_login_button_success(self, driver):
        """Вход в ЛК через кнопку 'Войти в аккаунт' на главной странице"""
        driver.get(URLS.BASE_URL)
        driver.find_element(*MainPageLocators.login_account_but).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(User.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(User.password)
        driver.find_element(*AuthPageLocators.login_account_but).click()

        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.place_order_but))
        order_but = driver.find_element(*MainPageLocators.place_order_but).text

        assert (driver.current_url == URLS.BASE_URL) and (order_but == 'Оформить заказ')

    def test_login_by_personal_account_button_success(self, driver):
        """Вход в ЛК через кнопку 'Личный кабинет' на главной странице"""
        driver.get(URLS.BASE_URL)
        driver.find_element(*MainPageLocators.personal_account_but).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(User.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(User.password)
        driver.find_element(*AuthPageLocators.login_account_but).click()

        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.place_order_but))
        order_but = driver.find_element(*MainPageLocators.place_order_but).text

        assert (driver.current_url == URLS.BASE_URL) and (order_but == 'Оформить заказ')

    def test_login_by_registration_form_success(self, driver):
        """Вход в личный кабинет через форму регистрации"""
        driver.get(URLS.REG_PAGE_URL)
        driver.find_element(*RegistrationPageLocators.login_account_but).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(User.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(User.password)
        driver.find_element(*AuthPageLocators.login_account_but).click()

        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.place_order_but))
        order_but = driver.find_element(*MainPageLocators.place_order_but).text

        assert (driver.current_url == URLS.BASE_URL) and (order_but == 'Оформить заказ')

    def test_login_by_recover_form_success(self, driver):
        """Вход в личный кабинет через форму восстановления"""
        driver.get(URLS.RECOVER_PAGE_URL)
        driver.find_element(*RecoverPageLocators.login_account_but).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(User.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(User.password)
        driver.find_element(*AuthPageLocators.login_account_but).click()
        
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.place_order_but))
        order_but = driver.find_element(*MainPageLocators.place_order_but).text
        
        assert (driver.current_url == URLS.BASE_URL) and (order_but == 'Оформить заказ')

    