# coding: utf-8
import logging
from typing import Union, Tuple, Dict, List

from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By

import config
from core.appium.AppiumWebElementExtended.web_element_click import WebElementClick
from core.appium.AppiumWebElementExtended.web_element_dom import WebElementDOM
from core.appium.AppiumWebElementExtended.web_element_scroll import WebElementScroll
from core.appium.AppiumWebElementExtended.web_element_tap import WebElementTap
from core.appium.AppiumWebElementsExtended.web_element_elements import WebElementsExtended
from core.appium.AppiumWebElementExtended.web_element_adb_actions import WebElementAdbActions
from core.decorators.decorators import time_it


class WebElementExtended(WebElementClick,
                         WebElementAdbActions,
                         WebElementsExtended,
                         WebElementDOM,
                         WebElementTap,
                         WebElementScroll):
    """
    Основной интерфейс для работы с WebElementExtended
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = args[0]
        self.logger = logging.getLogger(config.LOGGER_NAME)

    # GET
    @time_it
    def get_element(self,
                    locator: Union[Tuple, WebElement, 'WebElementExtended', Dict[str, str], str] = None,
                    by: Union[MobileBy, AppiumBy, By, str] = None,
                    value: Union[str, Dict, None] = None,
                    timeout_elem: int = 10,
                    timeout_method: int = 600,
                    elements_range: Union[Tuple, List[WebElement], Dict[str, str], None] = None,
                    contains: bool = True
                    ) -> Union['WebElementExtended', None]:
        """
        fill me
        """
        inner_element = super()._get_element(locator=locator,
                                             by=by,
                                             value=value,
                                             timeout_elem=timeout_elem,
                                             timeout_method=timeout_method,
                                             elements_range=elements_range,
                                             contains=contains)
        return WebElementExtended(inner_element.parent, inner_element.id)

    @time_it
    def get_attributes(self,
                       desired_attributes: Union[str, List[str]] = None) -> \
            Union[str, Dict[str, str], None]:
        attributes = super()._get_attributes(desired_attributes=desired_attributes)
        return attributes

    # CLICK
    @time_it
    def click(self,
              duration: int = 0,
              decorator_args: dict = None,
              wait: bool = False, ) -> bool:
        """
        Нажимает на элемент.
        Args:
            duration: время в секундах продолжительности нажатия (по умолчанию 0)
            wait: ожидать изменение окна или нет
            decorator_args: параметры для декоратора.
                timeout_window: int время ожидания нового окна (умножается на количество попыток)
                tries: int количество попыток нажатия (по умолчанию 3)
        Usage:
            decorator_args = {"timeout_window": 5,
                              "tries": 5}
            element._tap(duration=0, wait=True, decorator_args=decorator_args)

        Returns:
            True если удалось нажать на элемент, иначе False
        """
        return super()._click(duration=duration,
                              wait=wait,
                              decorator_args=decorator_args)

    @time_it
    def double_click(self,
                     decorator_args: dict = None,
                     wait: bool = False, ) -> bool:
        """
        fill me
        """
        return super()._double_click(decorator_args=decorator_args,
                                     wait=wait)

    @time_it
    def click_and_move(self, locator: Union[Tuple, WebElement, 'WebElementExtended', Dict[str, str], str] = None,
                       x: int = None,
                       y: int = None,
                       direction: int = None,
                       distance: int = None,
                       ):
        """
        fill me
        """
        root = self.driver.find_element('xpath', '//*')
        root = WebElementExtended(root.parent, root.id)
        return super()._click_and_move(root=root, locator=locator, x=x, y=y, direction=direction, distance=distance)

    # ADB TAP
    @time_it
    def adb_tap(self,
                decorator_args: dict = None,
                wait: bool = False, ) -> bool:
        """
        tap by adb
        """
        return super()._adb_tap(wait=wait,
                                decorator_args=decorator_args)

    @time_it
    def adb_multi_tap(self):
        """
        double tap by adb
        """
        return super()._adb_multi_tap()

    @time_it
    def adb_swipe(self,
                  locator: Union[Tuple, WebElement, 'WebElementExtended', Dict[str, str], str] = None,
                  x: int = None,
                  y: int = None,
                  direction: int = None,
                  distance: int = None,
                  duration: int = 1,
                  contains: bool = True) -> bool:
        """
        swipe by adb
        """
        root = self.driver.find_element('xpath', '//*')
        root = WebElementExtended(root.parent, root.id)
        element = None
        if locator is not None:
            element = root.get_element(locator=locator)
        return super()._adb_swipe(root=root, element=element, x=x, y=y, direction=direction, distance=distance,
                                  duration=duration)

    # TAP
    @time_it
    def tap(self,
            duration: int = 0,
            decorator_args: dict = None,
            wait: bool = False, ) -> bool:
        positions = self.get_center()
        return super()._tap(positions=[positions],
                            duration=duration,
                            decorator_args=decorator_args,
                            wait=wait)

    @time_it
    def double_tap(self,
                   decorator_args: dict = None,
                   wait: bool = False,
                   pause: float = 0.2) -> bool:
        positions = self.get_center()
        return super()._double_tap(positions=positions,
                                   decorator_args=decorator_args,
                                   wait=wait,
                                   pause=pause)

    @time_it
    def tap_and_move(self,
                     locator: Union[Tuple, WebElement, 'WebElementExtended', Dict[str, str], str] = None,
                     x: int = None,
                     y: int = None,
                     direction: int = None,
                     distance: int = None,
                     ):
        root = self.driver.find_element('xpath', '//*')
        root = WebElementExtended(root.parent, root.id)
        return super()._tap_and_move(root=root, locator=locator, x=x, y=y, direction=direction, distance=distance)

    # ELEMENTS
    @time_it
    def get_elements(self,
                     locator: Union[Tuple, List[WebElement], Dict[str, str], str] = None,
                     by: Union[MobileBy, AppiumBy, By, str] = None,
                     value: Union[str, Dict, None] = None,
                     timeout_elements: int = 10,
                     timeout_method: int = 600,
                     elements_range: Union[Tuple, List[WebElement], Dict[str, str], None] = None,
                     contains: bool = True) -> \
            Union[List[WebElement], None]:
        """
        fill me
        """
        elements = super()._get_elements(locator=locator,
                                         by=by,
                                         value=value,
                                         timeout_elements=timeout_elements,
                                         timeout_method=timeout_method,
                                         elements_range=elements_range,
                                         contains=contains)
        result = []
        for element in elements:
            result.append(WebElementExtended(element.parent, element.id))
        return result

    # SCROLL
    @time_it
    def scroll_down(self,
                    locator: Union[Tuple, 'WebElementExtended', Dict[str, str], str] = None,
                    duration: int = None) -> bool:
        """
        Скроллит элемент вниз от нижнего до верхнего элемента.
        :param child_locator: str, имя класса дочернего элемента.
        :param timeout: int, время ожидания элемента, по умолчанию 10 секунд.
        :return: bool, True, если скроллинг выполнен успешно.
        """
        return super()._scroll_down(locator=locator,
                                    duration=duration)

    @time_it
    def scroll_up(self,
                  locator: Union[Tuple, 'WebElementExtended', Dict[str, str], str] = None,
                  duration: int = None) -> bool:
        """
        Скроллит элемент вверх от верхнего дочернего элемента до нижнего дочернего элемента родительского элемента.
        :param locator: Union[tuple, WebElement], локатор или элемент, который нужно проскроллить.
        :param child_locator: str, имя класса дочернего элемента.
        :param timeout: int, время ожидания элемента, по умолчанию 10 секунд.
        :return: bool, True, если скроллинг выполнен успешно.
        """
        return super()._scroll_up(locator=locator,
                                  duration=duration)

    @time_it
    def scroll_to_bottom(self,
                         locator: Union[Tuple, 'WebElementExtended', Dict[str, str], str] = None,
                         timeout_method: int = 120) -> bool:
        return super()._scroll_to_bottom(locator=locator,
                                         timeout_method=timeout_method)

    @time_it
    def scroll_to_top(self,
                      locator: Union[Tuple, 'WebElementExtended', Dict[str, str], str] = None,
                      timeout_method: int = 120) -> bool:
        return super()._scroll_to_top(locator=locator,
                                      timeout_method=timeout_method)

    @time_it
    def scroll_until_find(self,
                          locator: Union[Tuple, 'WebElementExtended', Dict[str, str], str],
                          roll_locator: Union[Tuple, 'WebElementExtended', Dict[str, str], str] = None,
                          timeout_method: int = 120) -> bool:
        return super()._scroll_until_find(locator=locator,
                                          roll_locator=roll_locator,
                                          timeout_method=timeout_method)

    # DOM
    @time_it
    def get_parent(self):
        """
        fill me
        """
        element = super()._get_parent()
        return WebElementExtended(element.parent, element.id)

    @time_it
    def get_parents(self):
        """
        fill me
        """
        elements = super()._get_parents()
        elements_ext = []
        for element in elements:
            elements_ext.append(WebElementExtended(element.parent, element.id))
        return elements_ext

    @time_it
    def get_sibling(self, attributes: dict, contains: bool = True):
        """
        fill me
        """
        element = super()._get_sibling(attributes=attributes, contains=contains)
        return WebElementExtended(element.parent, element.id)

    @time_it
    def get_siblings(self):
        """
        fill me
        """
        elements = super()._get_siblings()
        elements_ext = []
        for element in elements:
            elements_ext.append(WebElementExtended(element.parent, element.id))
        return elements_ext

    @time_it
    def get_cousin(self, ancestor: Union[Tuple, WebElement, 'WebElementExtended', Dict[str, str], str],
                   cousin: dict, contains: bool = True):
        """
        fill me
        """
        root = self.driver.find_element('xpath', '//*')
        root = WebElementExtended(root.parent, root.id)
        ancestor = root.get_element(ancestor)
        ancestor = WebElement(ancestor.parent, ancestor.id)
        element = super()._get_cousin(ancestor=ancestor, cousin=cousin, contains=True)
        return WebElementExtended(element.parent, element.id)

    @time_it
    def get_cousins(self, ancestor: Union[Tuple, WebElement, 'WebElementExtended', Dict[str, str], str],
                    cousin: dict, contains: bool = True):
        """
        fill me
        """
        root = self.driver.find_element('xpath', '//*')
        root = WebElementExtended(root.parent, root.id)
        ancestor = root.get_element(ancestor)
        ancestor = WebElement(ancestor.parent, ancestor.id)
        elements = super()._get_cousins(ancestor=ancestor, cousin=cousin, contains=True)
        elements_ext = []
        for element in elements:
            elements_ext.append(WebElementExtended(element.parent, element.id))
        return elements_ext

    @time_it
    def is_contains(self,
                    locator: Union[Tuple, WebElement, 'WebElementExtended', Dict[str, str], str],
                    contains: bool = True) -> bool:
        """
        fill me
        """
        child_element = self.get_element(locator=locator, contains=contains)
        if child_element is not None:
            return True
        return False

    # ACTIONS

    @time_it
    def zoom(hold: bool):
        """
        fill me
        """
        return False

    @time_it
    def unzoom(hold: bool):
        """
        fill me
        """
        return False

    @time_it
    def get_center(self) -> Union[Tuple[int, int], None]:
        """
        Вычисляет координаты центра заданного элемента.

        Аргументы:
            element (WebElement): Веб-элемент.

        Возвращает:
            tuple: Координаты центра в виде (x, y). Возвращает None, если произошла ошибка.
        """
        return self._get_center()
