from locators import MainPageLocators
from urls import URLS
from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestConstructor:
    def test_switch_to_bun_constr_success(self, driver):
        """Проверка перехода к разделу 'Булки' в конструкторе"""
        driver.get(URLS.BASE_URL)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.sauces_by_span))
        driver.find_element(*MainPageLocators.sauces_by_span).click()
        driver.find_element(*MainPageLocators.bun_by_span).click()
        assert driver.find_element(*MainPageLocators.active_tab_in_constructor).text == 'Булки'

    def test_switch_to_sauces_constr_success(self, driver):
        """Проверка перехода к разделу 'Соусы' в конструкторе"""
        driver.get(URLS.BASE_URL)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.sauces_by_span))
        driver.find_element(*MainPageLocators.sauces_by_span).click()
        assert driver.find_element(*MainPageLocators.active_tab_in_constructor).text == 'Соусы'

    def test_switch_to_toppings_constr_success(self, driver):
        """Проверка перехода к разделу 'Начинки' в конструкторе"""
        driver.get(URLS.BASE_URL)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.topping_by_span))
        driver.find_element(*MainPageLocators.topping_by_span).click()
        assert driver.find_element(*MainPageLocators.active_tab_in_constructor).text == 'Начинки'
