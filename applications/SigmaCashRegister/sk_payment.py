# coding: utf-8
import time

from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import my_step_info, screenshots
from core.operations import operations as op

from applications.SigmaCashRegister.sk_num_pad import SigmaAppNumPad
from applications.SigmaCashRegister.sk_wait import SigmaAppWait
from applications.SigmaCashRegister.sk_modal import SigmaAppModal
from applications.SigmaCashRegister.sk_get import SigmaAppGet


class SigmaAppPayment(SigmaAppNumPad, SigmaAppWait, SigmaAppModal, SigmaAppGet):
    def __init__(self):
        super().__init__()
        self.valid_cash_methods = sk_locator.VALID_CASH_METHODS
        self.cash_methods = {
            'keep_change': self.receive_cash_payment_keep_change,   # прием наличных кнопкой "без сдачи"
            'banknote_buttons': self.receive_cash_payment_banknote_buttons,     # прием наличных кнопками банкнот
            'digit_buttons': self.receive_cash_payment_digits,      # прием наличных цифровыми кнопками
        }
        self.combo_methods = {
            'banknote_buttons': self.receive_combo_payment_banknote_buttons,     # прием наличных кнопками банкнот
            'digit_buttons': self.receive_combo_payment_digits,     # прием наличных цифровыми кнопками
        }
        self.banknote_buttons = sk_locator.BANKNOTE_BUTTONS

    @my_step_info("Обработка оплаты наличными")
    @screenshots()
    def process_one_receipt_cash(self, cash_method: str = 'keep_change', amount: str = '0'):
        """
        Метод производит оплату товара наличными.
        Ожидает пин пад оплаты наличными, отдает главное окно
        """
        assert cash_method in self.valid_cash_methods
        assert self.cash_methods[cash_method](amount)
        return True

    def receive_cash_payment_banknote_buttons(self, amount: str = '9800'):
        """
        Метод приема оплаты наличными кнопками банкнот.
        Ожидает пин пад оплаты наличными
        corr_amount: сумма оплаты
        """
        count_banknotes = op.count_currency_numbers(int(amount))
        amount = float(int(int(amount) / 100) * 100)
        for banknote in self.banknote_buttons:
            banknotes_quantity = count_banknotes[self.banknote_buttons.index(banknote)]
            for i in range(banknotes_quantity):
                assert self.tap_to_element(locator=sk_locator.PAY_CASH_NUM_PAD[banknote])
        assert self.tap_to_element(sk_locator.PAY_CASH_BTN_NEXT)
        assert self.wait_for_element(locator=sk_locator.PAY_IMG_PROGRESS)
        assert self.wait_until_element_will_not_displayed(locator=sk_locator.PAY_IMG_PROGRESS, timeout=60)
        assert self.wait_for_window(locator=sk_locator.PAY_CASH_SUCCESS_TV_TITLE,
                                    text=sk_locator.PAY_CASH_SUCCESS_TV_TITLE_TEXT,
                                    timeout=30)
        assert self.check_change(input_amount=str(amount))
        assert self.tap_to_element(locator=sk_locator.PAY_CASH_SUCCESS_BTN_NEXT)
        assert self.wait_until_element_will_not_displayed(locator=sk_locator.PAY_IMG_PROGRESS, timeout=60)
        return True

    def receive_cash_payment_keep_change(self, amount=None):
        """
        Метод приема оплаты наличными кнопкой "Без сдачи".
        Ожидает пин пад оплаты наличными
        """
        assert self.tap_to_element(locator=sk_locator.PAY_CASH_NUM_PAD['keep_change'])
        assert self.tap_to_element(sk_locator.PAY_CASH_BTN_NEXT)
        if self.wait_for_element(locator=sk_locator.PAY_IMG_PROGRESS):
            assert self.wait_until_element_will_not_displayed(locator=sk_locator.PAY_IMG_PROGRESS, timeout=60)
        assert self.wait_for_window(locator=sk_locator.PAY_CASH_SUCCESS_TV_MESSAGE,
                                    text=sk_locator.PAY_CASH_SUCCESS_TV_MESSAGE_TEXT,
                                    timeout=50)
        assert self.check_change(input_amount=amount)
        self.tap_to_element(locator=sk_locator.PAY_CASH_SUCCESS_BTN_NEXT)
        assert self.wait_until_element_will_not_displayed(locator=sk_locator.PAY_IMG_PROGRESS, timeout=60)
        return True

    def receive_cash_payment_digits(self, amount: str = '987,6'):
        """
        Метод приема оплаты наличными цифровыми кнопками.
        Ожидает пин пад оплаты наличными
        corr_amount: сумма оплаты
        """
        amount = amount.replace('.', ',')
        assert self.input_by_num_pad(number=amount, num_pad=sk_locator.PAY_CASH_NUM_PAD)
        assert self.tap_to_element(sk_locator.PAY_CASH_BTN_NEXT)
        if self.wait_for_element(locator=sk_locator.PAY_IMG_PROGRESS):
            assert self.wait_until_element_will_not_displayed(locator=sk_locator.PAY_IMG_PROGRESS, timeout=60)
        assert self.wait_for_window(locator=sk_locator.PAY_CASH_SUCCESS_TV_TITLE,
                                    text=sk_locator.PAY_CASH_SUCCESS_TV_TITLE_TEXT,
                                    timeout=30)
        assert self.check_change(input_amount=amount)
        self.tap_to_element(locator=sk_locator.PAY_CASH_SUCCESS_BTN_NEXT)
        assert self.wait_until_element_will_not_displayed(locator=sk_locator.PAY_IMG_PROGRESS, timeout=60)
        return True

    def check_change(self, input_amount: str):
        """
        Метод проверяет соответствие сдачи.
        Ожидает окно успешной оплаты наличными.
        """
        input_amount = float(input_amount)
        delta = self.get_element_attribute(locator=sk_locator.PAY_CASH_SUCCESS_TV_CHANGE, attr='text')
        if delta == 'Без сдачи':
            return True
        delta = float(delta.replace(',', '.').replace(' ₽', '').replace(' ', ''))

        receipt_amount = self.get_element_attribute(locator=sk_locator.PAY_CASH_SUCCESS_TV_RECEIPT_AMOUNT, attr='text')
        receipt_amount = float(receipt_amount.replace(',', '.').replace(' ₽', ''))

        actual_delta = input_amount - receipt_amount
        self.logger.debug(f"{input_amount=}, {receipt_amount=}, {delta=}, {actual_delta=}")
        assert float(delta) == float(actual_delta)
        return True

    @my_step_info("Обработка оплаты картой")
    @screenshots()
    def process_one_receipt_card(self, timeout=60):
        """
        Метод обрабатывающий окна оплаты картой.
        Ожидает окно оплаты картой.
        """
        end_time = time.time() + timeout
        while not self.is_window(locator=sk_locator.PAY_CARD_SUCCESS_1_TV_STATUS,
                                 text=sk_locator.PAY_CARD_SUCCESS_1_TV_STATUS_TEXT):
            assert not self.is_window_displayed(locator=sk_locator.PAY_CARD_TIMEOUT_TV_STATUS,
                                                text=sk_locator.PAY_CARD_TIMEOUT_TV_STATUS_TEXT)
            if time.time() > end_time:
                self.logger.error("Не получена оплата по карте")
                assert False
            time.sleep(1)
        assert self.tap_to_element(locator=sk_locator.PAY_CARD_SUCCESS_1_BTN_CONTINUE)
        assert self.wait_until_element_will_not_displayed(locator=sk_locator.PAY_CARD_SUCCESS_2_IMG_PROGRESS,
                                                          timeout=60)
        assert self.wait_for_window(locator=sk_locator.PAY_CARD_SUCCESS_3_TV_STATUS,
                                    text=sk_locator.PAY_CARD_SUCCESS_3_TV_STATUS_TEXT,
                                    timeout=3)
        if not self.wait_for_main_window_goods(timeout=3):
            assert self.tap_to_element(locator=sk_locator.MAIN_HEADER_BTN_BACK)
        return True

    @my_step_info("Обработка комбооплаты")
    @screenshots()
    def process_one_receipt_combo(self, cash_method: str = 'keep_change', amount_cash: str = '0'):
        """
        Метод производящий комбо оплату товара.
        Ожидает окно первого шага комбооплаты (прием наличных)
        """
        assert self.process_modal_combo()
        assert cash_method in self.valid_cash_methods
        assert self.combo_methods[cash_method](amount_cash)
        return True

    def receive_combo_payment_banknote_buttons(self, amount: str = '9800'):
        """
        Метод приема комбо оплаты шаг 1 "Наличные".
        Принимает оплату кнопками банкнот.
        corr_amount: сумма оплаты
        """
        required_amount = self.get_required_amount()
        count_banknotes = op.count_currency_numbers(int(amount))
        amount = float(int(int(amount) / 100) * 100)
        for banknote in self.banknote_buttons:
            banknotes_quantity = count_banknotes[self.banknote_buttons.index(banknote)]
            for i in range(banknotes_quantity):
                assert self.tap_to_element(locator=sk_locator.PAY_CASH_NUM_PAD[banknote])
        assert self.tap_to_element(sk_locator.PAY_CASH_BTN_NEXT)
        if amount > required_amount:
            assert self.wait_for_element(locator=sk_locator.PAY_IMG_PROGRESS)
            assert self.wait_until_element_will_not_displayed(locator=sk_locator.PAY_IMG_PROGRESS, timeout=60)
            assert self.wait_for_window(locator=sk_locator.PAY_CASH_SUCCESS_TV_TITLE,
                                        text=sk_locator.PAY_CASH_SUCCESS_TV_TITLE_TEXT,
                                        timeout=30)
            assert self.check_change(input_amount=str(amount))
            assert self.wait_until_element_will_not_displayed(locator=sk_locator.PAY_IMG_PROGRESS, timeout=60)
            assert self.tap_to_element(locator=sk_locator.PAY_CASH_SUCCESS_BTN_NEXT)
        else:
            self.receive_combo_payment_card(required_amount=required_amount, paid_amount=amount)
        return True

    def receive_combo_payment_digits(self, amount: float = 1000.0):
        """
        Метод приема комбо оплаты шаг 1 "Наличные".
        Принимает оплату цифровыми кнопками.
        corr_amount: сумма оплаты
        """
        required_amount = self.get_required_amount()
        amount = str(amount).replace('.', ',')
        assert self.input_by_num_pad(number=amount, num_pad=sk_locator.PAY_CASH_NUM_PAD)
        assert self.tap_to_element(sk_locator.PAY_CASH_BTN_NEXT)
        if float(amount.replace(',', '.')) > required_amount:
            assert self.wait_for_window(locator=sk_locator.PAY_CASH_SUCCESS_TV_TITLE,
                                        text=sk_locator.PAY_CASH_SUCCESS_TV_TITLE_TEXT,
                                        timeout=30)
            assert self.check_change(input_amount=amount)
            assert self.wait_until_element_will_not_displayed(locator=sk_locator.PAY_IMG_PROGRESS, timeout=60)
            assert self.tap_to_element(locator=sk_locator.PAY_CASH_SUCCESS_BTN_NEXT)
            self.logger.debug(f"receive_cash_payment_digits() success")
        else:
            self.receive_combo_payment_card(required_amount=required_amount, paid_amount=amount)
        return True

    def receive_combo_payment_card(self, required_amount, paid_amount):
        """
        Метод приема комбо оплаты шаг 2 "Оплата картой".
        Перед приемом оплаты проверяет корректность оставшейся суммы к оплате картой.
        required_amount: общая сумма к оплате
        paid_amount: сумма оплаченная наличными
        """
        self.wait_for_element(locator=sk_locator.PAY_CARD_TV_AMOUNT)
        card_amount = self.get_element_attribute(locator=sk_locator.PAY_CARD_TV_AMOUNT, attr='text')
        assert op.str_to_float(card_amount) == op.str_to_float(required_amount) - op.str_to_float(paid_amount)
        self.logger.info("Сумма по карте совпала")
        while not self.is_window(locator=sk_locator.PAY_CARD_SUCCESS_1_TV_STATUS,
                                 text=sk_locator.PAY_CARD_SUCCESS_1_TV_STATUS_TEXT):
            assert not self.is_window_displayed(locator=sk_locator.PAY_CARD_TIMEOUT_TV_STATUS,
                                                text=sk_locator.PAY_CARD_TIMEOUT_TV_STATUS_TEXT)
            time.sleep(1)
        assert self.tap_to_element(locator=sk_locator.PAY_CARD_SUCCESS_1_BTN_CONTINUE)
        assert self.wait_until_element_will_not_displayed(locator=sk_locator.PAY_CARD_SUCCESS_2_IMG_PROGRESS)
        assert self.wait_for_window(locator=sk_locator.PAY_CARD_SUCCESS_3_TV_STATUS,
                                    text=sk_locator.PAY_CARD_SUCCESS_3_TV_STATUS_TEXT,
                                    timeout=60)
        if not self.wait_for_main_window_goods(timeout=3):
            assert self.tap_to_element(locator=sk_locator.MAIN_HEADER_BTN_BACK)
        return True

    @my_step_info("Проверка неактивности кнопки \"принять\"")
    @screenshots()
    def is_pay_btn_inactive(self, amount: str = '0,01'):
        """
        Проверка неактивности кнопки "принять" на экране оплаты наличными при недостаточной сумме.
        Ожидает окно оплаты наличными, отдает окно оплаты наличными
        """
        self.logger.debug("is_pay_btn_inactive()")
        assert self.wait_for_window(locator=sk_locator.PAY_CASH_TV_TITLE, text=sk_locator.PAY_CASH_TV_TITLE_TEXT)
        assert self.input_by_num_pad(number=amount, num_pad=sk_locator.PAY_CASH_NUM_PAD)
        assert not bool(self.is_element_active(locator=sk_locator.PAY_CASH_BTN_NEXT))
        for i in range(len(amount)):
            assert self.tap_to_element(sk_locator.PAY_CASH_NUM_PAD["backspace"])
        assert self.get_element_attribute(locator=sk_locator.PAY_CASH_TV_AMOUNT_PAID, attr='text') == '0 ₽'
        self.logger.info("Кнопка оплаты неактивна при недостаточной сумме")
        return True
