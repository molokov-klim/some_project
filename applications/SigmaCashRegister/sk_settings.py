# coding: utf-8
import time

from consts.locators import sigma_kassa_locators as sk_locator
from core.adb import adb
from core.decorators.decorators import my_step_info, screenshots

from applications.SigmaCashRegister.sk_transfer import SigmaAppTransfer


class SigmaAppSettings(SigmaAppTransfer):

    def __init__(self):
        super().__init__()

    @my_step_info("Включение настройки \"использовать полный список признаков расчета\"")
    @screenshots()
    def turn_on_complete_list_settlement(self):
        """
        Метод переходит в правила торговли, ищет и включает настройки \"использовать полный список признаков расчета\".
        Ожидает главное окно товары, отдает главное окно товары.
        """
        assert self.transfer_to_trading_rules()
        assert self.scroll_to(locator=sk_locator.TRADING_RULES_SWITCH_EXPENSES)
        assert self.scroll_to(locator=sk_locator.TRADING_RULES_SWITCH_FULL_1054)
        if self.get_element_attribute(locator=sk_locator.TRADING_RULES_SWITCH_EXPENSES, attr='text') != 'ВКЛ':
            assert self.tap_to_element(locator=sk_locator.TRADING_RULES_SWITCH_FULL_1054)
        assert self.tap_to_element(locator=sk_locator.TRADING_RULES_BTN_BACK)
        assert self.wait_for_window(locator=sk_locator.SETTINGS_TV_TITLE,
                                    text=sk_locator.SETTINGS_TV_TITLE_TEXT,
                                    timeout=3)
        assert self.tap_to_element(locator=sk_locator.SETTINGS_BTN_BACK)
        assert self.wait_for_main_window_goods()
        return True


    @my_step_info("Включение настройки 'Использовать расходы'")
    @screenshots()
    def turn_on_outcome_items(self):
        """
        Метод переходит в правила торговли, ищет и включает расход.
        Ожидает главное окно товары, отдает главное окно товары.
        """
        assert self.transfer_to_trading_rules()
        assert self.scroll_to(locator=sk_locator.TRADING_RULES_SWITCH_EXPENSES)
        if self.get_element_attribute(locator=sk_locator.TRADING_RULES_SWITCH_EXPENSES, attr='text') != 'ВКЛ':
            assert self.scroll_to_and_tap(locator=sk_locator.TRADING_RULES_SWITCH_EXPENSES)
        assert self.tap_to_element(locator=sk_locator.TRADING_RULES_BTN_BACK)
        assert self.wait_for_window(locator=sk_locator.SETTINGS_TV_TITLE,
                                    text=sk_locator.SETTINGS_TV_TITLE_TEXT,
                                    timeout=3)
        assert self.tap_to_element(locator=sk_locator.SETTINGS_BTN_BACK)
        assert self.wait_for_main_window_goods()
        return True

    @my_step_info("Переключение настройки 'Печать чеков при продаже'")
    @screenshots()
    def turn_receipt_printer(self, on: bool = True):
        """
        Метод переходит в принтер чеков и переключает печать чеков при продаже
        Ожидает "главное окно товары", отдает "главное окно товары".
        """
        assert self.transfer_to_receipt_printer()
        if self.get_element_attribute(locator=sk_locator.RECEIPT_PRINTER_SWITCH_PRINT_RECEIPTS,
                                      attr='text') == 'ВЫКЛ' and on:
            self.tap_to_element(locator=sk_locator.RECEIPT_PRINTER_SWITCH_PRINT_RECEIPTS)
        if self.get_element_attribute(locator=sk_locator.RECEIPT_PRINTER_SWITCH_PRINT_RECEIPTS,
                                      attr='text') == 'ВКЛ' and not on:
            self.tap_to_element(locator=sk_locator.RECEIPT_PRINTER_SWITCH_PRINT_RECEIPTS)
        assert self.tap_to_element(locator=sk_locator.RECEIPT_PRINTER_BTN_BACK)
        assert self.tap_to_element(locator=sk_locator.SETTINGS_BTN_BACK)
        assert self.wait_for_main_window_goods()
        return True

    def add_email_electronically_receipt(self, quantity_character_remove: int = 0, email: str = ""):
        """
        Метод переходит в принтер чеков добавляет электронную почту компании
        """
        assert self.transfer_to_receipt_printer()
        assert self.tap_to_element(sk_locator.RECEIPT_PRINTER_ET_EMAIL)
        time.sleep(1)
        for i in range(quantity_character_remove):
            adb.input_keycode(keycode="KEYCODE_DEL")
        assert adb.input_text(text=email)
        assert self.tap_to_element(locator=sk_locator.RECEIPT_PRINTER_BTN_BACK)
        assert self.tap_to_element(locator=sk_locator.SETTINGS_BTN_BACK)
        assert self.wait_for_main_window_goods()
        return True


