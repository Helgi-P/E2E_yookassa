import pytest
import allure
from main_page import MainPage
from product_page import ProductPage
from cart_page import CartPage
from order_page import OrderPage
import time
from OrderPageLocators import OrderPageLocators


@allure.feature('Процесс оформления заказа')
@allure.story('Простое добавление товаров в корзину с оформлением заказа только обязательными валидными данными')
@pytest.mark.order(1)
def test_product_order_flow1(driver):
    print('Простое добавление товаров в корзину с оформлением заказа только обязательными валидными данными')
    with allure.step('Переход на главную страницу'):
        main_page = MainPage(driver)
        main_page.open()

    with allure.step('Добавление квадрата в корзину'):
        main_page.add_square_to_cart()
        time.sleep(10)

    with allure.step('Переход на страницу продукта квадрата'):
        main_page = MainPage(driver)
        main_page.go_to_square_page()
        time.sleep(20)

    with allure.step('Увеличение количества квадрата на 2'):
        product_page = ProductPage(driver)
        product_page.increase_item_quantity(2)
        time.sleep(20)

    with allure.step('Переход в корзину через кнопку "В корзине х шт. Перейти"'):
        product_page.go_to_cart()
        time.sleep(10)

    with allure.step('Добавление 2 шт круга с использованием универсального метода'):
        cart_page = CartPage(driver)
        cart_page.modify_product_quantity(action='add', product_type='круг', quantity=2)
        time.sleep(10)

    with allure.step('Переход на страницу оформления заказа нажатием кнопки "Оформить заказ" с запоминанием их видов'):
        remembered_items = cart_page.proceed_to_checkout()
        time.sleep(10)

    with allure.step('Проверка отображения товаров на странице заказа'):
        order_page = OrderPage(driver)
        order_page.verify_cart_items(remembered_items)

    with allure.step('Корректное заполнение всех обязательных полей заказа'):
        order_page = OrderPage(driver)
        order_page.fill_contact_phone()
        order_page.fill_locality_valid()
        order_page.fill_client_name()

    with allure.step('Подтверждение заказа, с проверкой редиректа'):
        order_page = OrderPage(driver)
        order_page.submit_order()
        order_page.check_redirect_to_payment()

@allure.story('Добавление всех товаров в корзину с изменением способов оплаты и доставки')
@pytest.mark.order(2)
def test_product_order_flow2(driver):
    print('Добавление всех товаров в корзину с изменением способов оплаты и доставки')
    with allure.step('Переход на главную страницу'):
        main_page = MainPage(driver)
        main_page.open()

    with allure.step('Проверка элементов хэдера'):
        main_page.assert_header_elements()

    with allure.step('Добавить все товары в корзину'):
        main_page.add_all_products_to_cart()
        time.sleep(10)

    with allure.step('Переход в корзину через иконку'):
        main_page.open_cart_with_icon()

    with allure.step('Переход на страницу оформления заказа нажатием кнопки "Оформить заказ" с запоминанием их видов'):
        cart_page = CartPage(driver)
        cart_page.assert_header_elements()
        remembered_items = cart_page.proceed_to_checkout()

    with allure.step('Проверка отображения товаров на странице заказа'):
        order_page = OrderPage(driver)
        order_page.verify_cart_items(remembered_items)
        order_page.assert_header_elements()

    with allure.step('Корректное заполнение всех полей заказа c изменением способов заказа и оплаты'):
        order_page.fill_contact_phone()
        order_page.select_delivery_by_courier()
        order_page.fill_delivery_address()
        order_page.fill_order_comment()
        order_page.select_payment_sberpay()
        order_page.fill_client_name()
        time.sleep(5)
        order_page.fill_locality_valid()
        time.sleep(10)

    with allure.step('Подтверждение заказа, с проверкой редиректа'):
        order_page = OrderPage(driver)
        order_page.submit_order()
        order_page.check_redirect_to_payment()


@allure.story('Негативные проверки на сложном негативном пути')
@pytest.mark.order(3)
def test_product_order_negative_flow(driver):
    print('Негативные проверки на сложном негативном пути')
    with allure.step('Переход на главную страницу'):
        main_page = MainPage(driver)
        main_page.open()

    with allure.step('Переход в корзину без покупок'):
        main_page.open_cart_with_icon()

    with allure.step('Добавление 3х ромбов'):
        cart_page = CartPage(driver)
        cart_page.modify_product_quantity(action='add', product_type='ромб', quantity=3)

    with allure.step('Удаление ромбов'):
        cart_page = CartPage(driver)
        cart_page.modify_product_quantity(action='delete', product_type='ромб')

    with allure.step('Переход обратно в каталог'):
        cart_page = CartPage(driver)
        cart_page.go_back_to_catalog()
        time.sleep(2)

    with allure.step('Добавление эллипса, переход в корзину иконкой'):
        main_page = MainPage(driver)
        main_page.add_ellipse_to_cart()
        time.sleep(5)
        main_page.open_cart_with_icon()
        time.sleep(5)

    with allure.step('Ввод промокода, переход к оформлению заказа'):
        cart_page = CartPage(driver)
        cart_page.apply_promo_code('InvalidPromo')

    with allure.step('Переход на страницу оформления заказа'):
        cart_page.assert_header_elements()
        remembered_items = cart_page.proceed_to_checkout()

    with allure.step('Проверка отображения товаров на странице заказа'):
        order_page = OrderPage(driver)
        order_page.verify_cart_items(remembered_items)
        order_page.assert_header_elements()

    with allure.step('Валидное заполнение телефона, нажатие на кнопку "Подтвердить заказ" '
                     'без заполненных полей "Населенный пункт", "Контактное лицо (ФИО)"'):
        print("Валидное заполнение телефона")
        order_page.fill_contact_phone()
        time.sleep(5)
        order_page.submit_order()
        time.sleep(5)
        if not order_page.check_redirect_to_payment():
            print("Переход на следующую проверку заполнения полей.")

    with allure.step('Заполнение только невалидного населенного пункта и повторная попытка'):
        print("Заполнение невалидного населенного пункта")
        order_page.fill_locality_invalid()
        time.sleep(10)
        order_page.submit_order()
        time.sleep(5)
        if not order_page.check_redirect_to_payment():
            print("Переход на следующую проверку заполнения полей.")

    with allure.step('Заполнение валидного населенного пункта и повторная попытка без ФИО'):
        print("Заполнение валидного населенного пункта")
        order_page.fill_locality_valid()
        time.sleep(10)
        order_page.submit_order()
        time.sleep(5)
        if not order_page.check_redirect_to_payment():
            print("Переход на следующую проверку заполнения полей.")

    with allure.step('Проверка, что поле ФИО не заполнено'):
        print("Смотрим, что ФИО не заполнено")
        if order_page.is_element_visible(OrderPageLocators.ERROR_NOTIFICATION_FIO):
            error_message = order_page.get_element_text(OrderPageLocators.ERROR_NOTIFICATION_FIO)
            print(f"Ошибка в поле 'Контактное лицо (ФИО)': {error_message}")
            order_page.take_screenshot("error_fio_is_empty")
            print("Тест завершён. Поле ФИО не заполнено.")
