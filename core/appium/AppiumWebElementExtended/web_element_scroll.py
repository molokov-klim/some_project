# coding: utf-8
import logging
import time
from typing import Union, Tuple, Dict

from appium.webdriver import WebElement
from selenium.common import StaleElementReferenceException, NoSuchElementException, TimeoutException

import config

from core.appium.AppiumWebElementExtended.web_element_get import WebElementGet


class WebElementScroll(WebElementGet):
    """
    Класс для выполнения действий прокрутки элемента.
    Наследуется от класса WebElementGet.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = args[0]
        self.logger = logging.getLogger(config.LOGGER_NAME)

    def _scroll_down(self,
                     locator: Union[Tuple, 'WebElementExtended', Dict[str, str], str] = None,
                     duration: int = None) -> bool:
        """
        Прокручивает элемент вниз от нижнего дочернего элемента до верхнего дочернего элемента родительского элемента.

        Args:
            locator (Union[Tuple, WebElement, Dict[str, str], str], optional): Локатор или элемент для прокрутки (за что крутить).
            duration (int, optional): Продолжительность прокрутки в миллисекундах (по умолчанию: None).

        Returns:
            bool: True, если прокрутка выполнена успешно.

        """
        try:
            recycler = self

            # Проверка, является ли элемент прокручиваемым
            if recycler.get_attribute('scrollable') != 'true':
                self.logger.error("Элемент не крутиться")
                return False

            # Если локатор для прокрутки не указан, используется локатор первого дочернего элемента
            if not locator:
                locator = {'class': self._get_first_child_class()}

            # Получение верхнего и нижнего дочерних элементов родительского элемента
            top_child = self._get_top_child_from_parent(locator=locator)
            bottom_child = self._get_bottom_child_from_parent(locator=locator)

            # Прокрутка вниз от нижнего дочернего элемента до верхнего дочернего элемента родительского элемента
            self.driver.scroll(origin_el=bottom_child, destination_el=top_child, duration=duration)
            return True

        except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
            self.logger.error("_scroll_down(): Ошибка. {}".format(e))
            return False

    def _scroll_up(self,
                   locator: Union[Tuple, 'WebElementExtended', Dict[str, str], str] = None,
                   duration: int = None) -> bool:
        """
        Прокручивает элемент вверх от верхнего дочернего элемента до нижнего дочернего элемента родительского элемента.

        Args:
            locator (Union[Tuple, WebElement, Dict[str, str], str], optional): Локатор или элемент для прокрутки (за что крутить).
            duration (int, optional): Продолжительность прокрутки в миллисекундах (по умолчанию: None).

        Returns:
            bool: True, если прокрутка выполнена успешно.

        """
        try:
            recycler = self

            # Проверка, является ли элемент прокручиваемым
            if recycler.get_attribute('scrollable') != 'true':
                self.logger.error("Элемент не крутиться")
                return False

            # Если локатор для прокрутки не указан, используется локатор первого дочернего элемента
            if not locator:
                locator = {'class': self._get_first_child_class()}

            # Получение верхнего и нижнего дочерних элементов родительского элемента
            top_child = self._get_top_child_from_parent(locator=locator)
            bottom_child = self._get_bottom_child_from_parent(locator=locator)

            # Прокрутка вверх от верхнего дочернего элемента до нижнего дочернего элемента родительского элемента
            self.driver.scroll(origin_el=top_child, destination_el=bottom_child, duration=duration)
            return True

        except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
            self.logger.error("_scroll_up(): Ошибка. {}".format(e))
            return False

    def _scroll_to_bottom(self,
                          locator: Union[Tuple, WebElement, Dict[str, str], str] = None,
                          timeout_method: int = 120) -> bool:
        """
        Прокручивает элемент вниз до упора.

        Args:
            locator (Union[Tuple, WebElement, Dict[str, str], str], optional): Локатор или элемент для прокрутки (за что крутить).
            timeout_method (int, optional): Время ожидания элемента в секундах (по умолчанию: 120).

        Returns:
            bool: True, если прокрутка выполнена успешно.

        """
        recycler = self

        # Проверка, является ли элемент прокручиваемым
        if recycler.get_attribute('scrollable') != 'true':
            self.logger.error("Элемент не крутиться")
            return False

        # Если локатор для прокрутки не указан, используется локатор первого дочернего элемента
        if not locator:
            locator = {'class': self._get_first_child_class()}

        last_child = None
        start_time = time.time()

        # Прокрутка вниз до упора
        while time.time() - start_time < timeout_method:
            child = self._get_element(locator=locator)
            if child == last_child:
                return True
            last_child = child
            self._scroll_down(locator=locator)
        self.logger.error("_scroll_to_bottom(): Неизвестная ошибка")
        return False

    def _scroll_to_top(self,
                       locator: Union[Tuple, WebElement, Dict[str, str], str],
                       timeout_method: int = 120) -> bool:
        """
        Прокручивает элемент вверх до упора.

        Args:
            locator (Union[Tuple, WebElement, Dict[str, str], str]): Локатор или элемент для прокрутки (за что крутить).
            timeout_method (int): Время ожидания элемента в секундах (по умолчанию: 120).

        Returns:
            bool: True, если прокрутка выполнена успешно.

        """
        recycler = self

        # Проверка, является ли элемент прокручиваемым
        if recycler.get_attribute('scrollable') != 'true':
            self.logger.error("Элемент не крутиться")
            return False

        # Если локатор для прокрутки не указан, используется локатор первого дочернего элемента
        if not locator:
            locator = {'class': self._get_first_child_class()}
        last_child = None
        start_time = time.time()

        # Прокрутка вверх до упора
        while time.time() - start_time < timeout_method:
            child = self._get_element(locator=locator)
            if child == last_child:
                return True
            last_child = child
            self._scroll_up(locator=locator)

        self.logger.error("_scroll_to_top(): Неизвестная ошибка")
        return False

    def _scroll_until_find(self,
                           locator: Union[Tuple, WebElement, Dict[str, str], str],
                           roll_locator: Union[Tuple, WebElement, Dict[str, str], str] = None,
                           timeout_method: int = 120) -> bool:
        """
        Крутит элемент вниз, а затем вверх для поиска элемента по заданному локатору.

        Args:
            locator (Union[Tuple, WebElement, Dict[str, str], str]): Локатор или элемент, для которого производится
                поиск.
            roll_locator (Union[Tuple, WebElement, Dict[str, str], str], optional): Локатор элемента,
            за который производится захват для прокрутки.
            timeout_method (int): Время на поиск в одном направлении (по умолчанию: 120 вниз и 120 вверх).

        Returns:
            bool: True, если элемент найден. False, если элемент не найден.

        """
        recycler = self

        # Проверка, является ли элемент scrollable
        if recycler.get_attribute('scrollable') != 'true':
            self.logger.error("Элемент не крутиться")
            return False

        # Если не указан локатор для прокрутки, используется локатор первого дочернего элемента
        if not roll_locator:
            roll_locator = {'class': self._get_first_child_class()}
        last_child = None
        start_time = time.time()

        # Прокрутка вниз до поиска элемента
        while time.time() - start_time < timeout_method:
            try:
                self._get_element(locator=locator, timeout_elem=1)
            except NoSuchElementException:
                pass
            child = self._get_element(locator=roll_locator)
            if child == last_child:
                break
            last_child = child
            self._scroll_down(locator=roll_locator)

        # Прокрутка вверх до поиска элемента
        while time.time() - start_time < timeout_method:
            try:
                self._get_element(locator=locator, timeout_elem=1)
            except NoSuchElementException:
                pass
            child = self._get_element(locator=roll_locator)
            if child == last_child:
                return True
            last_child = child
            self._scroll_up(locator=roll_locator)

        self.logger.error("_scroll_until_find(): Элемент не найден")
        return False
