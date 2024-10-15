import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from main_page import MainPage
from cart_page import CartPage
from order_page import OrderPage


@pytest.fixture(scope="session")
def driver():
    # Настройки для запуска браузера Chrome
    chrome_options = Options()

    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(30)
    yield driver

    # Закрытие браузера после завершения тестов
    driver.quit()


# Фикстура для открытия главной страницы
@pytest.fixture(scope="function")
def open_main_page(driver):
    main_page = MainPage(driver)
    main_page.open()
    return main_page


# Фикстура для открытия страницы корзины
@pytest.fixture(scope="function")
def cart_page(driver):
    cart_page = CartPage(driver)
    cart_page.open()
    return cart_page


# Фикстура для открытия страницы оформления заказа
@pytest.fixture(scope="function")
def order_page(driver):
    order_page = OrderPage(driver)
    order_page.open()
    return order_page


# Фикстура для создания скриншотов при ошибках
@pytest.fixture(scope="function")
def take_screenshot_on_failure(request, driver):
    yield
    if request.node.rep_call.failed:
        # Создание скриншота при ошибке
        screenshot_name = request.node.name + ".png"
        driver.save_screenshot(screenshot_name)
        print(f"Скриншот сохранен: {screenshot_name}")


# Хук для понимания, когда тест завершился с ошибкой
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from main_page import MainPage
# from cart_page import CartPage
# from order_page import OrderPage
#
#
# @pytest.fixture(scope="session")
# def driver():
#     # Настройки для запуска браузера Chrome
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument("--disable-notifications")
#     chrome_options.add_argument("--disable-infobars")  # Отключаем инфо-панели
#     chrome_options.add_argument("--disable-extensions")  # Отключаем расширения
#
#
#     # Установка драйвера через webdriver_manager
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#     driver.implicitly_wait(10)
#     yield driver
#
#     # Закрытие браузера после завершения тестов
#     driver.quit()
#
# # Фикстура для открытия главной страницы
# @pytest.fixture(scope="function")
# def open_main_page(driver):
#     main_page = MainPage(driver)
#     main_page.open()
#     return main_page
#
#
# # Фикстура для открытия страницы корзины
# @pytest.fixture(scope="function")
# def cart_page(driver):
#     cart_page = CartPage(driver)
#     cart_page.open()
#     return cart_page
#
#
# # Фикстура для открытия страницы оформления заказа
# @pytest.fixture(scope="function")
# def order_page(driver):
#     order_page = OrderPage(driver)
#     order_page.open()
#     return order_page
#
#
# # Фикстура для создания скриншотов при ошибках
# @pytest.fixture(scope="function")
# def take_screenshot_on_failure(request, driver):
#     yield
#     if request.node.rep_call.failed:
#         # Создание скриншота при ошибке
#         screenshot_name = request.node.name + ".png"
#         driver.save_screenshot(screenshot_name)
#         print(f"Скриншот сохранен: {screenshot_name}")
#
#
# # Хук для понимания, когда тест завершился с ошибкой
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)


# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from base_page import BasePage
#
# @pytest.fixture(scope="session")
# def driver():
#     # Настройки для запуска браузера Chrome
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")  # Открываем окно браузера в максимальном размере
#     chrome_options.add_argument("--disable-notifications")  # Отключаем уведомления
#     chrome_options.add_argument("--disable-infobars")
#     chrome_options.add_argument("--disable-extensions")
#
#     # Установка драйвера через webdriver_manager
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#     driver.implicitly_wait(10)  # Устанавливаем неявное ожидание в 10 секунд
#     yield driver
#     driver.quit()
#
# @pytest.fixture(scope="function")
# def open_main_page(driver):
#     # Фикстура для открытия главной страницы
#     base_page = BasePage(driver)
#     base_page.open("https://demo.yookassa.ru/")
#
# @pytest.fixture(scope="function")
# def cart_page(driver):
#     # Фикстура для открытия Страницы корзины
#     base_page = BasePage(driver)
#     base_page.open("https://demo.yookassa.ru/cart_items")
#
# @pytest.fixture(scope="function")
# def order_page(driver):
#     # Фикстура для открытия Страницы заказа
#     base_page = BasePage(driver)
#     base_page.open("https://demo.yookassa.ru/new_order")
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item):
#     # Этот хук помогает понять, когда тест завершился с ошибкой, для фикстуры скриншотов
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#
# @pytest.fixture(scope="function")
# def take_screenshot_on_failure(request, driver):
#     # Фикстура для создания скриншотов при ошибках
#     base_page = BasePage(driver)
#     yield
#     if request.node.rep_call.failed:
#         base_page.take_screenshot(name=request.node.name)
#
#
#
# # import pytest
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from webdriver_manager.chrome import ChromeDriverManager
# # from selenium.webdriver.common.by import By
# # from base_page import BasePage
# #
# #
# # @pytest.fixture(scope="session")
# # def driver():
# #     # Настройки для запуска браузера Chrome
# #     chrome_options = Options()
# #     chrome_options.add_argument("--start-maximized")  # Открываем окно браузера в максимальном размере
# #     chrome_options.add_argument("--disable-notifications")  # Отключаем уведомления
# #     chrome_options.add_argument("--disable-infobars")
# #     chrome_options.add_argument("--disable-extensions")
# #
# #     # Установка драйвера через webdriver_manager
# #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# #     driver.implicitly_wait(10)  # Устанавливаем неявное ожидание в 10 секунд
# #     yield driver
# #     driver.quit()
# #
# # #ДУБЛЬ?
# # @pytest.fixture(scope="function")
# # def open_main_page(driver):
# #     # Фикстура для открытия главной страницы
# #     url = "https://demo.yookassa.ru/"
# #     print(f"Открытие главной страницы: {url}")
# #     driver.get(url)
# #
# # @pytest.fixture(scope="function")
# # def cart_page(driver):
# #     # Фикстура для открытия Страницы корзины
# #     url = "https://demo.yookassa.ru/cart_items"
# #     print(f"Открытие Старницы корзины: {url}")
# #     driver.get(url)
# #
# #
# # @pytest.fixture(scope="function")
# # def order_page(driver):
# #     # Фикстура для открытия Страницы заказа
# #     url = "https://demo.yookassa.ru/new_order"
# #     print(f"Открытие Старницы заказа: {url}")
# #     driver.get(url)
# # #
# # #
# # # @pytest.fixture(scope="function")
# # # def take_screenshot_on_failure(request, driver):
# # #     # Фикстура для создания скриншотов при ошибках
# # #     # ЦЕЛИКОМ СЮДА???
# # #     yield
# # #     if request.node.rep_call.failed:
# # #         # Используем метод take_screenshot() из BasePage для создания скриншота
# # #         base_page = BasePage(driver)
# # #         base_page.take_screenshot(name=request.node.name)
# #
# #
# # @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# # def pytest_runtest_makereport(item):
# #     # Этот хук помогает понять, когда тест завершился с ошибкой, для фикстуры скриншотов
# #     outcome = yield
# #     rep = outcome.get_result()
# #     setattr(item, "rep_" + rep.when, rep)
# #
# #
# # ##ДУБЛЬ с base
# # # @pytest.fixture(scope="function")
# # # def add_to_cart(driver):
# # #     # Фикстура для добавления товара в корзину
# # #     def _add_product_to_cart(product_locator):
# # #         print(f"Добавление товара в корзину: {product_locator}")
# # #         driver.find_element(By.XPATH, product_locator).click()
# # #
# # #     return _add_product_to_cart
# #
# # # #ДУБЛЬ с base
# # # @pytest.fixture(scope="function")
# # # def fill_order_form(driver):
# # #     # Фикстура для заполнения формы заказа
# # #     def _fill_form(data):
# # #         print(f"Заполнение формы заказа данными: {data}")
# # #         for field_locator, value in data.items():
# # #             driver.find_element(By.XPATH, field_locator).send_keys(value)
# # #
# # #     return _fill_form
