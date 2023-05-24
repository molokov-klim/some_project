# coding: utf-8
import time

import config
from consts.locators import sigma_kassa_locators as sk_locator
from core.adb import adb
from core.decorators.decorators import my_step_info, screenshots

from applications.SigmaCashRegister.sk_wait import SigmaAppWait
from applications.SigmaCashRegister.sk_modal import SigmaAppModal
from applications.SigmaCashRegister.sk_get import SigmaAppGet


class SigmaAppTransfer(SigmaAppWait, SigmaAppModal, SigmaAppGet):
    def __init__(self):
        super().__init__()
        self.wait = SigmaAppWait
        self.modal = SigmaAppModal
        self.get = SigmaAppGet

        self.valid_1054 = sk_locator.VALID_1054
        self.valid_payment_methods = sk_locator.VALID_PAYMENT_METHODS

        self.payment_locators = sk_locator.PAYMENT_METHODS_LOCATORS

    def transfer_to_custom_price(self):
        """
        Метод перехода в окно "Своя цена".
        Ожидает главное окно товары, отдает главное окно своя цена
        """
        assert self.wait_for_main_window_goods()
        assert self.tap_to_element(sk_locator.MAIN_HEADER_BTN_CUSTOM_PRICE_PT5F)
        assert self.wait_for_window(locator=sk_locator.MAIN_HEADER_TV_TITLE,
                                    text='Св.цена')

    @my_step_info("Перемещение в товарную категорию")
    @screenshots()
    def transfer_to_category(self, category: tuple, timeout: int = 60):
        """
        Метод перемещения в категорию товаров.
        Ожидает "главное окно товары", отдает окно категории.
        """
        # assert self.scroll_to(category)
        start_time = time.time()
        title = self.get_title()
        new_title = title
        while title == new_title:
            assert self.scroll_to_and_tap(locator=category)
            new_title = self.get_title()
            if time.time() - start_time > timeout:
                self.logger.error(TimeoutError(f"Timeout exceeded ({timeout} seconds)"))
                return False
            time.sleep(1)
        return True

    @my_step_info("Перемещение в корзину")
    @screenshots()
    def transfer_to_cart(self, timeout: int = 10):
        """
        Метод перемещения в окно "корзина".
        Ожидает "главное окно товары", отдает окно "корзина"
        """
        assert self.wait_for_main_window_goods(timeout=timeout)
        assert self.tap_to_element(locator=sk_locator.MAIN_FOOTER_BTN_BLUE)
        assert self.wait_for_window(locator=sk_locator.CART_TV_TITLE,
                                    text=sk_locator.CART_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение к оплате")
    @screenshots()
    def transfer_to_payment(self, tag_1054: str = 'income',
                            payment_method: str = "cash",
                            timeout: int = 10,
                            electronically: bool = False,
                            company_email: str = ""):
        """
        Метод перемещения в окно "оплата".
        Ожидает "главное окно товары", отдает окно "оплата".
        tag_1054: признак расчета ['income', 'outcome']
        payment_method: способ оплаты ['cash', 'card', 'qr', 'combo']
        """
        assert tag_1054 in self.valid_1054
        assert payment_method in self.valid_payment_methods
        assert self.transfer_to_cart()
        assert self.tap_to_element(locator=sk_locator.CART_BTN_NEXT)
        assert self.process_modal_1054(tag_1054=tag_1054)
        assert self.process_modal_many_receipts()
        assert self.wait_for_choose_payment_type(timeout=5)
        if electronically:
            if company_email:
                assert self.tap_to_element(locator=sk_locator.PAYMENT_CHOOSE_BTN_ELECTRONIC_RECEIPT_DATA)
                time.sleep(1)
                assert self.tap_to_element(locator=sk_locator.ELECTRONICALLY_RECEIPT_DATA_RADIO_COMPANY_EMAIL)
                time.sleep(1)
                assert self.tap_to_element(locator=sk_locator.ELECTRONICALLY_RECEIPT_DATA_BTN_OK)
            else:
                assert self.tap_to_element(locator=sk_locator.PAYMENT_CHOOSE_BTN_ELECTRONIC_RECEIPT_DATA)
                time.sleep(1)
                assert adb.input_text(text=config.ELECTRONICALLY_FD_EMAIL)
                time.sleep(1)
                assert self.tap_to_element(locator=sk_locator.ELECTRONICALLY_RECEIPT_DATA_BTN_OK)
        assert self.tap_to_element(self.payment_locators[payment_method])
        time.sleep(1)
        return True

    @my_step_info("Перемещение к выбору способа оплаты")
    @screenshots()
    def transfer_to_choose_payment_method(self, tag_1054='income', timeout: int = 10):
        """
        Метод перемещения в окно "выбор способа оплаты".
        Ожидает "главное окно товары", отдает окно "выбор способа оплаты".
        tag_1054: признак расчета ['income', 'outcome']
        """
        assert tag_1054 in self.valid_1054
        assert self.transfer_to_cart()
        assert self.tap_to_element(locator=sk_locator.CART_BTN_NEXT)
        assert self.process_modal_1054(tag_1054=tag_1054)
        assert self.wait_for_window(locator=sk_locator.PAYMENT_CHOOSE_TV_TITLE,
                                    text=sk_locator.PAYMENT_CHOOSE_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение в чеки и возвраты")
    @screenshots()
    def transfer_to_receipts_and_returns(self, timeout: int = 10):
        """
        Метод перемещения в окно "чеки и возвраты".
        Ожидает "главное окно товары", отдает окно "чеки и возвраты"
        """
        assert self.wait_for_main_window_goods(timeout=timeout)
        assert self.tap_to_element(locator=sk_locator.MAIN_HEADER_BTN_HAMBURGER)
        assert self.tap_to_element(locator=sk_locator.MAIN_SIDEBAR_BTN_RECEIPTS_AND_RETURNS)
        assert self.wait_for_window(locator=sk_locator.RECEIPTS_AND_RETURNS_TV_TITLE,
                                    text=sk_locator.RECEIPTS_AND_RETURNS_TV_TITLE_TEXT,
                                    timeout=timeout)
        assert self.wait_until_element_will_not_displayed(locator=sk_locator.RECEIPTS_AND_RETURNS_IMG_PROGRESS,
                                                          timeout=180)
        time.sleep(2)
        return True

    @my_step_info("Перемещение в кассовые операции")
    @screenshots()
    def transfer_to_cash_transaction(self, timeout: int = 10):
        """
        Метод перемещения в окно "кассовые операции".
        Ожидает "главное окно товары", отдает окно "кассовые операции"
        """
        assert self.wait_for_main_window_goods(timeout=timeout)
        assert self.tap_to_element(locator=sk_locator.MAIN_HEADER_BTN_HAMBURGER)
        assert self.tap_to_element(locator=sk_locator.MAIN_SIDEBAR_BTN_CASH_TRANSACTIONS)
        assert self.wait_for_window(locator=sk_locator.CASH_TRANSACTIONS_TV_TITLE,
                                    text=sk_locator.CASH_TRANSACTIONS_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение в формирование чека коррекции")
    @screenshots()
    def transfer_to_correction_receipt(self, timeout: int = 10):
        """
        Метод перемещения в окно формирования чека коррекции.
        Ожидает "главное окно товары", отдает окно формирования чека коррекции.
        """
        assert self.transfer_to_cash_transaction()
        assert self.scroll_to_and_tap(locator=sk_locator.CASH_TRANSACTIONS_BTN_MAKE_CORRECTION)
        assert self.wait_for_window(locator=sk_locator.CORRECTION_RECEIPT_FFD_1_05_TV_TITLE,
                                    text=sk_locator.CORRECTION_RECEIPT_FFD_1_05_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение в окно клиентов")
    @screenshots()
    def transfer_to_clients(self, timeout: int = 30):
        """
        Метод перемещения в окно клиентов.
        Ожидает "главное окно товары", отдает окно клиентов.
        """
        assert self.wait_for_main_window_goods(timeout=timeout)
        assert self.tap_to_element(locator=sk_locator.MAIN_HEADER_BTN_HAMBURGER)
        assert self.tap_to_element(locator=sk_locator.MAIN_SIDEBAR_BTN_CLIENTS)
        assert self.wait_for_window(locator=sk_locator.CLIENTS_TV_TITLE,
                                    text=sk_locator.CLIENTS_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(2)
        return True

    @my_step_info("Перемещение в окно создания нового клиента")
    @screenshots()
    def transfer_to_create_client(self, timeout: int = 10):
        """
        Метод перемещения в окно создания клиента.
        Ожидает "главное окно товары", отдает окно создания клиента.
        """
        assert self.transfer_to_clients()
        assert self.tap_to_element(locator=sk_locator.CLIENTS_BTN_ADD_NEW_CLIENT)
        assert self.wait_for_window(locator=sk_locator.CLIENTS_NEW_TV_TITLE,
                                    text=sk_locator.CLIENTS_NEW_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение в окно создания товара")
    @screenshots()
    def transfer_to_create_item(self, timeout: int = 60):
        """
        Метод перемещения в окно создания товара.
        Ожидает "главное окно товары", отдает окно создания товара.
        """
        assert self.wait_for_main_window_goods(timeout=timeout)
        assert self.tap_to_element(locator=sk_locator.MAIN_HEADER_BTN_HAMBURGER)
        assert self.tap_to_element(locator=sk_locator.MAIN_SIDEBAR_BTN_CREATE_PRODUCT)
        assert self.wait_for_window(locator=sk_locator.CREATE_PRODUCT_TV_TITLE,
                                    text=sk_locator.CREATE_PRODUCT_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение в окно создания услуги")
    @screenshots()
    def transfer_to_create_service(self, timeout: int = 60):
        """
        Метод перемещения в окно создания услуги.
        Ожидает "главное окно товары", отдает окно создания услуги.
        """
        assert self.wait_for_main_window_goods(timeout=timeout)
        assert self.tap_to_element(locator=sk_locator.MAIN_HEADER_BTN_HAMBURGER)
        assert self.tap_to_element(locator=sk_locator.MAIN_SIDEBAR_BTN_CREATE_SERVICE)
        assert self.wait_for_window(locator=sk_locator.CREATE_SERVICE_TV_TITLE,
                                    text=sk_locator.CREATE_SERVICE_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение в настройки")
    @screenshots()
    def transfer_to_settings(self, timeout: int = 60):
        """
        Метод перемещения в окно "настройки".
        Ожидает "главное окно товары", отдает окно "настройки"
        """
        assert self.wait_for_main_window_goods(timeout=timeout)
        assert self.tap_to_element(locator=sk_locator.MAIN_HEADER_BTN_HAMBURGER)
        assert self.tap_to_element(locator=sk_locator.MAIN_SIDEBAR_BTN_SETTINGS)
        assert self.wait_for_window(locator=sk_locator.SETTINGS_TV_TITLE,
                                    text=sk_locator.SETTINGS_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение в правила торговли")
    @screenshots()
    def transfer_to_trading_rules(self, timeout: int = 60):
        """
        Метод перемещения в окно "правила торговли".
        Ожидает "главное окно товары", отдает окно "правила торговли"
        """
        assert self.transfer_to_settings()
        assert self.tap_to_element(locator=sk_locator.SETTINGS_BTN_TRADING_RULES)
        assert self.wait_for_window(locator=sk_locator.TRADING_RULES_TV_TITLE,
                                    text=sk_locator.TRADING_RULES_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение в окно маркировки")
    @screenshots()
    def transfer_to_marking(self, timeout: int = 10):
        """
        Метод перемещения в окно маркировки.
        Ожидает "главное окно товары", отдает окно маркировки.
        """
        assert self.transfer_to_settings()
        assert self.tap_to_element(locator=sk_locator.SETTINGS_BTN_MARKING)
        assert self.wait_for_window(locator=sk_locator.MARKING_TV_TITLE,
                                    text=sk_locator.MARKING_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение в окно безналичных платежей")
    @screenshots()
    def transfer_to_cashless_payments(self, timeout: int = 10):
        """
        Метод перемещения в окно безналичных платежей.
        Ожидает "главное окно товары", отдает окно безналичных платежей.
        """
        assert self.transfer_to_settings()
        assert self.tap_to_element(locator=sk_locator.SETTINGS_BTN_CASHLESS_PAYMENTS)
        assert self.wait_for_window(locator=sk_locator.CASHLESS_PAYMENTS_TV_TITLE,
                                    text=sk_locator.CASHLESS_PAYMENTS_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение в окно принтеры чеков")
    @screenshots()
    def transfer_to_receipt_printer(self, timeout: int = 10):
        """
        Метод перемещения в окно принтер чеков.
        Ожидает "главное окно товары", отдает окно принтер чеков.
        """
        assert self.transfer_to_settings()
        assert self.tap_to_element(locator=sk_locator.SETTINGS_BTN_RECEIPT_PRINTER)
        assert self.wait_for_window(locator=sk_locator.RECEIPT_PRINTER_TV_TITLE,
                                    text=sk_locator.RECEIPT_PRINTER_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение в окно сканеры")
    @screenshots()
    def transfer_to_scanners(self, timeout: int = 10):
        """
        Метод перемещения в окно сканеры.
        Ожидает "главное окно товары", отдает окно сканеры.
        """
        assert self.transfer_to_settings()
        assert self.tap_to_element(locator=sk_locator.SETTINGS_BTN_SCANNERS)
        assert self.wait_for_window(locator=sk_locator.SCANNERS_TV_TITLE,
                                    text=sk_locator.SCANNERS_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение в окно ЕГАИС")
    @screenshots()
    def transfer_to_egais(self, timeout: int = 10):
        """
        Метод перемещения в окно ЕГАИС.
        Ожидает "главное окно товары", отдает окно ЕГАИС.
        """
        assert self.transfer_to_settings()
        assert self.tap_to_element(locator=sk_locator.SETTINGS_BTN_EGAIS)
        assert self.wait_for_window(locator=sk_locator.EGAIS_TV_TITLE,
                                    text=sk_locator.EGAIS_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение в окно весы")
    @screenshots()
    def transfer_to_scales(self, timeout: int = 10):
        """
        Метод перемещения в окно весы.
        Ожидает "главное окно товары", отдает окно весы.
        """
        assert self.transfer_to_settings()
        assert self.tap_to_element(locator=sk_locator.SETTINGS_BTN_SCALES)
        assert self.wait_for_window(locator=sk_locator.SCALES_TV_TITLE,
                                    text=sk_locator.SCALES_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение в окно информация о кассе")
    @screenshots()
    def transfer_to_cashregister_info(self, timeout: int = 10):
        """
        Метод перемещения в окно информация о кассе.
        Ожидает "главное окно товары", отдает окно весы.
        """
        assert self.transfer_to_settings()
        assert self.tap_to_element(locator=sk_locator.SETTINGS_BTN_CASHREGISTER_INFO)
        assert self.wait_for_window(locator=sk_locator.CASHREGISTER_INFO_TV_TITLE,
                                    text=sk_locator.CASHREGISTER_INFO_TV_TITLE_TEXT,
                                    timeout=timeout)
        time.sleep(1)
        return True

    @my_step_info("Перемещение в окно услуги")
    @screenshots()
    def transfer_to_services(self, timeout: int = 10):
        """
        Метод перемещения в окно услуги.
        Ожидает "главное окно товары", отдает окно услуги.
        """
        assert self.wait_for_main_window_goods(timeout=timeout)
        assert self.tap_to_element(locator=sk_locator.MAIN_HEADER_BTN_SERVICE_PT5F)
        assert self.wait_for_window(locator=sk_locator.MAIN_HEADER_TV_TITLE,
                                    text=sk_locator.MAIN_HEADER_TV_TITLE_SERVICE_TEXT,
                                    timeout=timeout)
        return True

    @my_step_info("Перемещение в окно своя цена")
    @screenshots()
    def transfer_to_custom_price(self, timeout: int = 10):
        """
        Метод перемещения в окно своя цена.
        Ожидает "главное окно товары", отдает окно своя цена.
        """
        assert self.wait_for_main_window_goods(timeout=timeout)
        assert self.tap_to_element(locator=sk_locator.MAIN_HEADER_BTN_CUSTOM_PRICE_PT5F)
        assert self.wait_for_window(locator=sk_locator.MAIN_HEADER_TV_TITLE,
                                    text=sk_locator.MAIN_HEADER_TV_TITLE_CUSTOM_PRICE_TEXT,
                                    timeout=timeout)
        return True

    @my_step_info("Перемещение в окно поиска")
    @screenshots()
    def transfer_to_search(self, timeout: int = 10):
        """
        Метод перемещения в окно поиск.
        Ожидает "главное окно товары", отдает окно поиск.
        """
        assert self.wait_for_main_window_goods(timeout=timeout)
        assert self.tap_to_element(locator=sk_locator.MAIN_HEADER_BTN_SEARCH_PT5F)
        assert self.wait_for_window(locator=sk_locator.MAIN_HEADER_TV_TITLE,
                                    text=sk_locator.MAIN_HEADER_TV_TITLE_SEARCH_TEXT,
                                    timeout=timeout)
        return True

    @my_step_info("Перемещение в отложенные чеки")
    @screenshots()
    def transfer_to_delayed_receipt(self, timeout: int = 10):
        """
        Метод перемещения в окно отложенные чеки.
        Ожидает "главное окно товары", отдает окно отложенные чеки.
        """
        assert self.transfer_to_cart(timeout=timeout)
        assert self.tap_to_element(locator=sk_locator.CART_BTN_DELAYED_RECEIPTS_PT5F)
        assert self.wait_for_window(locator=sk_locator.DELAYED_RECEIPTS_TV_TITLE,
                                    text=sk_locator.DELAYED_RECEIPTS_TV_TITLE_TEXT,
                                    timeout=timeout)
        return True

    @my_step_info("Перемещение в основное окно")
    @screenshots()
    def transfer_from_receipts_and_returns(self, timeout: int = 10):
        """
        Метод перемещения в "главное окно товары" и окна "чеки и возвраты".
        Ожидает окно "чеки и возвраты", отдает "главное окно товары".
        """
        assert self.wait_for_window(locator=sk_locator.RECEIPTS_AND_RETURNS_TV_TITLE,
                                    text=sk_locator.RECEIPTS_AND_RETURNS_TV_TITLE_TEXT,
                                    timeout=timeout)
        assert self.tap_to_element(locator=sk_locator.RECEIPTS_AND_RETURNS_BTN_BACK)
        assert self.wait_for_main_window_goods(timeout=timeout)
        return True

    @my_step_info("Перемещение в основное окно")
    @screenshots()
    def transfer_from_cash_transaction(self, timeout: int = 10):
        """
        Метод перемещения в "главное окно товары" и окна "кассовые операции".
        Ожидает окно "кассовые операции", отдает "главное окно товары".
        """
        assert self.wait_for_window(locator=sk_locator.CASH_TRANSACTIONS_TV_TITLE,
                                    text=sk_locator.CASH_TRANSACTIONS_TV_TITLE_TEXT,
                                    timeout=timeout)
        assert self.tap_to_element(locator=sk_locator.CART_BTN_BACK)
        assert self.wait_for_main_window_goods(timeout=timeout)
        return True

    def transfer_to_custom_price_item_settings(self, item: str, timeout: int = 10):
        """
        Метод перехода в настройки товара со свободной ценой.
        Ожидает окно корзина, отдает окно товара
        """
        assert self.wait_for_window(locator=sk_locator.CART_TV_TITLE,
                                    text=sk_locator.CART_TV_TITLE_TEXT,
                                    timeout=timeout)
        assert self.scroll_to_and_tap(locator=(
            "xpath", f"//android.widget.TextView[@text='{item}']"))
        assert self.wait_for_window(locator=(
            "id", "ru.sigma.app.debug:id/productNameTextView"),
            text='Товар со свободной ценой', timeout=30)
        return True


