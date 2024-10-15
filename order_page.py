from base_page import BasePage
from OrderPageLocators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time


class OrderPage(BasePage):
    url = "https://demo.yookassa.ru/new_order "

    def open(self):
        super().open(self.url)

    # 0. Метод для автоматической проверки отображаемых товаров на странице заказа
    def verify_cart_items(self, remembered_items):
        # Локаторы всех товаров на странице заказа
        order_items_locators = {
            "Квадрат": OrderPageLocators.CART_ITEM_SQUARE,
            "Круг": OrderPageLocators.CART_ITEM_CIRCLE,
            "Равнобедренная трапеция": OrderPageLocators.CART_ITEM_TRAPEZOID,
            "Ромб": OrderPageLocators.CART_ITEM_RHOMBUS,
            "Треугольник": OrderPageLocators.CART_ITEM_TRIANGLE,
            "Шестиугольник": OrderPageLocators.CART_ITEM_HEXAGON,
            "Эллипс": OrderPageLocators.CART_ITEM_ELLIPSE
        }

        # Проходим по каждому элементу, который был запомнен в корзине
        for item in remembered_items:
            assert self.is_element_visible(
                order_items_locators[item]), f"Товар '{item}' не отображается на странице заказа."
        print("Все товары из корзины успешно отображены на странице заказа.")

    # 1. Заполнение поля "Контактный телефон" конкретным валидным значением
    def fill_contact_phone(self):
        self.wait_for_element_to_be_visible(OrderPageLocators.CONTACT_PHONE)
        self.hover_element(OrderPageLocators.CONTACT_PHONE)
        self.click_element(OrderPageLocators.CONTACT_PHONE)
        self.input_text(OrderPageLocators.CONTACT_PHONE, "+79549991122")
        print("Поле 'Контактный телефон' успешно заполнено значением '+79549991122'.")

    # 2.1. Ввод невалидного значения в поле "Населенный пункт" и проверка ошибки
    def fill_locality_invalid(self):
        try:
            # Вводим невалидное значение и проверяем, что ошибка отображается
            self.input_text_with_autocomplete(OrderPageLocators.LOCALITY, "Сетубал")

            self.click_element(OrderPageLocators.CLIENT_EMAIL)

            self.wait_for_element_to_be_visible(OrderPageLocators.LOCALITY_NOT_FOUND)
            error_visible = self.is_element_visible(OrderPageLocators.LOCALITY_NOT_FOUND)

            assert error_visible, "Ошибка 'Не удалось определить населенный пункт' не отображена."
            print("Ошибка 'Не удалось определить населенный пункт' успешно отображена.")

        except Exception as e:
            print(f"Ошибка при проверке поля 'Населенный пункт': {e}")
            self.take_screenshot("fill_locality_invalid_error")
            raise

    # 2.2. Ввод валидного значения в поле "Населенный пункт" и проверка отсутствия ошибки
    def fill_locality_valid(self):
        try:
            # Вводим валидное значение и проверяем, что ошибки нет
            self.input_text_with_autocomplete(OrderPageLocators.LOCALITY, "Полярные Зори")

            self.click_element(OrderPageLocators.CLIENT_EMAIL)

            assert self.is_element_not_visible(OrderPageLocators.LOCALITY_NOT_FOUND), \
                "Ошибка 'Не удалось определить населенный пункт' отображена, хотя не должна."
            print("Сообщение об ошибке 'Не удалось определить населенный пункт' не отображается.")

        except Exception as e:
            print(f"Ошибка при проверке поля 'Населенный пункт': {e}")
            self.take_screenshot("fill_locality_valid_error")
            raise

    # 3. Нажатие на радиобаттон "Курьером" и проверка появления поля "Адрес" и устранения радиобаттона "ЮKassa"
    def select_delivery_by_courier(self):
        self.click_element(OrderPageLocators.DELIVERY_OPTION)
        self.wait_for_element_to_be_visible(OrderPageLocators.DELIVERY_ADDRESS)

        assert self.is_element_visible(OrderPageLocators.DELIVERY_ADDRESS), "Поле 'Адрес' не отображено."
        print("Поле 'Адрес' успешно отображено.")

        assert self.is_element_not_visible(
            OrderPageLocators.PAYMENT_YOOKASSA), "Опция 'Перейти на страницу ЮKassa' всё ещё отображается."
        print("Опция 'Перейти на страницу ЮKassa' успешно скрыта.")

    # 4. Заполнение поля "Адрес" валидным значением
    def fill_delivery_address(self):
        self.wait_for_element_to_be_visible(OrderPageLocators.DELIVERY_ADDRESS)
        self.hover_element(OrderPageLocators.DELIVERY_ADDRESS)
        self.click_element(OrderPageLocators.DELIVERY_ADDRESS)
        self.input_text(OrderPageLocators.DELIVERY_ADDRESS, "ул. Ленина 22, кв. 5")
        print("Поле 'Адрес' успешно заполнено значением 'ул. Ленина 22, кв. 5'.")

    # 5. Заполнение поля "Комментарий" валидным значением
    def fill_order_comment(self):
        self.wait_for_element_to_be_visible(OrderPageLocators.ORDER_COMMENT)
        self.hover_element(OrderPageLocators.ORDER_COMMENT)
        self.click_element(OrderPageLocators.ORDER_COMMENT)
        self.input_text(OrderPageLocators.ORDER_COMMENT, "после 14:00")
        print("Поле 'Комментарий к заказу' успешно заполнено значением 'после 14:00'.")

    # 6. Заполнение поля "Контактное лицо (ФИО)" валидным значением
    def fill_client_name(self):
        self.wait_for_element_to_be_visible(OrderPageLocators.CLIENT_NAME)
        self.hover_element(OrderPageLocators.CLIENT_NAME)
        self.click_element(OrderPageLocators.CLIENT_NAME)
        self.input_text(OrderPageLocators.CLIENT_NAME, "Иванов Иван Иваныч")
        print("Поле 'Контактное лицо (ФИО)' успешно заполнено значением 'Иванов Иван Иваныч'.")

    # 7. Нажатие на радиобаттон "SberPay"
    def select_payment_sberpay(self):
        self.click_element(OrderPageLocators.PAYMENT_SBERPAY)
        print("Опция 'SberPay' успешно выбрана.")

    # 8. Нажатие на радиобаттон "Перейти на страницу ЮKassa"
    def select_payment_yookassa(self):
        self.click_element(OrderPageLocators.PAYMENT_YOOKASSA)
        print("Опция 'Перейти на страницу ЮKassa' успешно выбрана.")

    # 9. Нажатие кнопки "Подтвердить заказ"
    def submit_order(self):
        self.click_element(OrderPageLocators.SUBMIT_ORDER)
        print("Кнопка 'Подтвердить заказ' успешно нажата.")

    # 10. Проверка редиректа на страницу оплаты после нажатия кнопки "Подтвердить заказ"
    def check_redirect_to_payment(self, timeout=30):
        intermediate_url = "https://demo.yookassa.ru/orders/"
        payment_urls = ["https://demo.yookassa.ru/payments/",
                        "https://yoomoney.ru/checkout/payments/"]

        try:
            # Шаг 1: Проверка, что мы переходим на промежуточную страницу
            WebDriverWait(self.driver, timeout).until(
                lambda driver: intermediate_url in driver.current_url
            )
            print(f"Успешный редирект на промежуточную страницу: {self.driver.current_url}")

            time.sleep(10)

            WebDriverWait(self.driver, timeout).until(
                lambda driver: any(payment_url in driver.current_url for payment_url in payment_urls)
            )
            print(f"Успешный редирект на страницу оплаты: {self.driver.current_url}")

        except TimeoutException:
            current_url = self.driver.current_url

            # Проверяем наличие ошибок если редирект не произошел
            if intermediate_url not in current_url and not any(
                    payment_url in current_url for payment_url in payment_urls):
                print(f"Не удалось выполнить редирект. Текущий URL: {current_url}")

                # Проверка ошибки в поле "Населённый пункт"
                if self.is_element_visible(OrderPageLocators.ERROR_NOTIFICATION_LOCALITY):
                    error_message = self.get_element_text(OrderPageLocators.ERROR_NOTIFICATION_LOCALITY)
                    print(f"Ошибка в поле 'Населённый пункт': {error_message}")
                    self.take_screenshot("error_locality")
                    return False

                # Проверка ошибки в поле "Контактное лицо (ФИО)"
                elif self.is_element_visible(OrderPageLocators.ERROR_NOTIFICATION_FIO):
                    error_message = self.get_element_text(OrderPageLocators.ERROR_NOTIFICATION_FIO)
                    print(f"Ошибка в поле 'Контактное лицо (ФИО)': {error_message}")
                    self.take_screenshot("error_fio")
                    return False

            return True
    # def check_redirect_to_payment(self, timeout=30):
    #     intermediate_url = "https://demo.yookassa.ru/orders/"
    #     payment_url = "https://demo.yookassa.ru/payments/"
    #
    #     try:
    #         # Шаг 1: Проверка, что мы переходим на промежуточную страницу
    #         WebDriverWait(self.driver, timeout).until(
    #             lambda driver: intermediate_url in driver.current_url
    #         )
    #         print(f"Успешный редирект на промежуточную страницу: {self.driver.current_url}")
    #
    #         time.sleep(10)
    #
    #         # Шаг 2: Ждем редирект на страницу оплаты (payments)
    #         WebDriverWait(self.driver, timeout).until(
    #             lambda driver: payment_url in driver.current_url
    #         )
    #         print(f"Успешный редирект на страницу оплаты: {self.driver.current_url}")
    #
    #     except TimeoutException:
    #         current_url = self.driver.current_url
    #
    #         # Проверяем наличие ошибок если редирект не произошел
    #         if intermediate_url not in current_url and payment_url not in current_url:
    #             print(f"Не удалось выполнить редирект. Текущий URL: {current_url}")
    #
    #             # Проверка ошибки в поле "Населённый пункт"
    #             if self.is_element_visible(OrderPageLocators.ERROR_NOTIFICATION_LOCALITY):
    #                 error_message = self.get_element_text(OrderPageLocators.ERROR_NOTIFICATION_LOCALITY)
    #                 print(f"Ошибка в поле 'Населённый пункт': {error_message}")
    #                 self.take_screenshot("error_locality")  # Создание скриншота
    #                 return False
    #
    #             # Проверка ошибки в поле "Контактное лицо (ФИО)"
    #             elif self.is_element_visible(OrderPageLocators.ERROR_NOTIFICATION_FIO):
    #                 error_message = self.get_element_text(OrderPageLocators.ERROR_NOTIFICATION_FIO)
    #                 print(f"Ошибка в поле 'Контактное лицо (ФИО)': {error_message}")
    #                 self.take_screenshot("error_fio")  # Создание скриншота
    #                 return False
    #
    #         return True
