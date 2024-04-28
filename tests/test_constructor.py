from locators import MainPageLocators
from urls import URLS
from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class TestConstructor:
    def test_switch_to_bun_constr_success(self, driver):
        """Проверка перехода к разделу 'Булки' в конструкторе"""
        driver.get(URLS.BASE_URL)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, MainPageLocators.sauces_by_span)))
        driver.find_element(By.XPATH, MainPageLocators.sauces_by_span).click()
        driver.find_element(By.XPATH, MainPageLocators.bun_by_span).click()
        assert driver.find_element(By.XPATH, MainPageLocators.active_tab_in_constructor).text == 'Булки'

    def test_switch_to_sauces_constr_success(self, driver):
        """Проверка перехода к разделу 'Соусы' в конструкторе"""
        driver.get(URLS.BASE_URL)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, MainPageLocators.sauces_by_span)))
        driver.find_element(By.XPATH, MainPageLocators.sauces_by_span).click()
        assert driver.find_element(By.XPATH, MainPageLocators.active_tab_in_constructor).text == 'Соусы'

    def test_switch_to_toppings_constr_success(self, driver):
        """Проверка перехода к разделу 'Начинки' в конструкторе"""
        driver.get(URLS.BASE_URL)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, MainPageLocators.topping_by_span)))
        driver.find_element(By.XPATH, MainPageLocators.topping_by_span).click()
        assert driver.find_element(By.XPATH, MainPageLocators.active_tab_in_constructor).text == 'Начинки'
