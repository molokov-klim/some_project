# coding: utf-8
import time

import allure

from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import my_step_info, screenshots

from applications.SigmaCashRegister.sk_num_pad import SigmaAppNumPad
from applications.SigmaCashRegister.sk_transfer import SigmaAppTransfer


class SigmaAppCashTransactions(SigmaAppNumPad, SigmaAppTransfer):

    def __init__(self):
        super().__init__()

    @my_step_info("Внесение")
    @screenshots()
    def deposit_cash(self, amount: int = 50):
        """
        Метод внесения наличных в кассу.
        Ожидает главное окно кассовые операции, отдает главное окно кассовые операции.
        corr_amount: сумма внесения
        """
        assert int(amount) > 0
        assert self.scroll_to_and_tap(locator=sk_locator.CASH_TRANSACTIONS_BTN_ADD_CASH)
        assert self.wait_for_numpad(timeout=10)
        assert self.input_by_num_pad(number=str(amount), num_pad=sk_locator.SIMPLE_NUM_PAD)
        assert self.tap_to_element(locator=sk_locator.ADD_CASH_NEXT)
        assert self.wait_for_window(locator=sk_locator.CASH_TRANSACTIONS_TV_TITLE,
                                    text=sk_locator.CASH_TRANSACTIONS_TV_TITLE_TEXT,
                                    timeout=30)
        time.sleep(5)
        return True

    @my_step_info("Изъятие")
    @screenshots()
    def withdraw_cash(self, amount: int = 25):
        """
        Метод изъятия наличных из кассы.
        Ожидает главное окно кассовые операции, отдает главное окно кассовые операции.
        corr_amount: сумма изъятия
        """
        self.logger.info(f"Изъятие: {amount}")
        assert int(amount) > 0
        assert self.scroll_to_and_tap(locator=sk_locator.CASH_TRANSACTIONS_BTN_REMOVE_CASH)
        assert self.wait_for_numpad(timeout=10)
        assert self.input_by_num_pad(number=str(amount), num_pad=sk_locator.SIMPLE_NUM_PAD)
        assert self.tap_to_element(locator=sk_locator.REMOVE_CASH_NEXT)
        assert self.wait_for_window(locator=sk_locator.CASH_TRANSACTIONS_TV_TITLE,
                                    text=sk_locator.CASH_TRANSACTIONS_TV_TITLE_TEXT,
                                    timeout=30)
        time.sleep(5)
        self.logger.info("Успешное изъятие")
        return True

    def make_x_report(self):
        """
        Метод печати X-отчета.
        Ожидает главное окно кассовые операции, отдает главное окно кассовые операции.
        """
        assert self.scroll_to_and_tap(locator=sk_locator.CASH_TRANSACTIONS_BTN_MAKE_X_REPORT)
        time.sleep(3)
        return True


    def make_calc_report(self):
        """
        Метод печати отчета о состоянии расчетов.
        Ожидает главное окно кассовые операции, отдает главное окно кассовые операции.
        """
        assert self.scroll_to_and_tap(locator=sk_locator.CASH_TRANSACTIONS_BTN_MAKE_CALCULATION_REPORT)
        time.sleep(3)
        return True

    @allure.step("Сравнение итогового значения денег в кассе и начального значения с "
                 "проведенными операциями внесения и изъятия")
    def deposit_withdraw_compare(self, after_withdraw_amount, start_amount, deposit, withdraw):
        """
        Метод сравнивает ожидаемую сумму наличных в кассе с фактической после операций внесения и изъятия
        """
        assert float(after_withdraw_amount) == start_amount + deposit - withdraw
        return True
