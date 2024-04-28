from selenium.webdriver.common.by import By


class MainPageLocators:
    """Основная страница"""
    main_form = (By.XPATH, ".//main[@class = 'App_componentContainer__2JC2W']")  # Форма главной страницы SB
    logo_but = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Лого-кнопка главной страницы SB
    personal_account_but = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка "Личный Кабинет"
    login_account_but = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # Кнопка "Войти в аккаунт" формы главной страницы
    constructor_but = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка "Конструктор" хедера главной страницы
    order_feed_but = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка "Лента Заказов" хедера главной страницы
    place_order_but = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка "Оформить заказ" корзины
    sauces_by_span = ".//span[contains(text(),'Соусы')]"  # Список "Соусы" конструктора
    bun_by_span = ".//span[contains(text(),'Булки')]"  # Список "Булки" конструктора
    topping_by_span = ".//span[contains(text(),'Начинки')]"  # Список "Начинки" конструктора
    active_tab_in_constructor = ".//div[contains(@class, 'current')]/span"  # Проверка активной вкладки конструктора


class AuthPageLocators:
    """Форма авторизации/восстановления данных"""
    auth_form = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")  # Форма авторизации
    email_input = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода Email формы авторизации
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля формы авторизации
    login_account_but = (By.XPATH, "//button[text() = 'Войти']")  # Кнопка "Войти" формы авторизации
    registration_but = (By.XPATH, "//a[text() = 'Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    recover_but = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # Кнопка "Восстановить пароль"
    constructor_but = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка "Конструктор" хедера
    order_feed_but = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка "Лента заказов" хедера
    logo_but = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Лого-кнопка главной страницы SB
    personal_account_but = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка "Личный кабинет" хедера


class RegistrationPageLocators:
    """Форма регистрации/логина"""
    name_input = (By.XPATH, ".//label[text() = 'Имя']/following-sibling::input")  # Поле ввода имени пользователя
    email_input = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")  # Поле ввода E-mail пользователя
    password_input = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")  # Поле ввода пароля пользователя
    registration_but = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # Кнопка "Зарегистрироваться
    login_account_but = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка "Войти"
    constructor_but = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка "Конструктор" хедера
    order_feed_but = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка "Лента заказов" хедера
    logo_but = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Лого-кнопка главной страницы SB
    personal_account_but = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка "Личный кабинет" хедера
    error_message_double_register = (By.XPATH, ".//p[text() = 'Такой пользователь уже существует']")  # Ошибка при повторной регистрации с теми же данными
    error_message_incorrect_pass = (By.XPATH, ".//p[text() = 'Некорректный пароль']")  # Ошибка при вводе некорректного пароля


class RecoverPageLocators:
    """Форма восстановления пароля"""
    email_input = (By.XPATH, ".//label[text() = 'Email']")  # Поле ввода E-mail
    recover_but = (By.XPATH, ".//button[text() = 'Восстановить']")  # Кнопка "Восстановить"
    login_account_but = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка "Войти"
    constructor_but = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка "Конструктор" хедера
    order_feed_but = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка "Лента заказов" хедера
    logo_but = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Лого-кнопка главной страницы SB
    personal_account_but = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка личного кабинета


class PersonalAreaLocators:
    """Форма ЛК"""
    profile_form = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")  # Форма ЛК
    profile_but = By.XPATH, './/a[text()="Профиль"]'  # Кнопка "Профиль" ЛК
    order_history_but = (By.XPATH, ".//a[text() = 'История заказов']")  # Кнопка "История заказов"
    exit_but = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка "Выход"
    save_but = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка "Сохранить"
    cansel_but = (By.XPATH, ".//button[text() = 'Отмена']")  # Кнопка "Отмена"
    constructor_but = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка "Конструктор" хедера
    order_feed_but = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка "Лента заказов" хедера
    logo_but = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Кнопка главной страницы сайта
    personal_account_but = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка "Личный кабинет" хедера
