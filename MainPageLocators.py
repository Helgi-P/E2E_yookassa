from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы для товаров
    PRODUCT_PREVIEW_SQUARE = (By.XPATH, '//form[@data-product-id="253354771"]')
    BUTTON_ADD_IN_CART_SQUARE = (
    By.XPATH, '//form[@data-product-id="253354771"]//button[contains(@class, "product-preview__buy-btn")]')
    LINK_TO_PRODUCT_PAGE_SQUARE = (By.XPATH, '//form[@data-product-id="253354771"]//a')

    PRODUCT_PREVIEW_CIRCLE = (By.XPATH, '//form[@data-product-id="253354830"]')
    BUTTON_ADD_IN_CART_CIRCLE = (
    By.XPATH, '//form[@data-product-id="253354830"]//button[contains(@class, "product-preview__buy-btn")]')
    LINK_TO_PRODUCT_PAGE_CIRCLE = (By.XPATH, '//form[@data-product-id="253354830"]//a')

    PRODUCT_PREVIEW_TRAPEZOID = (By.XPATH, '//form[@data-product-id="253354942"]')
    BUTTON_ADD_IN_CART_TRAPEZOID = (
    By.XPATH, '//form[@data-product-id="253354942"]//button[contains(@class, "product-preview__buy-btn")]')
    LINK_TO_PRODUCT_PAGE_TRAPEZOID = (By.XPATH, '//form[@data-product-id="253354942"]//a')

    PRODUCT_PREVIEW_RHOMBUS = (By.XPATH, '//form[@data-product-id="253355137"]')
    BUTTON_ADD_IN_CART_RHOMBUS = (
    By.XPATH, '//form[@data-product-id="253355137"]//button[contains(@class, "product-preview__buy-btn")]')
    LINK_TO_PRODUCT_PAGE_RHOMBUS = (By.XPATH, '//form[@data-product-id="253355137"]//a')

    PRODUCT_PREVIEW_TRIANGLE = (By.XPATH, '//form[@data-product-id="253355230"]')
    BUTTON_ADD_IN_CART_TRIANGLE = (
    By.XPATH, '//form[@data-product-id="253355230"]//button[contains(@class, "product-preview__buy-btn")]')
    LINK_TO_PRODUCT_PAGE_TRIANGLE = (By.XPATH, '//form[@data-product-id="253355230"]//a')

    PRODUCT_PREVIEW_HEXAGON = (By.XPATH, '//form[@data-product-id="253355337"]')
    BUTTON_ADD_IN_CART_HEXAGON = (
    By.XPATH, '//form[@data-product-id="253355337"]//button[contains(@class, "product-preview__buy-btn")]')
    LINK_TO_PRODUCT_PAGE_HEXAGON = (By.XPATH, '//form[@data-product-id="253355337"]//a')

    PRODUCT_PREVIEW_ELLIPSE = (By.XPATH, '//form[@data-product-id="253355471"]')
    BUTTON_ADD_IN_CART_ELLIPSE = (
    By.XPATH, '//form[@data-product-id="253355471"]//button[contains(@class, "product-preview__buy-btn")]')
    LINK_TO_PRODUCT_PAGE_ELLIPSE = (By.XPATH, '//form[@data-product-id="253355471"]//a')
