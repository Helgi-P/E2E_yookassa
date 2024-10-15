from selenium.webdriver.common.by import By


class CartPageLocators:
    # Кнопка "Назад в каталог"
    BACK_TO_CATALOG_BUTTON = (By.XPATH, '/html/body/div[2]/main/div[1]/div/a')

    # Промокоды и кнопки оформления заказа
    PROMO_CODE_INPUT = (By.XPATH, '/html/body/div[2]/main/div[2]/div/form/div[2]/div/div[1]/div[3]/input')
    PROMO_CODE_SUBMIT_BUTTON = (By.XPATH, '/html/body/div[2]/main/div[2]/div/form/div[2]/div/div[1]/div[3]/button')
    PROMO_CODE_ERROR_MESSAGE = (By.XPATH, '//div[contains(@class, "insales-ui-discount-error")]')
    CHECKOUT_BUTTON = (By.XPATH, '/html/body/div[2]/main/div[2]/div/form/div[2]/div/div[2]/button')

    # Локаторы для товаров
    SQUARE_CART_ITEM = (By.XPATH, '//div[@class="cart-item " and @data-product-id="253354771"]')
    SQUARE_ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="splide01-slide01"]/div/form/div/div[4]/div/div[2]/div/button')
    SQUARE_BUTTON_INCREASE_QUANTITY = (
        By.XPATH, '//div[@data-product-id="253354771"]//button[@data-quantity-change="1"]')
    SQUARE_BUTTON_DECREASE_QUANTITY = (
        By.XPATH, '//div[@data-product-id="253354771"]//button[@data-quantity-change="-1"]')
    SQUARE_BUTTON_DELETE_ITEM = (
        By.XPATH, '//div[@data-product-id="253354771"]//button[@class="button js-item-delete icon icon-trash"]')

    CIRCLE_CART_ITEM = (By.XPATH, '//div[@class="cart-item " and @data-product-id="253354830"]')
    CIRCLE_ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="splide01-slide02"]/div/form/div/div[4]/div/div[2]/div/button')
    CIRCLE_BUTTON_INCREASE_QUANTITY = (
        By.XPATH, '//div[@data-product-id="253354830"]//button[@data-quantity-change="1"]')
    CIRCLE_BUTTON_DECREASE_QUANTITY = (
        By.XPATH, '//div[@data-product-id="253354830"]//button[@data-quantity-change="-1"]')
    CIRCLE_BUTTON_DELETE_ITEM = (
        By.XPATH, '//div[@data-product-id="253354830"]//button[@class="button js-item-delete icon icon-trash"]')

    TRAPEZOID_CART_ITEM = (By.XPATH, '//div[@class="cart-item " and @data-product-id="253354942"]')
    TRAPEZOID_ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="splide01-slide03"]/div/form/div/div[4]/div/div[2]/div/button')
    TRAPEZOID_BUTTON_INCREASE_QUANTITY = (
        By.XPATH, '//div[@data-product-id="253354942"]//button[@data-quantity-change="1"]')
    TRAPEZOID_BUTTON_DECREASE_QUANTITY = (
        By.XPATH, '//div[@data-product-id="253354942"]//button[@data-quantity-change="-1"]')
    TRAPEZOID_BUTTON_DELETE_ITEM = (
        By.XPATH, '//div[@data-product-id="253354942"]//button[@class="button js-item-delete icon icon-trash"]')

    RHOMBUS_CART_ITEM = (By.XPATH, '//div[@class="cart-item " and @data-product-id="253355137"]')
    RHOMBUS_ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="splide01-slide04"]/div/form/div/div[4]/div/div[2]/div/button')
    RHOMBUS_BUTTON_INCREASE_QUANTITY = (
        By.XPATH, '//div[@data-product-id="253355137"]//button[@data-quantity-change="1"]')
    RHOMBUS_BUTTON_DECREASE_QUANTITY = (
        By.XPATH,
        '//div[@data-product-id="253355137"]//button[@data-quantity-change="-1"]//div[@data-product-id="253355137"]//button[@data-quantity-change="-1"]')
    RHOMBUS_BUTTON_DELETE_ITEM = (
        By.XPATH, '//div[@data-product-id="253355137"]//button[@class="button js-item-delete icon icon-trash"]')

    TRIANGLE_CART_ITEM = (By.XPATH, '//div[@class="cart-item " and @data-product-id="253355230"]')
    TRIANGLE_ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="splide01-slide05"]/div/form/div/div[4]/div/div[2]/div/button')
    TRIANGLE_BUTTON_INCREASE_QUANTITY = (
        By.XPATH, '//div[@data-product-id="253355230"]//button[@data-quantity-change="1"]')
    TRIANGLE_BUTTON_DECREASE_QUANTITY = (
        By.XPATH, '//div[@data-product-id="253355230"]//button[@data-quantity-change="-1"]')
    TRIANGLE_BUTTON_DELETE_ITEM = (
        By.XPATH, '//div[@data-product-id="253355230"]//button[@class="button js-item-delete icon icon-trash"]')

    HEXAGON_CART_ITEM = (By.XPATH, '//div[@class="cart-item " and @data-product-id="253355337"]')
    HEXAGON_ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="splide01-slide06"]/div/form/div/div[4]/div/div[2]/div/button')
    HEXAGON_BUTTON_INCREASE_QUANTITY = (
        By.XPATH, '//div[@data-product-id="253355337"]//button[@data-quantity-change="1"]')
    HEXAGON_BUTTON_DECREASE_QUANTITY = (
        By.XPATH, '//div[@data-product-id="253355337"]//button[@data-quantity-change="-1"]')
    HEXAGON_BUTTON_DELETE_ITEM = (
        By.XPATH, '//div[@data-product-id="253355337"]//button[@class="button js-item-delete icon icon-trash"]')

    ELLIPSE_CART_ITEM = (By.XPATH, '//div[@class="cart-item " and @data-product-id="253355471"]')
    ELLIPSE_ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="splide01-slide07"]/div/form/div/div[4]/div/div[2]/div/button')
    ELLIPSE_BUTTON_INCREASE_QUANTITY = (
        By.XPATH, '//div[@data-product-id="253355471"]//button[@data-quantity-change="1"]')
    ELLIPSE_BUTTON_DECREASE_QUANTITY = (
        By.XPATH, '//div[@data-product-id="253355471"]//button[@data-quantity-change="-1"]')
    ELLIPSE_BUTTON_DELETE_ITEM = (
        By.XPATH, '//div[@data-product-id="253355471"]//button[@class="button js-item-delete icon icon-trash"]')

    # Метод для получения локаторов в зависимости от типа товара
    @staticmethod
    def get_product_locators(product_type):
        if product_type == 'квадрат':
            return {
                'CART_ITEM': CartPageLocators.SQUARE_CART_ITEM,
                'ADD_TO_CART_BUTTON': CartPageLocators.SQUARE_ADD_TO_CART_BUTTON,
                'BUTTON_INCREASE_QUANTITY': CartPageLocators.SQUARE_BUTTON_INCREASE_QUANTITY,
                'BUTTON_DECREASE_QUANTITY': CartPageLocators.SQUARE_BUTTON_DECREASE_QUANTITY,
                'BUTTON_DELETE_ITEM': CartPageLocators.SQUARE_BUTTON_DELETE_ITEM
            }
        elif product_type == 'круг':
            return {
                'CART_ITEM': CartPageLocators.CIRCLE_CART_ITEM,
                'ADD_TO_CART_BUTTON': CartPageLocators.CIRCLE_ADD_TO_CART_BUTTON,
                'BUTTON_INCREASE_QUANTITY': CartPageLocators.CIRCLE_BUTTON_INCREASE_QUANTITY,
                'BUTTON_DECREASE_QUANTITY': CartPageLocators.CIRCLE_BUTTON_DECREASE_QUANTITY,
                'BUTTON_DELETE_ITEM': CartPageLocators.CIRCLE_BUTTON_DELETE_ITEM
            }
        elif product_type == 'трапеция':
            return {
                'CART_ITEM': CartPageLocators.TRAPEZOID_CART_ITEM,
                'ADD_TO_CART_BUTTON': CartPageLocators.TRAPEZOID_ADD_TO_CART_BUTTON,
                'BUTTON_INCREASE_QUANTITY': CartPageLocators.TRAPEZOID_BUTTON_INCREASE_QUANTITY,
                'BUTTON_DECREASE_QUANTITY': CartPageLocators.TRAPEZOID_BUTTON_DECREASE_QUANTITY,
                'BUTTON_DELETE_ITEM': CartPageLocators.TRAPEZOID_BUTTON_DELETE_ITEM
            }
        elif product_type == 'ромб':
            return {
                'CART_ITEM': CartPageLocators.RHOMBUS_CART_ITEM,
                'ADD_TO_CART_BUTTON': CartPageLocators.RHOMBUS_ADD_TO_CART_BUTTON,
                'BUTTON_INCREASE_QUANTITY': CartPageLocators.RHOMBUS_BUTTON_INCREASE_QUANTITY,
                'BUTTON_DECREASE_QUANTITY': CartPageLocators.RHOMBUS_BUTTON_DECREASE_QUANTITY,
                'BUTTON_DELETE_ITEM': CartPageLocators.RHOMBUS_BUTTON_DELETE_ITEM
            }
        elif product_type == 'треугольник':
            return {
                'CART_ITEM': CartPageLocators.TRIANGLE_CART_ITEM,
                'ADD_TO_CART_BUTTON': CartPageLocators.TRIANGLE_ADD_TO_CART_BUTTON,
                'BUTTON_INCREASE_QUANTITY': CartPageLocators.TRIANGLE_BUTTON_INCREASE_QUANTITY,
                'BUTTON_DECREASE_QUANTITY': CartPageLocators.TRIANGLE_BUTTON_DECREASE_QUANTITY,
                'BUTTON_DELETE_ITEM': CartPageLocators.TRIANGLE_BUTTON_DELETE_ITEM
            }
        elif product_type == 'шестиугольник':
            return {
                'CART_ITEM': CartPageLocators.HEXAGON_CART_ITEM,
                'ADD_TO_CART_BUTTON': CartPageLocators.HEXAGON_ADD_TO_CART_BUTTON,
                'BUTTON_INCREASE_QUANTITY': CartPageLocators.HEXAGON_BUTTON_INCREASE_QUANTITY,
                'BUTTON_DECREASE_QUANTITY': CartPageLocators.HEXAGON_BUTTON_DECREASE_QUANTITY,
                'BUTTON_DELETE_ITEM': CartPageLocators.HEXAGON_BUTTON_DELETE_ITEM
            }
        elif product_type == 'эллипс':
            return {
                'CART_ITEM': CartPageLocators.ELLIPSE_CART_ITEM,
                'ADD_TO_CART_BUTTON': CartPageLocators.ELLIPSE_ADD_TO_CART_BUTTON,
                'BUTTON_INCREASE_QUANTITY': CartPageLocators.ELLIPSE_BUTTON_INCREASE_QUANTITY,
                'BUTTON_DECREASE_QUANTITY': CartPageLocators.ELLIPSE_BUTTON_DECREASE_QUANTITY,
                'BUTTON_DELETE_ITEM': CartPageLocators.ELLIPSE_BUTTON_DELETE_ITEM
            }
        else:
            raise ValueError(f"Неверный тип товара: {product_type}")
