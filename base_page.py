import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys


class BasePageLocators:
    # Локаторы элементов хедера
    LOGO_UKASSA = (By.XPATH, '//span[@class="header__logo"]/img')
    ICON_MAGNIFIER = (
        By.XPATH, '//button[contains(@class, "header__search-btn") and contains(@class, "js-show-search")]')
    INPUT_SEARCH = (By.XPATH, '//input[@type="search"]')
    BUTTON_X_SEARCH = (
        By.XPATH, '//button[contains(@class, "header__search-btn") and contains(@class, "js-show-search")]')
    ICON_CART = (By.XPATH, '//a[@href="/cart_items"]')


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Сохранение скриншота
    def take_screenshot(self, name="screenshot"):
        # Папка для скриншотов
        screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots")

        # Проверяем, существует ли папка, если нет — создаем её
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        # Формируем имя файла скриншота
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = f"{timestamp}.png"
        screenshot_path = os.path.join(screenshot_dir, screenshot_name)

        # Сохраняем скриншот
        self.driver.save_screenshot(screenshot_path)
        print(f"Скриншот сохранён: {screenshot_path}")

    # 1. Открыть страницу
    def open(self, url):
        print(f"Открытие страницы: {url}")
        self.driver.get(url)

    # 2.1. Поиск элемента, который важен и должен быть
    def find_element(self, locator, timeout=20):
        try:
            print(f"Поиск элемента: {locator}")
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            print(f"Элемент найден: {locator}")
            return element
        except TimeoutException:
            print(f"Элемент не найден в течение {timeout} секунд: {locator}")
            self.take_screenshot(f"element_not_found_{locator}")
            raise

    # 2.2. Поиск элемента, значение которого неважно
    def is_element_present_without_exception(self, locator, timeout=10):

        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    # 3. Наведение на элемент
    def hover_element(self, locator):
        try:
            print(f"Наведение на элемент: {locator}")
            element = self.find_element(locator)
            ActionChains(self.driver).move_to_element(element).perform()
            print(f"Наведение выполнено на элемент: {locator}")
        except Exception as e:
            print(f"Не удалось навести на элемент: {locator}. Ошибка: {e}")
            self.take_screenshot(f"hover_failed_{locator}")
            raise

    # 4. Клик на элемент
    def click_element(self, locator, timeout=25):
        try:
            print(f"Клик на элемент: {locator}")
            element = self.find_element(locator, timeout)
            element.click()
            print(f"Клик выполнен на элемент: {locator}")
        except Exception as e:
            print(f"Не удалось кликнуть на элемент: {locator}. Ошибка: {e}")
            self.take_screenshot(f"click_failed_{locator}")
            raise

    # 6. Ввод текста в поле
    def input_text(self, locator, text, timeout=10):
        try:
            print(f"Ввод текста '{text}' в элемент: {locator}")
            element = self.find_element(locator, timeout)
            element.clear()
            time.sleep(2)

            # Проверяем, что поле пустое перед вводом
            assert element.get_attribute('value') == '', "Поле не очищено до конца"
            print(f"Поле '{locator}' очищено.")

            element.send_keys(text)
            print(f"Текст '{text}' введён в элемент: {locator}")
        except Exception as e:
            print(f"Не удалось ввести текст '{text}' в элемент: {locator}. Ошибка: {e}")
            self.take_screenshot(f"input_failed_{locator}")
            raise

    # 7. Ввод теста в поле с автозаполнением
    def input_text_with_autocomplete(self, locator, text, timeout=10):
        try:
            print(f"Ввод текста '{text}' в элемент: {locator}")
            element = self.find_element(locator, timeout)

            # Очистка поля через выделение всего текста и удаление
            element.click()
            element.send_keys(Keys.CONTROL, 'a')  # Выделить весь текст
            element.send_keys(Keys.BACKSPACE)  # Удалить выделенное
            time.sleep(5)

            assert element.get_attribute('value') == '', "Поле не очищено до конца"
            print(f"Поле '{locator}' очищено.")

            element.send_keys(text)
            time.sleep(5)

            # Для подтверждения автозаполнения — нажимаем клавишу Enter
            element.send_keys(Keys.RETURN)

            print(f"Текст '{text}' введён и подтверждён через автозаполнение.")
        except Exception as e:
            print(f"Не удалось ввести текст '{text}' в элемент: {locator}. Ошибка: {e}")
            self.take_screenshot(f"input_failed_{locator}")
            raise

    # 8. Ожидание появления элемента
    def wait_for_element_to_be_visible(self, locator, timeout=20):
        try:
            print(f"Ожидание видимости элемента: {locator}")
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            print(f"Элемент видим: {locator}")
        except TimeoutException:
            print(f"Элемент не появился в течение {timeout} секунд: {locator}")
            self.take_screenshot(f"element_not_visible_{locator}")
            raise

    # 9. Проверка присутствия элемента
    def is_element_present(self, locator, timeout=10):
        try:
            print(f"Проверка наличия элемента: {locator}")
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            print(f"Элемент присутствует: {locator}")
            return True
        except TimeoutException:
            print(f"Элемент не найден в течение {timeout} секунд: {locator}")
            self.take_screenshot(f"element_not_present_{locator}")
            return False

    # 10. Проверка видимости элемента
    def is_element_visible(self, locator, timeout=10):
        try:
            print(f"Проверка видимости элемента: {locator}")
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            print(f"Элемент виден: {locator}")
            return True
        except TimeoutException:
            print(f"Элемент не виден в течение {timeout} секунд: {locator}")
            self.take_screenshot(f"element_not_visible_{locator}")
            return False

    # 11. Проверка, что элемент невидим
    def is_element_not_visible(self, locator, timeout=10):
        try:
            print(f"Проверка отсутствия видимости элемента: {locator}")
            WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(locator))
            print(f"Элемент невиден: {locator}")
            return True
        except TimeoutException:
            print(f"Элемент продолжает отображаться: {locator}")
            self.take_screenshot(f"element_still_visible_{locator}")
            return False

    # 12. Открытие корзины через иконку
    def open_cart_with_icon(self):
        print(f"Открытие корзины через иконку")
        self.click_element(BasePageLocators.ICON_CART)

    # 13. Проверка видимости хэдера
    def assert_header_elements(self):
        print(f"Проверка видимости элементов хедера")
        assert self.is_element_visible(BasePageLocators.ICON_MAGNIFIER), "Иконка лупы не видна"
        assert self.is_element_visible(BasePageLocators.ICON_CART), "Иконка корзины не видна"

    # 14. Прокрутка до элемента
    def scroll_to_element(self, locator):
        try:
            print(f"Прокрутка до элемента: {locator}")
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            print(f"Прокрутка выполнена до элемента: {locator}")
        except Exception as e:
            print(f"Не удалось прокрутить до элемента: {locator}. Ошибка: {e}")
            self.take_screenshot(f"scroll_failed_{locator}")
            raise

    # 15. Получить элемент текста
    def get_element_text(self, locator, timeout=10):
        try:
            element = self.find_element(locator, timeout)
            text = element.text
            print(f"Текст элемента '{locator}': {text}")
            return text
        except Exception as e:
            print(f"Не удалось получить текст элемента: {locator}. Ошибка: {e}")
            self.take_screenshot(f"get_text_failed_{locator}")
            raise


    # Неиспользуемые методы. Жалко удалять)))
    # 3. Поиск нескольких элементов
    # def find_elements(self, locator, timeout=10):
    #     try:
    #         print(f"Поиск элементов: {locator}")
    #         elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    #         print(f"Найдено элементов: {len(elements)} для {locator}")
    #         return elements
    #     except TimeoutException:
    #         print(f"Элементы не найдены в течение {timeout} секунд: {locator}")
    #         self.take_screenshot(f"elements_not_found_{locator}")
    #         raise


    # # 11. Проверка URL
    # def assert_url_contains(self, expected_url_part):
    #     print(f"Проверка, что URL содержит: {expected_url_part}")
    #     current_url = self.driver.current_url
    #     assert expected_url_part in current_url, f"Ожидалось, что URL будет содержать '{expected_url_part}', но текущий: '{current_url}'"
    #     print(f"Проверка URL успешна: текущий URL содержит {expected_url_part}")

    # # 12. Проверка текста элемента
    # def assert_text(self, locator, expected_text, timeout=10):
    #     print(f"Проверка текста элемента: {locator}")
    #     element = self.find_element(locator, timeout)
    #     actual_text = element.text
    #     assert expected_text in actual_text, f"Ожидалось '{expected_text}', но получено '{actual_text}'"
    #     print(f"Текст соответствует ожиданиям: {expected_text}")

    #
    # # 14. Поиск продукта через иконку лупы
    # def search_product_with_icon(self, product_name):
    #     print(f"Поиск продукта '{product_name}' через иконку лупы")
    #     self.input_text(BasePageLocators.INPUT_SEARCH, product_name)
    #     self.click_element(BasePageLocators.ICON_MAGNIFIER)

    #
    # # 17. Ожидание кликабельности
    # def wait_for_element_to_be_clickable(self, locator, timeout=15):
    #     try:
    #         print(f"Ожидание кликабельности элемента: {locator}")
    #         WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    #         print(f"Элемент кликабелен: {locator}")
    #     except TimeoutException:
    #         print(f"Элемент не стал кликабельным в течение {timeout} секунд: {locator}")
    #         self.take_screenshot(f"element_not_clickable_{locator}")
    #         raise