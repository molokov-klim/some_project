# coding: utf-8
import time
from selenium.common.exceptions import NoSuchElementException

from consts.locators import sigma_kassa_locators as sk_locator

from core.decorators.decorators import my_step_info, screenshots
from core.adb import adb
from applications.SigmaCashRegister.sk_transfer import SigmaAppTransfer


class SigmaAppCart(SigmaAppTransfer):
    def __init__(self):
        super().__init__()

    @my_step_info("Добавление товара в корзину")
    @screenshots()
    def add_item_to_cart_specific(self, category: tuple, item: tuple, quantity: int = 1, timeout: int = 60):
        """
        Метод переходит в указанную категорию и добавляет указанный товар в корзину.
        Ожидает главное окно. Отдает главное окно.
        category: категория товара
        item: наименование товара
        quantity: количество товара
        """
        assert self.wait_for_main_window_goods()
        assert self.transfer_to_category(category=category, timeout=60)
        assert self.add_item_to_cart(item, quantity=quantity)
        start_time = time.time()
        while time.time() - start_time < timeout:
            assert self.tap_to_element(sk_locator.MAIN_HEADER_BTN_BACK)
            self.wait_for_window(locator=sk_locator.MAIN_HEADER_TV_TITLE,
                                 text=sk_locator.MAIN_HEADER_TV_TITLE_GOODS_TEXT,
                                 timeout=3)
            if self.is_window(locator=sk_locator.MAIN_HEADER_TV_TITLE,
                              text=sk_locator.MAIN_HEADER_TV_TITLE_GOODS_TEXT):
                break
        return True

    @my_step_info("Поиск и добавление товара")
    @screenshots()
    def add_item_to_cart(self, item: tuple, quantity: int = 1):
        """
        Метод добавляет указанный товар в корзину.
        Ожидает главное окно. Отдает главное окно.
        item: наименование товара
        quantity: количество товара
        timeout: максимальное время ожидания в секундах
        """
        assert self.scroll_to(item)
        for i in range(quantity):
            assert self.tap_to_element(item)
        return True

    def is_cart_empty(self):
        """
        Метод проверки наличия товаров в корзине. Возвращает bool.
        Ожидает окно корзина, отдает окно корзина.
        """
        if self.wait_for_window(locator=sk_locator.CART_TV_EMPTY_MESSAGE,
                                text=sk_locator.CART_TV_EMPTY_MESSAGE_TEXT,
                                timeout=2):
            return True
        return False

    def clear_cart(self):
        """
        Метод проверяет количество товаров в корзине, если более 0, то удаляет чек.
        Ожидает главное окно товары, отдает главное окно товары.
        """
        self.logger.info("Очистка корзины")
        assert self.wait_for_main_window_goods()
        if int(self.get_element_attribute(sk_locator.MAIN_FOOTER_TV_ORDER_COUNTER, attr='text')) != 0:
            assert self.transfer_to_cart()
            assert self.tap_to_element(locator=sk_locator.CART_BTN_ORDER_OPTIONS)
            assert self.tap_to_element(locator=sk_locator.CART_ORDER_OPTIONS_CANCEL_RECEIPT)
            assert self.tap_to_element(locator=sk_locator.CART_ORDER_CANCEL_RECEIPT_REASON_TV_DISCARD_ORDER)
            assert self.tap_to_element(locator=sk_locator.CART_ORDER_CANCEL_RECEIPT_REASON_BTN_NEXT)
            assert self.wait_for_main_window_goods()
        self.logger.info("Успешная очистка корзины")
        return True

    def add_item_to_cart_weight_manual_input(self, category: tuple, item: tuple):
        """
        Метод добавляет весовой товар в корзину, вес вводит вручную.
        Ожидает главное окно товары, отдает главное окно товары.
        category: категория товара
        item: наименование товара
        """
        self.logger.info(f"Добавление весового товара в корзину. {category=}, {item=}")
        assert self.wait_for_main_window_goods()
        assert self.scroll_to_and_tap(category)
        assert self.scroll_to_and_tap(item)
        assert self.process_weight_item()
        assert self.tap_to_element(sk_locator.MAIN_HEADER_BTN_BACK)
        return True

    def process_weight_item(self, weight: str = '1'):
        """
        Метод обработки окна ввода веса. Вводит указанное значение и тапает далее.
        weight: вес товара
        """
        self.logger.info("Обработка окна ввода веса")
        time.sleep(5)  # не трогать работает adb
        for i in weight:
            assert adb.input_keycode_num_(int(i))
        time.sleep(0.1)  # не трогать работает adb
        assert self.tap_to_element(sk_locator.CART_ORDER_ADD_WEIGHT_ITEM_BTN_NEXT)
        return True

    def add_custom_price(self, quantity: int, timeout=600):
        """
        Метод добавления товаров своя цена в корзину
        """
        start_time = time.time()
        assert self.transfer_to_custom_price()
        while self.get_element_attribute(locator=('id', 'ru.sigma.app.debug:id/orderItemsCount'), attr='text') != str(
                quantity) \
                and time.time() - start_time < timeout:
            assert self.tap_to_element(locator=('id', 'ru.sigma.app.debug:id/buttonOne'))
            assert self.tap_to_element(locator=('id', 'ru.sigma.app.debug:id/checkButton'))
        assert self.tap_to_element(locator=sk_locator.MAIN_HEADER_BTN_GOODS_PT5F)
        return True

    def choose_type_custom_price_item(self, item_type: str):
        """
        Изменить тип товара для товара со свободной ценой
        """
        assert self.transfer_to_custom_price_item_settings(item='Товар')
        assert self.tap_to_element(locator=("xpath", "//android.widget.TextView[contains(@text,'Тип "
                                                     "товара')]/following-sibling::android.widget.Spinner"))
        assert self.scroll_to_and_tap(locator=('xpath', f"//android.widget.TextView[contains(@text,'{item_type}')]"))
        assert self.tap_to_element(locator=('xpath', f"//android.widget.TextView[contains(@text,'Сохранить')]"))
        return True

    def choose_custom_price_item_options(self, option: str):
        """
        Изменить признак способа расчета (тег 1214)
        """
        assert self.transfer_to_custom_price_item_settings(item='Товар')
        assert self.tap_to_element(locator=("xpath", "//android.widget.TextView[contains(@text,'Тип "
                                                     "товара')]/following-sibling::android.widget.Spinner"))
        assert self.tap_to_element(locator=('xpath', f"//android.widget.TextView[contains(@text,\"Работа\")]"))
        assert self.tap_to_element(locator=('xpath', '//android.widget.EditText[@text="Работа"]'))
        for i in "Работа":
            adb.tap(*sk_locator.PT5_VIRTUAL_KEYBOARD_CIRILLIC['BACKSPACE'])
        adb.tap(*sk_locator.PT5_VIRTUAL_KEYBOARD_QWERTY['q'])
        if self.get_element_attribute(locator=('xpath', '//android.widget.EditText[@text="Работа"]'),
                                      attr='text') == 'q':
            adb.input_by_virtual_keyboard(key="LANG", keyboard=sk_locator.PT5_VIRTUAL_KEYBOARD_CIRILLIC)
        adb.tap(*sk_locator.PT5_VIRTUAL_KEYBOARD_CIRILLIC['BACKSPACE'])
        for letter in option:
            assert adb.input_by_virtual_keyboard(key=letter, keyboard=sk_locator.PT5_VIRTUAL_KEYBOARD_CIRILLIC)
        assert self.tap_to_element(locator=('xpath', f"//android.widget.TextView[contains(@text,'Сохранить')]"))
        if self.is_element_displayed(locator=('xpath', f"//android.widget.TextView[contains(@text,'Сохранить')]")):
            assert self.tap_to_element(locator=('xpath', f"//android.widget.TextView[contains(@text,'Сохранить')]"))
        assert self.tap_to_element(locator=('xpath',
                                            f'//android.widget.TextView[@text=\'{option}\']/following-sibling::android.widget.LinearLayout/android.widget.ImageView'))
        assert adb.tap(*sk_locator.CART_ITEM_OPTIONS[option])
        return True
