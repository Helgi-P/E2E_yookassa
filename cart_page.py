from base_page import BasePage
from CartPageLocators import CartPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CartPage(BasePage):
    url = "https://demo.yookassa.ru/cart_items"

    def open(self):
        super().open(self.url)

    # 1. Универсальный метод для добавления, увеличения, уменьшения или удаления товара
    def modify_product_quantity(self, action, product_type, quantity=1):
        product_locators = CartPageLocators.get_product_locators(product_type)  # Получаем локаторы для нужного товара

        if action == 'add':
            if not self.is_product_in_cart(product_locators['CART_ITEM']):
                print(f"Товар {product_type} не в корзине. Добавляем первый раз.")
                assert self.is_element_visible(product_locators['ADD_TO_CART_BUTTON']), "Кнопка добавления не видна."
                self.find_element(product_locators['ADD_TO_CART_BUTTON']).click()
                # Добавляем ожидание на обновление корзины
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(product_locators['CART_ITEM'])
                )
                if quantity > 1:
                    self.increase_quantity(product_locators['BUTTON_INCREASE_QUANTITY'], quantity - 1)
            else:
                print(f"Товар {product_type} уже в корзине. Увеличиваем на {quantity} раз.")
                self.increase_quantity(product_locators['BUTTON_INCREASE_QUANTITY'], quantity)

        elif action == 'increase':
            print(f"Увеличиваем количество товара {product_type} на {quantity}.")
            assert self.is_element_visible(product_locators['BUTTON_INCREASE_QUANTITY']), "Кнопка увеличения не видна."
            self.increase_quantity(product_locators['BUTTON_INCREASE_QUANTITY'], quantity)

        elif action == 'decrease':
            if not self.is_product_in_cart(product_locators['CART_ITEM']):
                print(f"Товар {product_type} не в корзине, уменьшать нечего.")
            else:
                print(f"Уменьшаем количество товара {product_type} на {quantity}.")
                assert self.is_element_visible(
                    product_locators['BUTTON_DECREASE_QUANTITY']), "Кнопка уменьшения не видна."
                self.decrease_quantity(product_locators['BUTTON_DECREASE_QUANTITY'], quantity)

        elif action == 'delete':
            if not self.is_product_in_cart(product_locators['CART_ITEM']):
                print(f"Товар {product_type} не в корзине, нечего удалять.")
            else:
                print(f"Удаляем товар {product_type} из корзины.")
                assert self.is_element_visible(product_locators['BUTTON_DELETE_ITEM']), "Кнопка удаления не видна."
                self.delete_product_from_cart(product_locators['BUTTON_DELETE_ITEM'])

    # Метод увеличения количества товара
    def increase_quantity(self, increase_button_locator, quantity):
        for _ in range(quantity):
            self.find_element(increase_button_locator).click()

    # Метод уменьшения количества товара
    def decrease_quantity(self, decrease_button_locator, quantity):
        for _ in range(quantity):
            self.find_element(decrease_button_locator).click()

    # Метод удаления товара из корзины
    def delete_product_from_cart(self, delete_button_locator):
        self.find_element(delete_button_locator).click()

    def is_product_in_cart(self, product_locator):
        try:
            # Явное ожидание элемента в корзине
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(product_locator)
            )
            return True
        except TimeoutException:
            print("Товар не найден в корзине.")
            return False

    # 5. Метод нажатия на кнопку "Оформить заказ" с запоминанием видов товаров
    def proceed_to_checkout(self):
        cart_items = self.remember_cart_items()
        self.scroll_to_element(CartPageLocators.CHECKOUT_BUTTON)
        assert self.is_element_visible(CartPageLocators.CHECKOUT_BUTTON), "Кнопка оформления заказа не видна."
        self.click_element(CartPageLocators.CHECKOUT_BUTTON)
        return cart_items

    # 5.1. Метод для запоминания товаров в корзине
    def remember_cart_items(self):
        cart_items = []

        if self.is_element_present_without_exception(CartPageLocators.SQUARE_CART_ITEM):
            cart_items.append("Квадрат")
        if self.is_element_present_without_exception(CartPageLocators.CIRCLE_CART_ITEM):
            cart_items.append("Круг")
        if self.is_element_present_without_exception(CartPageLocators.TRAPEZOID_CART_ITEM):
            cart_items.append("Равнобедренная трапеция")
        if self.is_element_present_without_exception(CartPageLocators.RHOMBUS_CART_ITEM):
            cart_items.append("Ромб")
        if self.is_element_present_without_exception(CartPageLocators.TRIANGLE_CART_ITEM):
            cart_items.append("Треугольник")
        if self.is_element_present_without_exception(CartPageLocators.HEXAGON_CART_ITEM):
            cart_items.append("Шестиугольник")
        if self.is_element_present_without_exception(CartPageLocators.ELLIPSE_CART_ITEM):
            cart_items.append("Эллипс")

        return cart_items

    # 2. Метод перехода на страницу конкретного товара
    def go_to_product_page(self, product_preview_locator):
        assert self.is_element_visible(product_preview_locator), "Превью товара не видно."
        self.find_element(product_preview_locator).click()

    # 3. Метод применения промокода и проверка ошибки
    def apply_promo_code(self, promo_code):
        promo_code_input = self.find_element(CartPageLocators.PROMO_CODE_INPUT)
        promo_code_input.clear()
        promo_code_input.send_keys(promo_code)

        self.find_element(CartPageLocators.PROMO_CODE_SUBMIT_BUTTON).click()

        try:
            error_message_element = self.find_element(CartPageLocators.PROMO_CODE_ERROR_MESSAGE)
            error_message = error_message_element.text

            self.take_screenshot()
            print(f"Ошибка при применении промокода: {error_message}")
            return error_message

        except NoSuchElementException:

            return None

    # 3. Метод перехода обратно в каталог
    def go_back_to_catalog(self):
        assert self.is_element_visible(CartPageLocators.BACK_TO_CATALOG_BUTTON), "Кнопка возврата в каталог не видна."
        self.find_element(CartPageLocators.BACK_TO_CATALOG_BUTTON).click()
