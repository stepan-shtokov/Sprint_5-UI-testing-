from locators import MainPageLocators
from urls import URLS
from conftest import driver


class TestConstructor:
    def test_switch_to_bun_constr_success(self, driver):
        """Проверка перехода к разделу 'Булки' в конструкторе"""
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_but).click()
        driver.find_element(*MainPageLocators.buns_but).click()
        bun_text = driver.find_element(*MainPageLocators.bun_txt).text
        bun_displayed = driver.find_element(*MainPageLocators.bun_ul).is_displayed()

        assert bun_text == 'Булки' and bun_displayed

    def test_switch_to_sauces_constr_success(self, driver):
        """Проверка перехода к разделу 'Соусы' в конструкторе"""
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_but).click()
        souces_text = driver.find_element(*MainPageLocators.sauces_txt).text
        souces_displayed = driver.find_element(*MainPageLocators.sauces_ul).is_displayed()

        assert souces_text == 'Соусы' and souces_displayed

    def test_switch_to_toppings_constr_success(self, driver):
        """Проверка перехода к разделу 'Начинки' в конструкторе"""
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.toppings_but).click()
        topping_text = driver.find_element(*MainPageLocators.topping_txt).text
        topping_displayed = driver.find_element(*MainPageLocators.topping_ul).is_displayed()

        assert topping_text == 'Начинки' and topping_displayed
