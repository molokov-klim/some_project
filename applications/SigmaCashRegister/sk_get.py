# coding: utf-8
import logging

from selenium.common import WebDriverException

from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import my_step_info, screenshots

from core.appium.AppiumPage.appium_page import AppiumPage
from core.operations import operations as op


class SigmaAppGet(AppiumPage):

    def __init__(self):
        super().__init__()

    @my_step_info("Получение суммы наличных в кассе")
    @screenshots()
    def get_cash_in_cashbox(self) -> float:
        """
        Метод возвращает сумму наличных в кассе.
        Ожидает окно кассовых операций
        """
        assert self.scroll_to(locator=sk_locator.CASH_TRANSACTIONS_INCOME_OUTCOME_TV_TITLE)
        attr = self.get_element_attribute(locator=sk_locator.CASH_TRANSACTIONS_TV_CASH_IN_CASHBOX, attr='text')
        assert attr is not None
        self.logger.info(f"В кассе {attr}руб.")
        return op.str_to_float(attr)

    def get_required_amount(self) -> float:
        """
        Метод возвращает сумму к оплате.
        Ожидает окно оплаты наличными
        """
        attr = self.get_element_attribute(locator=sk_locator.PAY_COMBO_STEP_1_TV_AMOUNT_REQUIRED, attr='text')
        assert attr is not None
        return op.str_to_float(attr)

    def get_items_quantity_in_cart(self):
        """
        Метод возваращает количество товаров в корзине
        """
        attr = self.get_element_attribute(locator=sk_locator.MAIN_FOOTER_TV_ORDER_COUNTER, attr='text')
        assert attr is not None
        return attr

    def get_title(self):
        """
        Метод возвращает атрибут text у элемента Title, если он представлен
        """
        try:
            attr = self.get_element_attribute(locator=("id", "ru.sigma.app.debug:id/titleTextView"), attr='text')
        except WebDriverException:
            self.logger.error("Title не найдет")
            return None
        return attr


    def get_page_source(self):
        source = self.driver.page_source
        return source

