# coding: utf-8
import time
from typing import Union, Dict, Tuple

from appium.webdriver.common.mobileby import MobileBy
from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException

from appium.webdriver import WebElement

from core.appium.AppiumExtended.appium_dom import AppiumDOM
from core.appium.AppiumExtended.appium_elements import AppiumElements
from core.decorators.decorators import log_debug


class AppiumScroll(AppiumElements):
    """
    Класс работы с Appium.
    Обеспечивает выполнение скролла
    """

    def __init__(self):
        super().__init__()

    @log_debug()
    def scroll_element_down(self,
                            locator: Union[tuple, WebElement],
                            child=None,
                            timeout_elem: int = 10) -> bool:
        """
        Скроллит элемент вниз от нижнего дочернего элемента до верхнего дочернего элемента родительского элемента.
        :param locator: Union[tuple, WebElement], локатор или элемент, который нужно проскроллить.
        :param child: str, имя класса дочернего элемента.
        :param timeout: int, время ожидания элемента, по умолчанию 10 секунд.
        :return: bool, True, если скроллинг выполнен успешно.
        """
        try:
            recycler = self.get_element(locator=locator, timeout_elem=timeout_elem)
            print("recycler.get_attribute('scrollable')", recycler.get_attribute('scrollable'))
            assert recycler.get_attribute('scrollable') == 'true'
            if not child:
                child = {'class': self.get_first_child_class(parent_locator=recycler)}
            top_child = self.get_top_child_from_parent(parent=recycler, child=child)
            bottom_child = self.get_bottom_child_from_parent(parent=recycler, child=child)
            self.driver.scroll(origin_el=bottom_child, destination_el=top_child)
            return True
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
            return False

    @log_debug()
    def scroll_element_up(self,
                          locator: Union[Tuple, WebElement],
                          child: Union[Tuple, WebElement, Dict[str, str], str] = None,
                          timeout_elem: int = 10) -> bool:
        """
        Скроллит элемент вверх от верхнего дочернего элемента до нижнего дочернего элемента родительского элемента.
        :param locator: Union[tuple, WebElement], локатор или элемент, который нужно проскроллить.
        :param child: str, имя класса дочернего элемента.
        :param timeout: int, время ожидания элемента, по умолчанию 10 секунд.
        :return: bool, True, если скроллинг выполнен успешно.
        """
        try:
            recycler = self.get_element(locator=locator, timeout_elem=timeout_elem)
            print("recycler.get_attribute('scrollable')", recycler.get_attribute('scrollable'))
            assert recycler.get_attribute('scrollable') == 'true'
            if not child:
                child = {'class': self.get_first_child_class(parent_locator=recycler)}
            top_child = self.get_top_child_from_parent(parent=recycler, child=child)
            bottom_child = self.get_bottom_child_from_parent(parent=recycler, child=child)
            self.driver.scroll(origin_el=top_child, destination_el=bottom_child)
            return True
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
            return False

    @log_debug()
    def scroll_element_to_bottom(self,
                                 locator: Union[tuple, WebElement],
                                 child: Union[Tuple, WebElement, Dict[str, str], str] = None,
                                 timeout_elem: int = 10,
                                 timeout_method: int = 120) -> bool:
        """
        Скроллит элемент вниз до упора.
        :param locator: Union[tuple, WebElement], локатор или элемент, который нужно проскроллить.
        :param child: str, имя класса дочернего элемента.
        :param timeout: int, время ожидания элемента, по умолчанию 10 секунд.
        :return: bool, True, если скроллинг выполнен успешно.
        """
        recycler = self.get_element(locator=locator, timeout_elem=timeout_elem)
        assert recycler.get_attribute('scrollable') == 'true'
        if not child:
            child_class = self.get_first_child_class(parent_locator=recycler)
            #child_locator = self._get_element(locator={'class': child_class})
        else:
            child_class = self.get_element(child).get_attribute('class')
        last_child = None
        start_time = time.time()
        while time.time() - start_time < timeout_method:
            child = self.get_element(locator={'class': child_class})
            if child == last_child:
                return True
            last_child = child
            self.scroll_element_down(locator=recycler, child=child)
        return False
        # recycler = self._get_element(locator=locator, timeout_elem=timeout_elem)
        # assert recycler.get_attribute('scrollable') == 'true'
        # if not child_locator:
        #     child_locator = self.get_first_child_class(parent_locator=recycler)
        # last_children = None
        # start_time = time.time()
        # while time.time() - start_time < timeout_method:
        #     children = [el for el in recycler.find_elements(by=MobileBy.CLASS_NAME, value=child_locator)]
        #     if children == last_children:
        #         return True
        #     last_children = children
        #     self.scroll_element_down(locator=recycler, child_locator=child_locator)
        # return False

    @log_debug()
    def scroll_element_to_top(self,
                              locator: Union[tuple, WebElement],
                              child: str = None, timeout_elem: int = 10,
                              timeout_method: int = 120) -> bool:
        """
        Скроллит элемент вверх до упора.
        :param locator: Union[tuple, WebElement], локатор или элемент, который нужно проскроллить.
        :param child: str, имя класса дочернего элемента.
        :param timeout: int, время ожидания элемента, по умолчанию 120 секунд.
        :return: bool, True, если скроллинг выполнен успешно.
        """
        recycler = self.get_element(locator=locator, timeout_elem=timeout_elem)
        assert recycler.get_attribute('scrollable') == 'true'
        if not child:
            child = self.get_first_child_class(parent_locator=recycler)
        last_children = None
        start_time = time.time()
        while time.time() - start_time < timeout_method:
            top_child = self.get_top_child_from_parent(parent=recycler, child=child)
            bottom_child = self.get_bottom_child_from_parent(parent=recycler, child=child)
            children = [el for el in recycler.find_elements(by=MobileBy.CLASS_NAME, value=child)]
            if children == last_children:
                return True
            last_children = children
            self.driver.scroll(origin_el=top_child, destination_el=bottom_child)
        return False

    @log_debug()  # TODO крутить вниз до упора, потом крутить вверх до упора. реализовать в трех методах
    def scroll_element_until_find(self,
                                  locator: Union[tuple, WebElement],
                                  child: Union[tuple, Dict[str, str]] = None,
                                  attribute: str = None,
                                  value: str = None,
                                  timeout_elem: int = 10,
                                  timeout_method: int = 120) -> bool:
        """
        Скроллит элемент вниз до поиска элемента по заданному локатору.
        :param locator: Union[tuple, WebElement], локатор или элемент, внутри которого производится поиск.
        :param child_locator: tuple, локатор внутри родительского элемента, который нужно найти.
        :param attribute: str, имя атрибута элемента, который нужно найти.
        :param value: str, значение атрибута элемента, который нужно найти.
        :param timeout: int, время ожидания элемента, по умолчанию 300 секунд.
        :return: WebElement или None, в случае его отсутствия
        """
        recycler = self.get_element(locator=locator, timeout_elem=timeout_elem)
        assert recycler.get_attribute('scrollable') == 'true'
        if not child:
            child = {'class': self.get_first_child_class(parent_locator=recycler)}
        last_children = None
        start_time = time.time()
        while time.time() - start_time < timeout_method:
            children = [el for el in recycler.find_elements(by=MobileBy.CLASS_NAME, value=child)]
            if children == last_children:
                return True
            last_children = children
            self.scroll_element_down(locator=recycler, child=child)
        return False

    ######################################################################################
    # def scroll_down_by_adb(self, max_scrolls: int = 1) -> bool:
    #     self.logger.debug(f"scroll_down_by_adb")
    #     try:
    #         screen_size = self.driver.get_window_size()
    #         height = screen_size['height']
    #         width = screen_size['width']
    #         start_x = int(width * 0.5)
    #         end_x = int(width * 0.5)
    #         start_y = int(height * 0.7)
    #         end_y = int(height * 0.4)
    #
    #         scroll_count = 0
    #
    #         while scroll_count < max_scrolls:
    #             adb.swipe(start_x=start_x, end_x=end_x, start_y=start_y, end_y=end_y)
    #             scroll_count += 1
    #         return True
    #     except Exception as e:
    #         self.logger.error("Error with scroll_down_by_adb: {}".format(e))
    #         return False
    #
    # def scroll_up_by_adb(self, max_scrolls: int = 1) -> bool:
    #     self.logger.debug(f"scroll_up_by_adb")
    #     try:
    #         screen_size = self.driver.get_window_size()
    #         height = screen_size['height']
    #         width = screen_size['width']
    #         start_x = int(width * 0.5)
    #         end_x = int(width * 0.5)
    #         start_y = int(height * 0.4)
    #         end_y = int(height * 0.7)
    #         scroll_count = 0
    #
    #         while scroll_count < max_scrolls:
    #             adb.swipe(start_x=start_x, end_x=end_x, start_y=start_y, end_y=end_y)
    #             scroll_count += 1
    #         return True
    #     except Exception as e:
    #         self.logger.error("Error with scroll_up_by_adb: {}".format(e))
    #         return False
    #
    # def scroll_down_to_element_by_adb(self, locator: tuple, max_scrolls: int = 5) -> bool:
    #     """
    #     Метод через adb скроллит вниз, пока элемент не будет найден или не будет исчерпано max_scrolls.
    #     """
    #     self.logger.debug(
    #         f"scroll_down_to_element_by_adb(self, locator {locator}: tuple, max_scrolls {max_scrolls}: int = 5)")
    #     wait = WebDriverWait(self.driver, 5)
    #     screen_size = self.driver.get_window_size()
    #     height = screen_size['height']
    #     width = screen_size['width']
    #     scroll_count = 0
    #
    #     while scroll_count < max_scrolls:
    #         try:
    #             element = wait.until(EC.visibility_of_element_located(locator))
    #             if self.is_element_within_screen(element, screen_size):
    #                 self.logger.debug(
    #                     f"scroll_down_to_element_by_adb: True")
    #                 return True
    #         except TimeoutException:
    #             pass
    #
    #         start_x = int(width * 0.5)
    #         end_x = int(width * 0.5)
    #
    #         start_y = int(height * 0.8)
    #         end_y = int(height * 0.5)
    #
    #         adb.swipe(start_x=start_x, end_x=end_x, start_y=start_y, end_y=end_y)
    #         scroll_count += 1
    #     self.logger.debug(
    #         f"scroll_down_to_element_by_adb: False")
    #     return False
    #
    # def scroll_up_to_element_by_adb(self, locator: tuple, max_scrolls: int = 1) -> bool:
    #     """
    #     This method should use the adb to scroll up until the element is displayed.
    #     """
    #     self.logger.debug(
    #         f"scroll_up_to_element_by_adb(self, locator {locator}: tuple, max_scrolls {max_scrolls}: int = 5)")
    #     wait = WebDriverWait(self.driver, 5)
    #     screen_size = self.driver.get_window_size()
    #     height = screen_size['height']
    #     width = screen_size['width']
    #     scroll_count = 0
    #
    #     while scroll_count < max_scrolls:
    #         try:
    #             element = wait.until(EC.visibility_of_element_located(locator))
    #             if self.is_element_within_screen(element, screen_size):
    #                 self.logger.debug(
    #                     f"scroll_up_to_element_by_adb: True")
    #                 return True
    #         except TimeoutException:
    #             pass
    #
    #         start_x = int(width * 0.5)
    #         end_x = int(width * 0.5)
    #
    #         start_y = int(height * 0.5)
    #         end_y = int(height * 0.8)
    #
    #         adb.swipe(start_x=start_x, end_x=end_x, start_y=start_y, end_y=end_y)
    #         scroll_count += 1
    #     self.logger.debug(
    #         f"scroll_up_to_element_by_adb: False")
    #     return False
    #
    #
    # def scroll_to_and_tap(self, locator, timeout: int = 30):
    #     self.logger.debug(f"def scroll_to_and_tap() locator {locator}")
    #     time.sleep(1)
    #     if self.scroll_to(locator=locator):
    #         self._tap(locator=locator)
    #         return True
    #     return False
    #
    #
    # def scroll_to(self, locator, max_retries=2):
    #     self.logger.debug(f"scroll_to(locator {locator}, max_retries {max_retries})")
    #     time.sleep(1)
    #     for i in range(max_retries):
    #         try:
    #             if not self.is_element_displayed(locator=locator):
    #                 self.scroll_down_to(locator=locator)
    #                 if not self.is_element_displayed(locator):
    #                     self.scroll_up_to(locator=locator)
    #                     if not self.is_element_displayed(locator=locator):
    #                         continue
    #             time.sleep(0.1)
    #             self.logger.debug(f"scroll_to(locator {locator}, max_retries {max_retries}): True")
    #             return True
    #         except Exception as e:
    #             self.logger.error(f"Exception occurred while trying to _tap element: {e}")
    #             self.logger.error(f"Exception occurred while trying to _tap element: {locator}")
    #     self.logger.debug(f"scroll_to(locator {locator}, max_retries {max_retries}): False")
    #     return False
    #
    # def scroll_down_to(self, locator: tuple, timeout: int = 600):
    #     self.logger.debug(f"scroll_down_to() locator {locator})")
    #     time.sleep(2)
    #     source = self.get_page_source()
    #     new_source = None
    #     start_time = time.time()
    #     while source != new_source and not time.time() - start_time > timeout:
    #         time.sleep(1)
    #         if self.is_element_displayed(locator=locator):
    #             if self.is_element_within_screen(self.find_element(locator=locator),
    #                                              screen_size=self.driver.get_window_size()):
    #                 self.logger.info("Элемент найден")
    #                 return True
    #         self.scroll_down_by_adb(max_scrolls=1)
    #         time.sleep(1)
    #         new_source = self.get_page_source()
    #     self.logger.debug(f"scroll_down_to() False)")
    #     return False
    #
    # def scroll_up_to(self, locator: tuple, timeout: int = 600):
    #     self.logger.debug(f"scroll_up_to() locator {locator})")
    #     source = self.get_page_source()
    #     new_source = None
    #     start_time = time.time()
    #     while source != new_source and not time.time() - start_time > timeout:
    #         if self.scroll_up_to_element_by_adb(locator=locator, max_scrolls=1):
    #             self.logger.debug(f"scroll_up_to() True)")
    #             return True
    #         time.sleep(1)
    #         new_source = self.get_page_source()
    #     self.logger.debug(f"scroll_up_to() False)")
    #     return False
    #
    # def scroll_to_element_with_text_and_tap(self, type_of: str, text: str, max_retries=3):  # TODO change me
    #     self.logger.debug(
    #         f"scroll_to_element_with_text_and_tap(type {type_of}, text {text}, max_retries {max_retries})")
    #     locator = ("xpath", f"//android.widget.{type_of}[contains(@text,'{text}')]")
    #     self.logger.debug(f"locator_: {locator}")
    #     for i in range(max_retries):
    #         try:
    #             if not self.is_element_displayed(locator=locator):
    #                 self.scroll_down_to_element_by_adb(locator=locator, max_scrolls=3)
    #                 if not self.is_element_displayed(locator):
    #                     self.scroll_up_to_element_by_adb(locator=locator, max_scrolls=5)
    #                     if not self.is_element_displayed(locator=locator):
    #                         if not self.is_element_displayed(locator=locator):
    #                             self.scroll_down_to_element_by_adb(locator=locator, max_scrolls=30)
    #                             if not self.is_element_displayed(locator):
    #                                 self.scroll_up_to_element_by_adb(locator=locator, max_scrolls=50)
    #                                 if not self.is_element_displayed(locator=locator):
    #                                     continue
    #             time.sleep(1)
    #             self._tap(locator=locator)
    #             time.sleep(0.1)
    #             self.logger.debug(f"scroll_to_element_with_text_and_tap(text {text}, max_retries {max_retries}): True")
    #             return True
    #         except InvalidElementStateException as e:
    #             self.logger.error(f"InvalidElementStateException occurred while trying to _tap element {locator}: {e}")
    #         except Exception as e:
    #             self.logger.error(f"Exception occurred while trying to _tap element {locator}: {e}")
    #     self.logger.debug(f"scroll_to_element_with_text_and_tap(text {text}, max_retries {max_retries}): False")
    #     return False
    #
    # def scroll_to_and_get_element(self, locator, max_retries=3) -> webdriver.webelement:
    #     self.logger.debug(f"scroll_to_and_get_element(locator {locator}, max_retries {max_retries})")
    #     time.sleep(1)
    #     for i in range(max_retries):
    #         try:
    #             element = self.find_element(locator=locator)
    #             if element.is_displayed():
    #                 self.logger.debug(f"scroll_to_and_get_element(locator {locator}, max_retries {max_retries}): True")
    #                 return element
    #             else:
    #                 self.scroll_down_to_element_by_adb(locator=locator, max_scrolls=3)
    #                 if element.is_displayed():
    #                     self.logger.debug(
    #                         f"scroll_to_and_get_element(locator {locator}, max_retries {max_retries}): True")
    #                     return element
    #                 else:
    #                     self.scroll_up_to_element_by_adb(locator=locator, max_scrolls=3)
    #                     if element.is_displayed():
    #                         self.logger.debug(
    #                             f"scroll_to_and_get_element(locator {locator}, max_retries {max_retries}): True")
    #                         return element
    #         except Exception as e:
    #             self.logger.error(f"Exception occurred while trying to find element: {e}")
    #     self.logger.debug(f"scroll_to_and_get_element(locator {locator}, max_retries {max_retries}): None")
    #     return None
    #
    # def scroll_to_element_with_text_and_get_element(self, text: str):
    #     locator = ("xpath", f".//*[contains(@text, '{text}')]")
    #     if self.scroll_down_to(locator):
    #         return self._get_element(locator)
    #     if self.scroll_up_to(locator):
    #         return self._get_element(locator)
