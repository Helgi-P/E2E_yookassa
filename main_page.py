from base_page import BasePage
from MainPageLocators import MainPageLocators
from product_page import ProductPage


class MainPage(BasePage):
    url = "https://demo.yookassa.ru/"

    def open(self):
        super().open(self.url)

    # Методы для добавления товаров в корзину
    def add_square_to_cart(self):
        print("Добавление квадрата в корзину")
        assert self.is_element_visible(MainPageLocators.PRODUCT_PREVIEW_SQUARE), "Картинка квадрата не видна"
        self.hover_element(MainPageLocators.PRODUCT_PREVIEW_SQUARE)
        assert self.is_element_visible(
            MainPageLocators.BUTTON_ADD_IN_CART_SQUARE), "Кнопка 'Добавить в корзину' для квадрата не видна"
        self.click_element(MainPageLocators.BUTTON_ADD_IN_CART_SQUARE)

    def add_circle_to_cart(self):
        print("Добавление круга в корзину")
        assert self.is_element_visible(MainPageLocators.PRODUCT_PREVIEW_CIRCLE), "Картинка круга не видна"
        self.hover_element(MainPageLocators.PRODUCT_PREVIEW_CIRCLE)
        assert self.is_element_visible(
            MainPageLocators.BUTTON_ADD_IN_CART_CIRCLE), "Кнопка 'Добавить в корзину' для круга не видна"
        self.click_element(MainPageLocators.BUTTON_ADD_IN_CART_CIRCLE)

    def add_trapezoid_to_cart(self):
        print("Добавление трапеции в корзину")
        assert self.is_element_visible(MainPageLocators.PRODUCT_PREVIEW_TRAPEZOID), "Картинка трапеции не видна"
        self.hover_element(MainPageLocators.PRODUCT_PREVIEW_TRAPEZOID)
        assert self.is_element_visible(
            MainPageLocators.BUTTON_ADD_IN_CART_TRAPEZOID), "Кнопка 'Добавить в корзину' для трапеции не видна"
        self.click_element(MainPageLocators.BUTTON_ADD_IN_CART_TRAPEZOID)

    def add_rhombus_to_cart(self):
        print("Добавление ромба в корзину")
        assert self.is_element_visible(MainPageLocators.PRODUCT_PREVIEW_RHOMBUS), "Картинка ромба не видна"
        self.hover_element(MainPageLocators.PRODUCT_PREVIEW_RHOMBUS)
        assert self.is_element_visible(
            MainPageLocators.BUTTON_ADD_IN_CART_RHOMBUS), "Кнопка 'Добавить в корзину' для ромба не видна"
        self.click_element(MainPageLocators.BUTTON_ADD_IN_CART_RHOMBUS)

    def add_triangle_to_cart(self):
        print("Добавление треугольника в корзину")
        assert self.is_element_visible(MainPageLocators.PRODUCT_PREVIEW_TRIANGLE), "Картинка треугольника не видна"
        self.hover_element(MainPageLocators.PRODUCT_PREVIEW_TRIANGLE)
        assert self.is_element_visible(
            MainPageLocators.BUTTON_ADD_IN_CART_TRIANGLE), "Кнопка 'Добавить в корзину' для треугольника не видна"
        self.click_element(MainPageLocators.BUTTON_ADD_IN_CART_TRIANGLE)

    def add_hexagon_to_cart(self):
        print("Добавление шестиугольника в корзину")
        assert self.is_element_visible(MainPageLocators.PRODUCT_PREVIEW_HEXAGON), "Картинка шестиугольника не видна"
        self.hover_element(MainPageLocators.PRODUCT_PREVIEW_HEXAGON)
        assert self.is_element_visible(
            MainPageLocators.BUTTON_ADD_IN_CART_HEXAGON), "Кнопка 'Добавить в корзину' для шестиугольника не видна"
        self.click_element(MainPageLocators.BUTTON_ADD_IN_CART_HEXAGON)

    def add_ellipse_to_cart(self):
        print("Добавление эллипса в корзину")
        assert self.is_element_visible(MainPageLocators.PRODUCT_PREVIEW_ELLIPSE), "Картинка эллипса не видна"
        self.hover_element(MainPageLocators.PRODUCT_PREVIEW_ELLIPSE)
        assert self.is_element_visible(
            MainPageLocators.BUTTON_ADD_IN_CART_ELLIPSE), "Кнопка 'Добавить в корзину' для эллипса не видна"
        self.click_element(MainPageLocators.BUTTON_ADD_IN_CART_ELLIPSE)

    def add_all_products_to_cart(self):
        self.add_square_to_cart()
        self.add_circle_to_cart()
        self.add_trapezoid_to_cart()
        self.add_rhombus_to_cart()
        self.add_triangle_to_cart()
        self.add_hexagon_to_cart()
        self.add_ellipse_to_cart()

    # Методы для перехода на страницы товаров
    def go_to_square_page(self):
        print("Переход на страницу квадрата")
        assert self.is_element_visible(
            MainPageLocators.LINK_TO_PRODUCT_PAGE_SQUARE), "Ссылка на страницу квадрата не видна"
        product_page = ProductPage(self.driver)
        product_page.open("square")

    def go_to_circle_page(self):
        print("Переход на страницу круга")
        assert self.is_element_visible(
            MainPageLocators.LINK_TO_PRODUCT_PAGE_CIRCLE), "Ссылка на страницу круга не видна"
        product_page = ProductPage(self.driver)
        product_page.open("circle")

    def go_to_trapezoid_page(self):
        print("Переход на страницу трапеции")
        assert self.is_element_visible(
            MainPageLocators.LINK_TO_PRODUCT_PAGE_TRAPEZOID), "Ссылка на страницу трапеции не видна"
        product_page = ProductPage(self.driver)
        product_page.open("trapezoid")

    def go_to_rhombus_page(self):
        print("Переход на страницу ромба")
        assert self.is_element_visible(
            MainPageLocators.LINK_TO_PRODUCT_PAGE_RHOMBUS), "Ссылка на страницу ромба не видна"
        product_page = ProductPage(self.driver)
        product_page.open("rhombus")

    def go_to_triangle_page(self):
        print("Переход на страницу треугольника")
        assert self.is_element_visible(
            MainPageLocators.LINK_TO_PRODUCT_PAGE_TRIANGLE), "Ссылка на страницу треугольника не видна"
        product_page = ProductPage(self.driver)
        product_page.open("triangle")

    def go_to_hexagon_page(self):
        print("Переход на страницу шестиугольника")
        assert self.is_element_visible(
            MainPageLocators.LINK_TO_PRODUCT_PAGE_HEXAGON), "Ссылка на страницу шестиугольника не видна"
        product_page = ProductPage(self.driver)
        product_page.open("hexagon")

    def go_to_ellipse_page(self):
        print("Переход на страницу эллипса")
        assert self.is_element_visible(
            MainPageLocators.LINK_TO_PRODUCT_PAGE_ELLIPSE), "Ссылка на страницу эллипса не видна"
        product_page = ProductPage(self.driver)
        product_page.open("ellipse")
