# coding: utf-8
import time

from consts.locators import sigma_kassa_locators as sk_locator
from applications.SigmaCashRegister.sk_window import SigmaAppWindow
from core.decorators.decorators import my_step_info, screenshots

from core.adb import adb


class SigmaAppModal(SigmaAppWindow):
    def __init__(self):
        super().__init__()

        self.valid_1054 = sk_locator.VALID_1054
        self.locator_1054 = sk_locator.LOCATORS_1054

    def process_modal_combo(self):
        """
        Метод обработки модального окна "Комбооплата"
        """
        if self.wait_for_window(locator=sk_locator.PAY_COMBO_MODAL_TV_TITLE,
                                text=sk_locator.PAY_COMBO_MODAL_TV_TITLE_TEXT,
                                timeout=3):
            assert self.tap_to_element(locator=sk_locator.PAY_COMBO_MODAL_BTN_DONT_SHOW)
            assert self.wait_for_window(locator=sk_locator.PAY_COMBO_STEP_1_TV_TITLE,
                                        text=sk_locator.PAY_COMBO_STEP_1_TV_TITLE_TEXT,
                                        timeout=3)
        return True

    @my_step_info("Добавление товара в корзину \"Признак расчета приход/расход\"")
    @screenshots()
    def process_modal_1054(self, tag_1054):
        """
        Метод обработки модального окна "Признак расчета приход/расход".
        tag_1054: 'income' или 'outcome'
        """
        assert tag_1054 in self.valid_1054
        if self.wait_for_window(locator=sk_locator.MODAL_CHOOSE_1054_TV_TITLE,
                                text=sk_locator.MODAL_CHOOSE_1054_TV_TITLE_TEXT,
                                timeout=2):
            assert self.tap_to_element(self.locator_1054[tag_1054])
        return True

    @my_step_info("Обработки модального окна \"Касса создаст несколько чеков\"")
    @screenshots()
    def process_modal_many_receipts(self):
        """
        Метод обработки модального окна "Касса создаст несколько чеков"
        """
        time.sleep(1)
        if self.wait_for_window(locator=sk_locator.MODAL_CART_ORDER_MANY_RECEIPTS_TV_TITLE,
                                text=sk_locator.MODAL_CART_ORDER_MANY_RECEIPTS_TV_TITLE_TEXT,
                                timeout=1):
            assert self.tap_to_element(sk_locator.MODAL_CART_ORDER_MANY_RECEIPTS_BTN_OK)
            assert self.process_many_receipts()
        return True

    @my_step_info("Установка даты в модальном окне установки даты")
    @screenshots()
    def modal_set_date(self, date, timeout=300):
        """
        Метод установки даты в модальном окне установки даты
        """
        time.sleep(2)
        start_time = time.time()
        day, month, year = date.split(".")
        if len(year) == 2:
            year = "20" + year
        while time.time() - start_time < timeout:
            present_day = self.get_element_attribute(locator=sk_locator.MODAL_DATE_TV_DAY, attr='text')
            present_month = self.get_element_attribute(locator=sk_locator.MODAL_DATE_TV_MONTH, attr='text')
            present_year = self.get_element_attribute(locator=sk_locator.MODAL_DATE_TV_YEAR, attr='text')
            if int(present_day) == int(day) and int(sk_locator.MONTHS[present_month]) == int(month) and int(present_year) == int(year):
                assert self.tap_to_element(locator=sk_locator.MODAL_DATE_BTN_OK)
                return True
            if int(present_day) > int(day):
                self.logger.debug("int(present_day) > int(day)")
                self.logger.debug(f"{present_day=}, {day=}")
                start_x = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_previous"][0]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_previous"][2])) / 2
                start_y = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_previous"][1]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_previous"][3])) / 2
                end_x = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_present"][0]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_present"][2])) / 2
                end_y = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_present"][1]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_present"][3])) / 2
                adb.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y)
            if int(present_day) < int(day):
                self.logger.debug("int(present_day) < int(day)")
                self.logger.debug(f"{present_day=}, {day=}")
                start_x = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_future"][0]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_future"][2])) / 2
                start_y = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_future"][1]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_future"][3])) / 2
                end_x = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_present"][0]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_present"][2])) / 2
                end_y = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_present"][1]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["day_present"][3])) / 2
                adb.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y)
            if int(sk_locator.MONTHS[present_month]) > int(month):
                self.logger.debug("int(sk_locator.MONTHS[present_month]) > int(month)")
                self.logger.debug(f"{sk_locator.MONTHS[present_month]=}, {month=}")
                start_x = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_previous"][0]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_previous"][2])) / 2
                start_y = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_previous"][1]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_previous"][3])) / 2
                end_x = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_present"][0]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_present"][2])) / 2
                end_y = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_present"][1]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_present"][3])) / 2
                adb.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y)
            if int(sk_locator.MONTHS[present_month]) < int(month):
                self.logger.debug("int(sk_locator.MONTHS[present_month]) < int(month)")
                self.logger.debug(f"{sk_locator.MONTHS[present_month]=}, {month=}")
                start_x = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_future"][0]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_future"][2])) / 2
                start_y = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_future"][1]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_future"][3])) / 2
                end_x = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_present"][0]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_present"][2])) / 2
                end_y = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_present"][1]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["month_present"][3])) / 2
                adb.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y)
            if int(present_year) > int(year):
                self.logger.debug("int(present_year) > int(year)")
                self.logger.debug(f"{present_year=}, {year=}")
                start_x = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_previous"][0]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_previous"][2])) / 2
                start_y = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_previous"][1]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_previous"][3])) / 2
                end_x = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_present"][0]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_present"][2])) / 2
                end_y = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_present"][1]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_present"][3])) / 2
                adb.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y)
            if int(present_year) < int(year):
                self.logger.debug("int(present_year) < int(year)")
                self.logger.debug(f"{present_year=}, {year=}")
                start_x = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_future"][0]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_future"][2])) / 2
                start_y = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_future"][1]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_future"][3])) / 2
                end_x = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_present"][0]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_present"][2])) / 2
                end_y = (int(sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_present"][1]) + int(
                    sk_locator.PT5_MODAL_DATE_INPUT_COORD["year_present"][3])) / 2
                adb.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y)
        self.logger.error("Timeout установки даты")
        return False
