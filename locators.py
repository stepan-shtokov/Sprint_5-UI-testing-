from selenium.webdriver.common.by import By


class MainPageLocators:
    """Основная страница"""
    personal_account_but = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка "Личный Кабинет"
    login_account_but = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # Кнопка "Войти в аккаунт" формы главной страницы
    place_order_but = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка "Оформить заказ" корзины
    sauces_by_span = (By.XPATH, ".//span[contains(text(),'Соусы')]")  # Список "Соусы" конструктора
    bun_by_span = (By.XPATH, ".//span[contains(text(),'Булки')]")  # Список "Булки" конструктора
    topping_by_span = (By.XPATH, ".//span[contains(text(),'Начинки')]")  # Список "Начинки" конструктора
    active_tab_in_constructor = (By.XPATH, ".//div[contains(@class, 'current')]/span")  # Проверка активной вкладки конструктора


class AuthPageLocators:
    """Форма авторизации/восстановления данных"""
    email_input = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода Email формы авторизации
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля формы авторизации
    login_account_auth_form_but = (By.XPATH, "//button[text() = 'Войти']")  # Кнопка "Войти" формы авторизации


class RegistrationPageLocators:
    """Форма регистрации/логина"""
    name_input = (By.XPATH, ".//label[text() = 'Имя']/following-sibling::input")  # Поле ввода имени пользователя
    email_input = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")  # Поле ввода E-mail пользователя
    password_input = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")  # Поле ввода пароля пользователя
    registration_but = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    login_account_but = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка "Войти"
    error_message_double_register = (By.XPATH, ".//p[text() = 'Такой пользователь уже существует']")  # Ошибка при повторной регистрации с теми же данными
    error_message_incorrect_pass = (By.XPATH, ".//p[text() = 'Некорректный пароль']")  # Ошибка при вводе некорректного пароля


class RecoverPageLocators:
    """Форма восстановления пароля"""
    login_account_but = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка "Войти"


class PersonalAreaLocators:
    """Форма ЛК"""
    exit_but = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка "Выход"
    save_but = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка "Сохранить"
    constructor_but = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка "Конструктор" хедера
    logo_but = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Кнопка главной страницы сайта
