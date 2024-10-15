from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Поле ввода "Контактный телефон"
    CONTACT_PHONE = (By.XPATH, '//*[@id="client_phone"]')

    # Поле ввода "Населенный пункт"
    LOCALITY = (By.XPATH, '//*[@id="shipping_address_full_locality_name"]')

    # Уведомление "Ошибка! Не удалось определить населенный пункт"
    LOCALITY_NOT_FOUND = (By.XPATH, '//*[@id="delivery-location-not-valid"]')

    # Радиобатон "Самовывоз"
    PICKUP_OPTION = (By.XPATH, '//*[@id="delivery_variants"]/div[2]/label[1]')

    # Радиобатон "Курьером"
    DELIVERY_OPTION = (By.XPATH, '//*[@id="delivery_variants"]/div[2]/label[2]')

    # Поле ввода "Адрес" (появляется при выборе "Курьером")
    DELIVERY_ADDRESS = (By.XPATH, '//*[@id="shipping_address_address"]')

    # Поле ввода "Комментарии к заказу"
    ORDER_COMMENT = (By.XPATH, '//*[@id="order_comment"]')

    # Поле ввода "Контактное лицо (ФИО)"
    CLIENT_NAME = (By.XPATH, '//*[@id="client_name"]')

    # Поле ввода "Email"
    CLIENT_EMAIL = (By.XPATH, '//*[@id="client_email"]')

    # Радиобатон "Виджет: банковские карты, ЮMoney, СБП, SberPay"
    PAYMENT_WIDGET = (By.XPATH, '//*[@id="payment_gateways"]/div/label[1]')

    # Радиобатон "SberPay"
    PAYMENT_SBERPAY = (By.XPATH, '//*[@id="payment_gateways"]/div/label[2]')

    # Радиобатон "Перейти на страницу ЮKassa"
    PAYMENT_YOOKASSA = (By.XPATH, '//*[@id="payment_gateways"]/div/label[3]')

    # Кнопка "Подтвердить заказ"
    SUBMIT_ORDER = (By.XPATH, '//*[@id="create_order"]')

    # Элементы товаров в корзине
    CART_ITEM_LIST = (By.XPATH, '/html/body/div[1]/main/div/div/div/div/div[2]/div')

    # Описание товаров
    CART_ITEM_SQUARE = (By.XPATH, "//div[@class='co-basket_item-description' and text()='Квадрат']/..")
    CART_ITEM_CIRCLE = (By.XPATH, "//div[@class='co-basket_item-description' and text()='Круг']/..")
    CART_ITEM_TRAPEZOID = (
        By.XPATH, "//div[@class='co-basket_item-description' and text()='Равнобедренная трапеция']/..")
    CART_ITEM_RHOMBUS = (By.XPATH, "//div[@class='co-basket_item-description' and text()='Ромб']/..")
    CART_ITEM_TRIANGLE = (By.XPATH, "//div[@class='co-basket_item-description' and text()='Треугольник']/..")
    CART_ITEM_HEXAGON = (By.XPATH, "//div[@class='co-basket_item-description' and text()='Шестиугольник']/..")
    CART_ITEM_ELLIPSE = (By.XPATH, "//div[@class='co-basket_item-description' and text()='Эллипс']/..")

    # Уведомления об ошибке
    ERROR_NOTIFICATION_LOCALITY = ('xpath', '//*[@id="delivery_address"]//div[contains(@class, "co-notice--danger")]')
    ERROR_NOTIFICATION_FIO = ('xpath', '//*[@id="tabs-person"]//div[contains(@class, "co-notice--danger")]')
