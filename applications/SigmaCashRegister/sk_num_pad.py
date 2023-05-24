# coding: utf-8
import time

from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import my_step_info

from core.appium.AppiumPage.appium_page import AppiumPage


class SigmaAppNumPad(AppiumPage):

    def __init__(self):
        super().__init__()

    def input_device_code(self, number: str):
        """
        Метод ввода кода устройства при активации кассы
        number: код устройства
        """
        assert self.wait_for_window(locator=sk_locator.ENTER_DEVICE_CODE_TV_TITLE,
                                    text=sk_locator.ENTER_DEVICE_CODE_TV_TITLE_TEXT)
        assert self.input_by_num_pad(number, sk_locator.ENTER_DEVICE_CODE_NUM_PAD)
        assert self.wait_until_element_will_not_present(locator=sk_locator.PIN_CODE_IMG_PROGRESS,
                                                        timeout=300)
        return True

    def input_pin_code(self, number: str, timeout: int = 10):
        """
        Метод ввода пин кода устройства.
        number: пин код
        """
        if self.wait_for_window(locator=sk_locator.PIN_CODE_TV_MESSAGE, text=sk_locator.PIN_CODE_TV_MESSAGE_TEXT,
                                timeout=timeout):
            assert self.input_by_num_pad(number, sk_locator.PIN_CODE_NUM_PAD)
            assert self.wait_until_element_will_not_present(locator=sk_locator.PIN_CODE_IMG_PROGRESS,
                                                            timeout=300)
            return True

    def input_by_num_pad(self, number: str, num_pad):
        """
        Метод ввода номера на пин паде
        number: номер
        num_pad: пин пад словарь из локаторов
        """
        assert number.replace(',', '.').replace('.', '').isnumeric()
        for i in number:
            locator = (num_pad[i])
            assert self.tap_to_element(locator)
        time.sleep(1)  # не трогать
        return True
