from base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPageLocators:
    # Локаторы для элементов страницы товара
    BUTTON_ADD_TO_CART = (By.XPATH, '//*[@id="product-detail-buy-area"]/div[1]/div/button')  # Кнопка "В корзину"
    BUTTON_DECREASE_QUANTITY = (By.XPATH, '//*[@id="product-detail-buy-area"]/div[1]/div/div/button[1]')  # Кнопка "-"
    BUTTON_INCREASE_QUANTITY = (By.XPATH, '//*[@id="product-detail-buy-area"]/div[1]/div/div/button[2]')  # Кнопка "+"
    BUTTON_CART_DETAIL = (
        By.XPATH, '//*[@id="product-detail-buy-area"]/div[1]/div/div/a')  # Кнопка "В корзине х шт. Перейти"


class ProductPage(BasePage):
    def open(self, product_type):
        # Формируем URL на основе типа продукта
        url_mapping = {
            "square": "https://demo.yookassa.ru/product/kvadrat",
            "circle": "https://demo.yookassa.ru/product/krug",
            "trapezoid": "https://demo.yookassa.ru/product/ravnobedrennaya-trapetsiya",
            "rhombus": "https://demo.yookassa.ru/product/romb",
            "triangle": "https://demo.yookassa.ru/product/treugolnik",
            "hexagon": "https://demo.yookassa.ru/product/shestiugolnik",
            "ellipse": "https://demo.yookassa.ru/product/ellips"
        }
        self.url = url_mapping.get(product_type)  # Получаем URL для конкретного типа продукта
        assert self.url, "Неверный тип продукта"
        super().open(self.url)  # Открываем страницу по сгенерированному URL

    # Проверяет, добавлен ли товар в корзину на основе видимости кнопки "В корзину".
    # Параметр times: Сколько раз нужно увеличить количество товара.
    def is_item_in_cart(self):
        # Если кнопка "В корзину" НЕ видна, значит товар уже в корзине
        return not self.is_element_visible(ProductPageLocators.BUTTON_ADD_TO_CART)

    # Метод увеличения количества товара на странице продукта
    def increase_item_quantity(self, times):

        if not self.is_item_in_cart():
            self.click_element(ProductPageLocators.BUTTON_ADD_TO_CART)
            print(f"Товар не был в корзине. Добавляем товар и увеличиваем количество на {times}.")
            for _ in range(times - 1):
                self.click_element(ProductPageLocators.BUTTON_INCREASE_QUANTITY)
        else:
            # Если товар уже в корзине, просто увеличиваем количество
            print(f"Товар уже в корзине. Увеличиваем количество на {times}.")
            for _ in range(times):
                self.click_element(ProductPageLocators.BUTTON_INCREASE_QUANTITY)

    # Метод уменьшения количества товара на странице продукта.
    # Параметр times: Сколько раз нужно уменьшить количество товара.
    def decrease_item_quantity(self, times):

        if not self.is_item_in_cart():
            print(f"Товар не в корзине, нечего уменьшать.")
        else:
            print(f"Товар в корзине. Уменьшаем количество на {times}.")
            for _ in range(times):
                self.click_element(ProductPageLocators.BUTTON_DECREASE_QUANTITY)

    # Переход в корзину кнопкой "В корзине х шт. Перейти"
    def go_to_cart(self):
        self.click_element(ProductPageLocators.BUTTON_CART_DETAIL)
