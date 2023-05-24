# coding: utf-8

from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import my_step_info, screenshots

from core.appium.AppiumPage.appium_page import AppiumPage


class SigmaAppWait(AppiumPage):
    def __init__(self):
        super().__init__()

    def wait_for_numpad(self, timeout=5):
        """
        Метод ожидания появления пин пада
        timeout: время ожидания
        """
        assert self.wait_until_element_will_enabled(locator=sk_locator.SIMPLE_NUM_PAD['5'], timeout=timeout)
        return True

    @my_step_info("Ожидание основного окна")
    @screenshots()
    def wait_for_main_window_goods(self, timeout=5):
        """
        Метод ожидания "главное окно товары"
        timeout: время ожидания
        """
        assert self.wait_for_window(locator=sk_locator.MAIN_HEADER_TV_TITLE,
                                    text=sk_locator.MAIN_HEADER_TV_TITLE_GOODS_TEXT,
                                    timeout=timeout)
        return True

    @my_step_info("Ожидание окна выбора способа оплаты")
    @screenshots()
    def wait_for_choose_payment_type(self, timeout=5):
        """
        Метод ожидания окна выбора способа оплаты
        timeout: время ожидания
        """
        assert self.wait_for_window(locator=sk_locator.PAYMENT_CHOOSE_TV_TITLE,
                                    text=sk_locator.PAYMENT_CHOOSE_TV_TITLE_TEXT,
                                    timeout=timeout)
        return True

    