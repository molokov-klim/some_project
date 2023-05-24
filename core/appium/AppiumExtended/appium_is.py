# coding: utf-8

from typing import Union
from appium.webdriver import WebElement

from core.appium.AppiumExtended.appium_elements import AppiumElements
from core.decorators.decorators import log_debug


class AppiumIs(AppiumElements):
    """
    Класс работы с Appium.
    Обеспечивает проверку чего-либо
    """

    def __init__(self):
        super().__init__()

    @log_debug()
    def is_element_within_screen(self, locator: Union[tuple, WebElement], timeout: int = 10) -> bool:
        """
        Метод проверяет, находится ли заданный элемент на видимом экране.
        :param locator: tuple or WebElement, локатор или элемент.
        :param timeout: int, время ожидания элемента.
        :return: bool, True если элемент находится на экране, и False, если нет.
        """
        screen_size = self.driver.get_window_size()
        element = self._get_element(locator=locator, timeout=timeout)
        element_location = element.location
        element_size = element.size
        screen_height = screen_size['height']
        screen_width = screen_size['width']
        if (element_location['y'] + element_size['height'] > screen_height) or \
                (element_location['x'] + element_size['width'] > screen_width) or \
                (element_location['y'] < 0) or (element_location['x'] < 0):
            return False
        return True



    #
    # def is_element_displayed(self, locator) -> bool:
    #     """
    #     This method should use the Appium driver to locate an element by the provided locator,
    #     and return a boolean value indicating whether the element is displayed on the screen or not.
    #     """
    #     self.logger.debug(f"is_element_displayed(locator {locator})")
    #     try:
    #         element = self.find_element(locator)
    #         if not element.is_displayed():
    #             self.logger.debug(f"is_element_displayed(locator {locator}): False")
    #             return False
    #         self.logger.debug(f"is_element_displayed(locator {locator}): True")
    #         return True
    #     except:
    #         self.logger.debug(f"is_element_displayed(locator {locator}): False")
    #         return False
    #
    # def is_element_enabled(self, locator) -> bool:
    #     self.logger.debug(f"is_element_enabled(locator {locator})")
    #     try:
    #         element = self.find_element(locator)
    #         if not element.is_enabled():
    #             self.logger.debug(f"is_element_enabled(locator {locator}): False")
    #             return False
    #         self.logger.debug(f"is_element_enabled(locator {locator}): True")
    #         return True
    #     except:
    #         self.logger.debug(f"is_element_enabled(locator {locator}): False")
    #         return False
    #
    # def is_element_active(self, locator) -> bool:
    #     self.logger.debug(f"is_element_active(locator {locator})")
    #     try:
    #         element = self.find_element(locator)
    #         if not element.is_displayed():
    #             self.logger.debug(f"is_element_active(locator {locator}): False")
    #             return False
    #         if not element.is_enabled():
    #             self.logger.debug(f"is_element_active(locator {locator}): False")
    #             return False
    #         self.logger.debug(f"is_element_active(locator {locator}): True")
    #         return True
    #     except Exception as e:
    #         self.logger.debug(f"is_element_active(locator {locator}): False", "{}".format(e))
    #         return False
    #
    # def is_element_attribute_value(self, locator: tuple, attr: str, value: str) -> bool:
    #     self.logger.debug(f"is_element_attribute_value() {locator=}, {attr=}")
    #     try:
    #         element_atrr = self.get_element_attribute(locator=locator, attr=attr)
    #         assert element_atrr is not None
    #         assert value == element_atrr
    #     except AssertionError:
    #         return False
