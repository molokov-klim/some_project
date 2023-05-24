# coding: utf-8

from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import my_step_info, screenshots

from applications.SigmaCashRegister.sk_num_pad import SigmaAppNumPad
from applications.SigmaCashRegister.sk_transfer import SigmaAppTransfer


class SigmaAppShift(SigmaAppNumPad, SigmaAppTransfer):
    def __init__(self):
        super().__init__()

    @my_step_info("Открытие смены")
    @screenshots()
    def open_shift(self, cash: str = '0', timeout: int = 2):
        """
        Метод открытия смены.
        Проверяет состояния: окно открытия смены, основное окно, смена открыта более 24 часов, смена на ФР открыта.
        Для любого из указанных состояний открывает смену, предварительно закрыв, если необходимо.
        cash: сумма внесения
        timeout: время ожидания
        """
        if not self.open_shift_check_main_window(cash=cash, timeout=timeout):
            if not self.process_open_shift(cash=cash, timeout=timeout):
                if not self.check_close_shift_window_reopen(cash=cash, timeout=timeout):
                    if not self.open_shift_check_long_shift(cash=cash, timeout=timeout):
                        assert self.open_shift_check_FR_already_open(timeout=timeout)
        return True

    def open_shift_check_main_window(self, cash: str = '0', timeout: int = 1):
        """
        Метод закрывает и открывает заново смену, если уже открыта.
        Ожидает главное окно товары, отдает главное окно товары
        cash: сумма внесения
        timeout: время ожидания
        """
        if self.wait_for_window(locator=sk_locator.MAIN_HEADER_TV_TITLE,
                                text=sk_locator.MAIN_HEADER_TV_TITLE_GOODS_TEXT,
                                timeout=timeout):
            if self.close_shift():
                if self.process_open_shift(cash, timeout=timeout):
                    return True
        return False

    def process_open_shift(self, cash: str = '0', timeout: int = 5):
        """
        Метод открывает смену с указанным внесением.
        Ожидает окно открытия смены, отдает главное окно товары
        cash: сумма внесения
        timeout: время ожидания
        """
        assert cash.isnumeric()
        if self.wait_for_numpad(timeout=timeout):
            if int(cash) > 0:
                assert self.input_by_num_pad(number=str(cash), num_pad=sk_locator.NEW_SHIFT_NUM_PAD)
            if self.tap_to_element(sk_locator.NEW_SHIFT_BTN_OPEN_SHIFT):
                if self.wait_until_element_will_not_present(locator=sk_locator.MODAL_NEW_SHIFT_IMG_PROGRESS):
                    return True
        return False

    def check_close_shift_window_reopen(self, cash: str = '0', timeout: int = 1):
        """
        Метод закрывает и открывает смену с указанным внесением.
        Ожидает окно закрытия смены, отдает главное окно товары
        cash: сумма внесения
        timeout: время ожидания
        """
        if self.wait_for_window(locator=sk_locator.CLOSE_SHIFT_TV_TITLE,
                                text=sk_locator.CLOSE_SHIFT_TV_TITLE_TEXT,
                                timeout=timeout):
            if self.close_shift():
                if self.process_open_shift(cash=cash, timeout=timeout):
                    return True
        return False

    def open_shift_check_long_shift(self, cash: str = '0', timeout=5):
        """
        Метод закрывает и открывает смену с указанным внесением.
        Ожидает окно "смена открыта более 24 часов", отдает главное окно товары
        cash: сумма внесения
        timeout: время ожидания
        """
        if self.wait_for_window(locator=sk_locator.LONG_SHIFT_MODAL_TV_TITLE,
                                text=sk_locator.LONG_SHIFT_MODAL_TV_TITLE_TEXT,
                                timeout=timeout):
            if self.tap_to_element(sk_locator.LONG_SHIFT_MODAL_BTN_OK):
                if self.close_shift():
                    if self.process_open_shift(cash=cash, timeout=timeout):
                        return True
        return False

    def open_shift_check_FR_already_open(self, timeout: int = 5):
        """
        Метод обрабатывает модальное окно "смена на ФР уже открыта".
        Ожидает модальное окно "смена на ФР уже открыта", отдает главное окно товары
        timeout: время ожидания
        """
        if self.wait_for_window(locator=sk_locator.MODAL_NEW_SHIFT_FR_HAVE_SHIFT_TV_MAIN,
                                text=sk_locator.MODAL_NEW_SHIFT_FR_HAVE_SHIFT_TV_MAIN_TEXT,
                                timeout=timeout):
            if self.tap_to_element(sk_locator.MODAL_NEW_SHIFT_FR_HAVE_SHIFT_BTN_OK):
                if self.wait_for_main_window_goods():
                    return True
        return False

    @my_step_info("Закрытие смены")
    @screenshots()
    def close_shift(self):
        """
        Метод перемещает в кассовые операции, закрытие смены, закрывает смену и ждет пин пад (новая смена).
        Ожидает главное окно товары, отдает окно новая смена.
        """
        assert self.transfer_to_cash_transaction()
        assert self.tap_to_element(locator=sk_locator.CASH_TRANSACTIONS_BTN_CLOSE_SHIFT)
        assert self.wait_until_element_will_not_displayed(sk_locator.CLOSE_SHIFT_WAIT_IMG_PROGRESS, timeout=60)
        assert self.tap_to_element(locator=sk_locator.CLOSE_SHIFT_BTN_CLOSE_SHIFT)
        assert self.wait_until_element_will_not_displayed(sk_locator.CLOSE_SHIFT_WAIT_IMG_PROGRESS, timeout=60)
        assert self.wait_for_numpad(timeout=30)
        return True

    @my_step_info("Закрытие смены с проверкой отправки ФД")
    @screenshots()
    def close_shift_with_zero_FD(self, timeout: int = 600):
        """
        Метод перемещает в кассовые операции, закрытие смены, ожидает отправки всех ФД,
        закрывает смену и ждет пин пад (новая смена).
        Ожидает главное окно товары, отдает окно новая смена.
        """
        assert self.transfer_to_cash_transaction()
        assert self.tap_to_element(locator=sk_locator.CASH_TRANSACTIONS_BTN_CLOSE_SHIFT)
        assert self.wait_until_element_will_not_displayed(sk_locator.CLOSE_SHIFT_WAIT_IMG_PROGRESS, timeout=60)
        assert self.wait_for_window(locator=sk_locator.CLOSE_SHIFT_TV_NOT_SENT_OFD,
                                    text='0 чеков',
                                    timeout=timeout)
        assert self.tap_to_element(locator=sk_locator.CLOSE_SHIFT_BTN_CLOSE_SHIFT)
        assert self.wait_until_element_will_not_displayed(sk_locator.CLOSE_SHIFT_WAIT_IMG_PROGRESS, timeout=60)
        assert self.wait_for_numpad(timeout=30)
        return True
