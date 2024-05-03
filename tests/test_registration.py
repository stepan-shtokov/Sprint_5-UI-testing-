from data import User, RandomUser
from conftest import driver
from locators import RegistrationPageLocators, AuthPageLocators
from urls import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestRegistrationPage:
    
    def test_registration_success(self, driver):
        """Проверка регистрации рандомного пользователя"""
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(RegistrationPageLocators.registration_but))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(RandomUser.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(RandomUser.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(RandomUser.password)
        driver.find_element(*RegistrationPageLocators.registration_but).click()
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(AuthPageLocators.login_account_auth_form_but))
        login_button_displayed = driver.find_element(*AuthPageLocators.login_account_auth_form_but).is_displayed()

        assert driver.current_url == URLS.AUTH_PAGE_URL and login_button_displayed

    def test_registration_incorrect_password_check_error(self, driver):
        """Проверка регистрации пользователя с некорректным паролем (менее 6 символов)"""
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(RegistrationPageLocators.registration_but))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(RandomUser.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(RandomUser.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(12345)
        driver.find_element(*RegistrationPageLocators.registration_but).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_any_elements_located(RegistrationPageLocators.error_message_incorrect_pass))
        error = driver.find_element(*RegistrationPageLocators.error_message_incorrect_pass).text

        assert (error == 'Некорректный пароль') and (driver.current_url == URLS.REG_PAGE_URL)

    def test_double_registration_check_error(self, driver):
        """Проверка повторной регистрации пользователя"""
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(RegistrationPageLocators.registration_but))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(User.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(User.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(User.password)
        driver.find_element(*RegistrationPageLocators.registration_but).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(RegistrationPageLocators.error_message_double_register))
        error = driver.find_element(*RegistrationPageLocators.error_message_double_register).text

        assert (error == 'Такой пользователь уже существует') and (driver.current_url == URLS.REG_PAGE_URL)
        