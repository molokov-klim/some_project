# coding: utf-8
import time

from selenium.common import WebDriverException
from core.adb import adb
from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import my_step_info, screenshots

from applications.SigmaCashRegister.sk_num_pad import SigmaAppNumPad


class SigmaAppRefund(SigmaAppNumPad):

    def __init__(self):
        super().__init__()
        self.valid_refund_methods = sk_locator.VALID_REFUND_METHODS
        self.valid_card_cancel_methods = sk_locator.VALID_CARD_CANCEL_METHODS
        self.refund_methods = {
            'cash': self.process_refund_receipt_cash,
            'card': self.process_refund_receipt_card,
            'combo': self.process_refund_receipt_combo,
        }
        self.card_cancel_methods = sk_locator.CARD_CANCEL_METHODS_LOCATORS

    @my_step_info("Возврат последнего чека")
    @screenshots()
    def refund_last_receipt(self, refund_method: str, card_cancel_method: str = 'cancel'):
        """
        Метод производит возврат последнего чека.
        Ожидает окно Чеки и возвраты, отдает окно Чеки и возвраты.
        """
        assert refund_method in self.valid_refund_methods
        assert card_cancel_method in self.valid_card_cancel_methods
        receipt_locator = self.find_last_receipt()
        assert self.tap_to_element(receipt_locator)
        assert self.refund_methods[refund_method](card_cancel_method=card_cancel_method)
        return True

    def find_last_receipt(self) -> tuple:
        """
        Метод возвращает локатор первого (верхнего) отображаемого чека.
        Ожидает окно Чеки и возвраты, отдает окно Чеки и возвраты.
        """
        try:
            self.logger.debug("find_last_receipt()")
            receipts = self.extract_receipts()
            key_of_last = list(receipts.keys())[0]
            return ("xpath", f"//android.widget.TextView[contains(@text,'{str(key_of_last)}')]")
        except Exception as e:
            self.logger.error("Не удалось найти чек: {}".format(e))

    def extract_receipts(self):
        """
        Метод находит все отображаемые в текущем окне чеки.
        Возвращает словарь, где ключ - номер чека, значение - сумма чека.
        Ожидает окно Чеки и возвраты, отдает окно Чеки и возвраты.
        """
        self.logger.debug("Извлечение чеков")
        receipts = {}
        cards = self.get_elements('android.view.ViewGroup')
        for card in cards:
            try:
                number = card.find_element(sk_locator.RECEIPTS_AND_RETURNS_ATTR_TV_NUMBER[0],
                                           sk_locator.RECEIPTS_AND_RETURNS_ATTR_TV_NUMBER[1]).text
                number = number.replace('№ ', '')
                amount = card.find_element(sk_locator.RECEIPTS_AND_RETURNS_ATTR_TV_SUM[0],
                                           sk_locator.RECEIPTS_AND_RETURNS_ATTR_TV_SUM[1]).text
                amount = amount.replace(',', '.').replace(' ₽', '')
                receipts[number] = amount
            except WebDriverException:
                continue
        self.logger.debug(receipts)
        return receipts

    def process_refund_receipt_cash(self, card_cancel_method: str = ''):
        """
        Метод производит возврат чека, оплаченного наличными.
        Ожидает окно - чек. Отдает окно - чеки и возвраты
        """
        self.logger.info("Производим возврат")
        assert self.wait_for_window(locator=sk_locator.RECEIPT_TV_TITLE,
                                    text=sk_locator.RECEIPT_TV_TITLE_TEXT,
                                    timeout=5)
        assert self.tap_to_element(locator=sk_locator.RECEIPT_BTN_MAKE_REFUND)
        assert self.wait_for_window(locator=sk_locator.REFUND_TV_TITLE,
                                    text=sk_locator.REFUND_TV_TITLE_TEXT,
                                    timeout=5)
        assert self.tap_to_element(locator=sk_locator.REFUND_BTN_SELECT_ALL)
        assert self.tap_to_element(locator=sk_locator.REFUND_BTN_NEXT)
        assert self.wait_for_window(locator=sk_locator.REFUND_COMMENT_TV_TITLE,
                                    text=sk_locator.REFUND_COMMENT_TV_TITLE_TEXT,
                                    timeout=5)
        assert self.tap_to_element(locator=sk_locator.REFUND_COMMENT_INPUT_STRING)
        time.sleep(1)
        adb.input_by_virtual_keyboard(key="auto", keyboard=sk_locator.PT5_VIRTUAL_KEYBOARD_QWERTY)
        adb.tap(*sk_locator.PT5_VIRTUAL_KEYBOARD_QWERTY["OK"])
        assert self.tap_to_element(locator=sk_locator.REFUND_COMMENT_BTN_NEXT)
        assert self.wait_until_element_will_not_displayed(locator=sk_locator.REFUND_EXECUTION_IMG_PROGRESS,
                                                          timeout=60)
        assert self.wait_for_window(locator=sk_locator.REFUND_EXECUTION_TV_MESSAGE,
                                    text=sk_locator.REFUND_EXECUTION_TV_MESSAGE_SUCCESS_TEXT,
                                    timeout=10)
        assert self.tap_to_element(locator=sk_locator.REFUND_EXECUTION_BTN_NEXT)
        assert self.wait_for_window(locator=sk_locator.RECEIPT_TV_ALREADY_REFUND,
                                    text=sk_locator.RECEIPT_TV_ALREADY_REFUND_TEXT,
                                    timeout=5)
        assert self.tap_to_element(locator=sk_locator.RECEIPT_BTN_ALREADY_REFUND_OPEN)
        assert self.wait_for_window(locator=sk_locator.RECEIPT_REFUNDED_TV_TITLE,
                                    text=sk_locator.RECEIPT_REFUNDED_TV_TITLE_TEXT,
                                    timeout=3)
        assert self.tap_to_element(locator=sk_locator.RECEIPT_REFUNDED_BTN_ALREADY_REFUND_OPEN)
        assert self.wait_for_window(locator=sk_locator.RECEIPT_TV_ALREADY_REFUND,
                                    text=sk_locator.RECEIPT_TV_ALREADY_REFUND_TEXT,
                                    timeout=5)
        assert self.tap_to_element(locator=sk_locator.RECEIPT_BTN_BACK)
        self.logger.info("Возврат чека оформлен")
        return True

    def process_refund_receipt_card(self, card_cancel_method: str = 'cancel'):
        """
        Метод производит возврат чека, оплаченного картой.
        Ожидает окно - чек. Отдает окно - чеки и возвраты
        """
        self.logger.info("Производим возврат")
        assert self.wait_for_window(locator=sk_locator.RECEIPT_TV_TITLE,
                                    text=sk_locator.RECEIPT_TV_TITLE_TEXT,
                                    timeout=5)
        assert self.tap_to_element(locator=sk_locator.RECEIPT_BTN_MAKE_REFUND)
        assert self.wait_for_window(locator=sk_locator.REFUND_MODAL_ATOL_PAY_OPTIONS_TV_TITLE,
                                    text=sk_locator.REFUND_MODAL_ATOL_PAY_OPTIONS_TV_TITLE_TEXT,
                                    timeout=3)
        assert self.tap_to_element(locator=self.card_cancel_methods[card_cancel_method])
        time.sleep(10)  # TODO сделать обработку промежуточных окон
        assert self.wait_for_window(locator=sk_locator.REFUND_ATOL_PAY_SUCCESS_TV_TITLE,
                                    text=sk_locator.REFUND_ATOL_PAY_SUCCESS_TV_TITLE_TEXT,
                                    timeout=30)
        assert self.tap_to_element(locator=sk_locator.REFUND_ATOL_PAY_SUCCESS_BTN_CONTINUE, timeout=30)
        assert self.wait_for_element(locator=sk_locator.REFUND_ATOL_PAY_SUCCESS_BTN_CLOSE, timeout=30)
        assert self.tap_to_element(locator=sk_locator.REFUND_ATOL_PAY_SUCCESS_BTN_CLOSE)
        assert self.wait_for_window(locator=sk_locator.RECEIPT_TV_ALREADY_REFUND,
                                    text=sk_locator.RECEIPT_TV_ALREADY_REFUND_TEXT,
                                    timeout=5)
        assert self.tap_to_element(locator=sk_locator.RECEIPT_BTN_ALREADY_REFUND_OPEN)
        assert self.wait_for_window(locator=sk_locator.RECEIPT_REFUNDED_TV_TITLE,
                                    text=sk_locator.RECEIPT_REFUNDED_TV_TITLE_TEXT,
                                    timeout=50)
        assert self.tap_to_element(locator=sk_locator.RECEIPT_REFUNDED_BTN_ALREADY_REFUND_OPEN)
        assert self.wait_for_window(locator=sk_locator.RECEIPT_TV_ALREADY_REFUND,
                                    text=sk_locator.RECEIPT_TV_ALREADY_REFUND_TEXT,
                                    timeout=10)
        assert self.tap_to_element(locator=sk_locator.RECEIPT_BTN_BACK)
        self.logger.info("Возврат чека оформлен")
        return True

    def process_refund_receipt_combo(self, card_cancel_method: str = 'cancel'):
        """
        Метод производит возврат чека, оплаченного комбооплатой.
        Ожидает окно - чек. Отдает окно - чеки и возвраты
        """

        self.logger.info("Производим возврат")
        assert self.wait_for_window(locator=sk_locator.RECEIPT_TV_TITLE,
                                    text=sk_locator.RECEIPT_TV_TITLE_TEXT,
                                    timeout=5)
        assert self.tap_to_element(locator=sk_locator.RECEIPT_BTN_MAKE_REFUND)
        assert self.wait_for_window(locator=sk_locator.REFUND_MODAL_ATOL_PAY_OPTIONS_TV_TITLE,
                                    text=sk_locator.REFUND_MODAL_ATOL_PAY_OPTIONS_TV_TITLE_TEXT,
                                    timeout=3)
        assert self.tap_to_element(locator=self.card_cancel_methods[card_cancel_method])
        if self.wait_for_window(locator=sk_locator.REFUND_TV_TITLE,
                                text=sk_locator.REFUND_TV_TITLE_TEXT,
                                timeout=3):
            assert self.tap_to_element(locator=sk_locator.REFUND_BTN_SELECT_ALL)
            assert self.tap_to_element(locator=sk_locator.REFUND_BTN_NEXT)
            assert self.wait_for_window(locator=sk_locator.REFUND_COMMENT_TV_TITLE,
                                        text=sk_locator.REFUND_COMMENT_TV_TITLE_TEXT,
                                        timeout=5)
            assert self.tap_to_element(locator=sk_locator.REFUND_COMMENT_INPUT_STRING)
            time.sleep(1)
            adb.input_by_virtual_keyboard(key="auto", keyboard=sk_locator.PT5_VIRTUAL_KEYBOARD_QWERTY)
            adb.tap(*sk_locator.PT5_VIRTUAL_KEYBOARD_QWERTY["OK"])
            assert self.tap_to_element(locator=sk_locator.REFUND_COMMENT_BTN_NEXT)
            assert self.input_by_num_pad(number='0,01', num_pad=sk_locator.PAY_CASH_NUM_PAD)
            assert self.tap_to_element(locator=sk_locator.PAY_CASH_BTN_NEXT)
            assert self.wait_for_element(locator=sk_locator.REFUND_TOAST_FORBIDDEN)
        assert self.tap_to_element(locator=sk_locator.PAY_CASH_NUM_PAD['keep_change'])
        assert self.tap_to_element(locator=sk_locator.PAY_CASH_BTN_NEXT)
        time.sleep(10)  # TODO сделать обработку промежуточных окон
        assert self.wait_for_window(locator=sk_locator.REFUND_ATOL_PAY_SUCCESS_TV_TITLE,
                                    text=sk_locator.REFUND_ATOL_PAY_SUCCESS_TV_TITLE_TEXT,
                                    timeout=30)
        assert self.tap_to_element(locator=sk_locator.REFUND_ATOL_PAY_SUCCESS_BTN_CONTINUE)
        assert self.wait_for_element(locator=sk_locator.REFUND_ATOL_PAY_SUCCESS_BTN_CLOSE, timeout=30)
        assert self.tap_to_element(locator=sk_locator.REFUND_ATOL_PAY_SUCCESS_BTN_CLOSE)
        assert self.wait_for_window(locator=sk_locator.RECEIPT_TV_ALREADY_REFUND,
                                    text=sk_locator.RECEIPT_TV_ALREADY_REFUND_TEXT,
                                    timeout=5)
        assert self.tap_to_element(locator=sk_locator.RECEIPT_BTN_ALREADY_REFUND_OPEN)
        assert self.wait_for_window(locator=sk_locator.RECEIPT_REFUNDED_TV_TITLE,
                                    text=sk_locator.RECEIPT_REFUNDED_TV_TITLE_TEXT,
                                    timeout=3)
        assert self.tap_to_element(locator=sk_locator.RECEIPT_REFUNDED_BTN_ALREADY_REFUND_OPEN)
        assert self.wait_for_window(locator=sk_locator.RECEIPT_TV_ALREADY_REFUND,
                                    text=sk_locator.RECEIPT_TV_ALREADY_REFUND_TEXT,
                                    timeout=5)
        assert self.tap_to_element(locator=sk_locator.RECEIPT_BTN_BACK)
        self.logger.info("Возврат чека оформлен")
        return True

