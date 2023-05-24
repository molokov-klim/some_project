# coding: utf-8
import logging
import re
import time
from typing import Union, Dict, List, Tuple

import xml.etree.ElementTree as ET

from appium.webdriver import WebElement
from selenium.common import WebDriverException

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

import config
from core.appium.AppiumHelpers.appium_helpers import AppiumHelpers


class WebElementGet(WebElement):
    """
    Класс расширяющий Appium WebElement.
    Обеспечивает получение сущностей из элемента.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = None
        self.driver = args[0]
        self.logger = logging.getLogger(config.LOGGER_NAME)

    def _get_element(self,
                     locator: Union[Tuple, WebElement, 'WebElementExtended', Dict[str, str], str] = None,
                     by: Union[MobileBy, AppiumBy, By, str] = None,
                     value: Union[str, Dict, None] = None,
                     timeout_elem: int = 10,
                     timeout_method: int = 600,
                     elements_range: Union[Tuple, List[WebElement], Dict[str, str], None] = None,
                     contains: bool = True
                     ) -> \
            Union[WebElement, None]:
        """
        Извлекает элемент из элемента.
        Должен принимать как минимум либо локатор, либо значения by и value.

        Usage:
            inner_element = element.get_element(locator=("id", "foo")).
            inner_element = element.get_element(element).
            inner_element = element.get_element(locator={'text': 'foo'}).
            inner_element = element.get_element(locator='/path/to/file/pay_agent.png').
            inner_element = element.get_element(locator=part_image,
                                       elements_range={'class':'android.widget.FrameLayout', 'package':'ru.app.debug'}).
            inner_element = element.get_element(by="id", value="ru.sigma.app.debug:id/backButton").
            inner_element = element.get_element(by=MobileBy.ID, value="ru.sigma.app.debug:id/backButton").
            inner_element = element.get_element(by=AppiumBy.ID, value="ru.sigma.app.debug:id/backButton").
            inner_element = element.get_element(by=By.ID, value="ru.sigma.app.debug:id/backButton").

        Args:
            locator: tuple / WebElement / dict / str, определяет локатор элемента.
                tuple - локатор в виде ('стратегия', 'значение'), например ('xpath', '//*'), ('id', 'elem_id') и т.д.
                WebElement / WebElementExtended - объект веб элемента
                dict - словарь, содержащий пары атрибут: значение (элемента), например {'text':'foo', 'enabled':'true'}
                str - путь до файла с изображением элемента.
            by: MobileBy, AppiumBy, By, str, тип локатора для поиска элемента (всегда в связке с value)
            value: str, dict, None, значение локатора или словарь аргументов, если используется AppiumBy.XPATH.
            timeout_elem: int, время ожидания элемента.
            timeout_method: int, время ожидания метода поиска элемента.
            elements_range: tuple, list, dict, None, ограничивает поиск элемента в указанном диапазоне
            (для поиска по изображению). По умолчанию - все элементы внутри текущего элемента

        Returns:
            WebElement или None, если элемент не был найден.
        """
        # Проверка и подготовка аргументов
        if (not locator) and (not by or not value):
            self.logger.error(f"Некорректные аргументы!\n"
                              f"{locator=}\n"
                              f"{by=}\n"
                              f"{value=}\n"
                              f"{timeout_elem=}\n")
            return None
        if not locator and (by and value):
            locator = (by, value)
        if locator is None:
            return None

        # Поиск по изображению в пределах текущего элемента
        if elements_range is None:
            elements_range = self.find_elements("xpath", ".//*")

        # Объявление стратегии поиска элементов
        self.helper = AppiumHelpers(driver=self.driver)
        locator_handler = {
            # составляет локатор типа tuple из словаря с атрибутами искомого элемента
            dict: self.helper.handle_dict_locator,
            # производит поиск элементов по фрагменту изображения, возвращает список элементов
            str: self.helper.handle_string_locator,
        }

        # Цикл подготовки локатора и поиска элементов
        start_time = time.time()
        while time.time() - start_time < timeout_method:
            # Выявление типа данных локатора для его подготовки
            if isinstance(locator, WebElement):
                return locator
            locator_type = type(locator)
            # Если локатор типа tuple, то выполняется извлечение элементов
            if isinstance(locator, tuple):
                try:
                    element = self.find_element(*locator)
                    return element
                except WebDriverException as e:
                    self.logger.error(f"Элемент не обнаружен!\n"
                                      f"{locator=}\n"
                                      f"{timeout_elem=}\n\n" +
                                      "{}\n".format(e))
                    self.logger.error(self.driver.page_source)
                    return None
            # Выполнение подготовки локатора
            handler = locator_handler.get(locator_type)
            locator = handler(locator=locator,
                              timeout=int(timeout_elem),
                              elements_range=elements_range,
                              contains=contains)
        # Подбирает результат после поиска по изображению
        if isinstance(locator, WebElement):
            return locator
        self.logger.error(f"Что-то пошло не так\n"
                          f"{locator=}\n"
                          f"{by=}\n"
                          f"{value=}\n"
                          f"{timeout_elem=}\n"
                          f"{timeout_method=}\n")
        return None

    def _get_elements(self,
                      locator: Union[Tuple, List[WebElement], Dict[str, str], str] = None,
                      by: Union[MobileBy, AppiumBy, By, str] = None,
                      value: Union[str, Dict, None] = None,
                      timeout_elements: int = 10,
                      timeout_method: int = 600,
                      elements_range: Union[Tuple, List[WebElement], Dict[str, str], None] = None,
                      contains: bool = True) -> \
            Union[List[WebElement], None]:
        """
        Метод обеспечивает поиск элементов в текущей DOM структуре.
        Должен принять либо локатор, либо by и value.

        Usage:
            elements = app.get_elements(locator=("id", "foo")).
            elements = app.get_elements(locator={'text': 'foo'}).
            elements = app.get_elements(locator='/path/to/file/pay_agent.png').
            elements = app.get_elements(by="id", value="ru.sigma.app.debug:id/backButton").
            elements = app.get_elements(by=MobileBy.ID, value="ru.sigma.app.debug:id/backButton").
            elements = app.get_elements(by=AppiumBy.ID, value="ru.sigma.app.debug:id/backButton").
            elements = app.get_elements(by=By.ID, value="ru.sigma.app.debug:id/backButton").

        Args:
            locator: tuple or WebElement or Dict[str, str], str, локатор tuple или Веб Элемент или словарь {'атрибут': 'значение'} или str как путь до файла с изображением элемента.
            by:[MobileBy, AppiumBy, By, str], тип локатора для поиска элемента (всегда в связке с value)
            value: Union[str, Dict, None], значение локатора или словарь аргументов, если используется AppiumBy.XPATH
            timeout_elements:
            timeout_method:
            elements_range:

        Returns:
            Список WebElement'ов, или пустой список в случае их отсутствия.
        """
        # Проверка и подготовка аргументов
        if not locator and (not by or not value):
            self.logger.error(f"Некорректные аргументы!\n"
                              f"{locator=}\n"
                              f"{by=}\n"
                              f"{value=}\n"
                              f"{timeout_elements=}\n"
                              f"{timeout_method=}\n"
                              f"{contains=}")
            return None
        if not locator and (by and value):
            locator = (by, value)
        if locator is None:
            return None

        # Объявление стратегии поиска элементов
        self.helper = AppiumHelpers(driver=self.driver)
        locator_handler = {
            # подразумевается список элементов, возвращает себя же
            list: self.helper.handle_webelement_locator_elements,
            # составляет локатор типа tuple из словаря с атрибутами искомого элемента
            dict: self.helper.handle_dict_locator_elements,
            # производит поиск элементов по фрагменту изображения, возвращает список элементов
            str: self.helper.handle_string_locator_elements,
        }

        # Цикл подготовки локатора и поиска элементов
        start_time = time.time()
        while not isinstance(locator, list) and time.time() - start_time < timeout_method:
            # Если локатор типа tuple, то выполняется извлечение элементов
            if isinstance(locator, tuple):
                try:
                    elements = self.find_elements(*locator)
                    return elements
                except WebDriverException as e:
                    self.logger.error(f"Элемент не обнаружен!\n"
                                      f"{locator=}\n"
                                      f"{by=}\n"
                                      f"{value=}\n"
                                      f"{timeout_elements=}\n"
                                      f"{timeout_method=}\n"
                                      f"{contains=}" +
                                      "{}\n".format(e))
                    return None
            # Выявление типа данных локатора для его подготовки
            locator_type = type(locator)
            # Выполнение подготовки локатора
            handler = locator_handler.get(locator_type)
            locator = handler(locator=locator,
                              timeout=int(timeout_elements),
                              elements_range=elements_range,
                              contains=contains)
        # Подбирает результат после поиска по изображению
        if isinstance(locator, list):
            return locator
        self.logger.error(f"Что-то пошло не так\n"
                          f"{locator=}\n"
                          f"{by=}\n"
                          f"{value=}\n"
                          f"{timeout_elements=}\n"
                          f"{timeout_method=}\n"
                          f"{contains=}")
        return None

    def _get_attributes(self,
                        desired_attributes: List[str] = None) -> Dict[str, str]:
        """
        Получает атрибуты элемента.
        Если хотя бы один запрашиваемый атрибут не найден, возвращает все атрибуты.

        Usage:
            element._get_attributes(['text', 'bounds', 'class'])
            element._get_attributes()

         Args:
            desired_attributes: список имен атрибутов для получения.
            Если не указан, будут возвращены все атрибуты элемента.

        Returns:
            Если указан desired_attributes и найдены в атрибутах элемента, возвращает словарь с требуемыми атрибутами
            и их значениями.
            Если desired_attributes не указан или атрибут не найден у элемента, возвращает словарь со всеми атрибутами.
        """
        # Инициализация пустого словаря для хранения атрибутов
        result = {}

        # Если desired_attributes не указан, установка значения 'all'
        if not desired_attributes:
            desired_attributes = 'all'

        # Если desired_attributes не указан, установка значения 'all'
        root = ET.fromstring(self.parent.page_source)

        # Поиск требуемого элемента по критериям атрибутов
        found_element = None
        for element in root.iter():
            if 'bounds' in element.attrib and 'class' in element.attrib:
                if self.get_attribute('bounds') == element.attrib['bounds'] and self.get_attribute('class') == \
                        element.attrib['class']:
                    found_element = element
                    break

        # Если элемент найден, получение его атрибутов
        if found_element is not None:
            attributes = found_element.attrib
            # Сохранение атрибутов в словаре result
            for attribute_name, attribute_value in attributes.items():
                result[attribute_name] = attribute_value

        # Если desired_attributes указан, фильтрация словаря result
        if desired_attributes:
            new_result = {}
            for attribute in desired_attributes:
                if attribute not in result:
                    # Возврат всех атрибутов если не найден искомый
                    return result
                new_result[attribute] = result[attribute]
            # Возврат отфильтрованных атрибутов
            return new_result
        # Возврат всех атрибутов
        return result

    def _get_xpath(self) -> Union[str, None]:
        """
        Подбирает атрибуты элемента и на их основе составляет XPath элемента.

        Returns:
            str: XPath элемента.
        """
        try:
            # Инициализация переменных
            element = self
            xpath = "//"
            attrs = element._get_attributes()
            element_type = attrs.get('class')
            except_attrs = ['hint',
                            'content-desc',
                            'selection-start',
                            'selection-end',
                            'extras',
                            ]

            # Формирование начальной части XPath в зависимости от наличия типа (класса) элемента
            if element_type:
                xpath += element_type
            else:
                xpath += "*"

            # Перебор атрибутов элемента для формирования остальной части XPath
            for key, value in attrs.items():
                if key in except_attrs:
                    continue

                # Добавление атрибута в XPath с соответствующим значением или без него, если значение равно None
                if value is None:
                    xpath += "[@{}]".format(key)
                else:
                    xpath += "[@{}='{}']".format(key, value)
            return xpath
        except (AttributeError, KeyError) as e:
            self.logger.error("Ошибка при формировании XPath: {}".format(str(e)))
        except Exception as e:
            self.logger.error("Неизвестная ошибка при формировании XPath: {}".format(str(e)))
        return None

    def _get_center(self, element: WebElement = None) -> Union[Tuple[int, int], None]:
        """
        Получение координат центра элемента.

        Returns:
            tuple: Координаты x и y центра элемента.
        """
        try:
            if element:
                # Получение границ элемента
                left, top, right, bottom = map(int,
                                               element.get_attribute('bounds').strip("[]").replace("][", ",").split(
                                                   ","))
            else:
                # Получение границ элемента
                left, top, right, bottom = map(int,
                                               self.get_attribute('bounds').strip("[]").replace("][", ",").split(","))
            # Расчет координат центра элемента
            x = (left + right) / 2
            y = (top + bottom) / 2

            return x, y
        except Exception as e:
            self.logger.error("some exception with _get_center(): {}".format(e))
            return None

    def _get_first_child_class(self) -> str:
        """
        Возвращает класс первого дочернего элемента, отличный от родительского
        """
        parent_element = self
        parent_class = parent_element.get_attribute('class')
        child_elements = parent_element.find_elements("xpath", "//*[1]")
        for i, child_element in enumerate(child_elements):
            child_class = child_element.get_attribute('class')
            if parent_class != child_class:
                return str(child_class)

    def _get_top_child_from_parent(self,
                                   locator: Union[Tuple[str, str], WebElement, Dict[str, str]]) -> \
            Union[WebElement, None]:
        """
        Возвращает самый верхний дочерний элемент родительского элемента.

        Args:
            locator: Кортеж / объект WebElement / словарь, представляющий локатор для дочернего элемента.

        Returns:
            Самый верхний дочерний элемент родительского элемента, указанному в локаторе дочерних элементов,
            или None, если соответствующий дочерний элемент не найден.
        """
        children = self._get_elements(locator=locator)
        if len(children) == 0:
            return None
        else:
            top_child = sorted(children, key=lambda x: x.location['y'])[0]
            return top_child

    def _get_bottom_child_from_parent(self,
                                      locator: Union[Tuple[str, str], WebElement, Dict[str, str]]) -> \
            Union[WebElement, None]:
        """
        Метод возвращает нижний дочерний элемент родительского элемента с заданным классом.
        Args:
            locator: Union[Tuple[str, str], WebElement, Dict[str, str]], локатор дочернего элемента.
        Returns:
            Найденный элемент или None, в случае его отсутствия.
        """
        children = self._get_elements(locator=locator)
        if len(children) == 0:
            return None
        else:
            bottom_child = sorted(children, key=lambda x: x.location['y'] + x.size['height'])[-1]
            return bottom_child
