# coding: utf-8

from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import my_step_info

from core.appium.AppiumPage.appium_page import AppiumPage


class SigmaAppWindow(AppiumPage):

    def __init__(self):
        super().__init__()

    def process_many_receipts(self):
        """
        Метод обработки окна "выбор чека".
        Выбирает чек системы налогообложения из словаря SNO в локаторах
        """
        self.logger.debug("Обработка окна выбора чека")
        assert self.wait_until_element_will_not_displayed(locator=sk_locator.CART_BTN_ORDER_TITLE)
        for locator in sk_locator.SNO:
            if not self.is_element_active(locator=locator):
                continue
            assert self.scroll_to_and_tap(locator=locator)
        return True


