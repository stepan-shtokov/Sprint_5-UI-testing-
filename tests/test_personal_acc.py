from locators import MainPageLocators, PersonalAreaLocators, AuthPageLocators
from conftest import driver, get_login_driver
from urls import URLS
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestPersonalAcc:
    
    def test_go_to_pesonal_acc_from_main_page_success(self, driver, get_login_driver):
        """Проверка перехода в ЛК с главной страницы по кнопке 'Личный кабинет' """
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(MainPageLocators.personal_account_but))
        driver.find_element(*MainPageLocators.personal_account_but).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(PersonalAreaLocators.exit_but))
        save_button_displayed = driver.find_element(*PersonalAreaLocators.save_but).is_displayed()

        assert driver.current_url == URLS.PROFILE_PAGE_URL and save_button_displayed

    def test_go_from_personal_acc_to_constructor_by_click_on_constructor_button_success(self, driver, get_login_driver):
        """Проверка перехода из ЛК в конструктор по кнопке "Конструктор" """
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainPageLocators.personal_account_but))
        driver.find_element(*MainPageLocators.personal_account_but).click()
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(PersonalAreaLocators.exit_but))
        driver.find_element(*PersonalAreaLocators.constructor_but).click()
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainPageLocators.place_order_but))
        order_button_main_page = driver.find_element(*MainPageLocators.place_order_but)

        assert driver.current_url == URLS.BASE_URL and order_button_main_page.text == "Оформить заказ"

    def test_go_from_personal_acc_to_constr_by_click_on_logo_success(self, driver, get_login_driver):
        """Проверка перехода из ЛК в конструктор по клику на логотип SB """
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainPageLocators.personal_account_but))
        driver.find_element(*MainPageLocators.personal_account_but).click()
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(PersonalAreaLocators.exit_but))
        driver.find_element(*PersonalAreaLocators.logo_but).click()
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(MainPageLocators.place_order_but))
        order_button_main_page = driver.find_element(*MainPageLocators.place_order_but)

        assert driver.current_url == URLS.BASE_URL and order_button_main_page.text == "Оформить заказ"

    def test_logout_from_personal_acc_success(self, driver, get_login_driver):
        """Проверка выхода из личного кабинета"""
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(MainPageLocators.personal_account_but))
        driver.find_element(*MainPageLocators.personal_account_but).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PersonalAreaLocators.exit_but))
        driver.find_element(*PersonalAreaLocators.exit_but).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(AuthPageLocators.login_account_but))
        login_button = driver.find_element(*AuthPageLocators.login_account_but)

        assert driver.current_url == URLS.AUTH_PAGE_URL and login_button.text == 'Войти'
