# coding: utf-8
import os
import time
from typing import Union, List, Dict, Tuple, Optional
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core.appium.AppiumExtended.appium_get import AppiumGet
from core.appium.AppiumHelpers.appium_helpers import AppiumHelpers
from core.decorators.decorators import log_debug


class AppiumElements(AppiumGet):  # TODO доделать
    """
    Класс работы с Appium.
    Обеспечивает работу с элементами
    """

    def __init__(self):
        super().__init__()

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
        При locator:str настоятельно рекомендуется использовать диапазон поиска elements_range.

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
            timeout_elements: #TODO fill me
            timeout_method: #TODO fill me
            elements_range: #TODO fill me

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
                              f"{timeout_method=}\n")
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
            # Выявление типа данных локатора для его подготовки
            locator_type = type(locator)
            # Если локатор типа tuple, то выполняется извлечение элементов
            if isinstance(locator, tuple):
                wait = WebDriverWait(driver=self.driver, timeout=timeout_elements)
                try:
                    element = wait.until(EC.presence_of_all_elements_located(locator))
                    return element
                except WebDriverException as e:
                    self.logger.error(f"Элемент не обнаружен!\n"
                                      f"{locator=}\n"
                                      f"{by=}\n"
                                      f"{value=}\n"
                                      f"{timeout_elements=}\n"
                                      f"{timeout_method=}\n\n" +
                                      "{}\n".format(e))
                    return None
            # Выполнение подготовки локатора
            handler = locator_handler.get(locator_type)
            locator = handler(locator=locator,
                              timeout=timeout_elements,
                              elements_range=elements_range,
                              contains=contains)
        # Подбирает результат после поиска по изображению
        if isinstance(locator, list):
            return locator
        self.logger.error(f"\nЧто-то пошло не так\n"
                          f"{locator=}\n"
                          f"{by=}\n"
                          f"{value=}\n"
                          f"{timeout_elements=}\n"
                          f"{timeout_method=}\n")
        return None


    def _get_elements_attributes(self,
                                 locator: Union[tuple, List[WebElement]],
                                 attrs: Union[str, List[str]],
                                 timeout=10) -> \
            Union[List[str], List[Dict[str, str]], None]:
        """
        Извлекает значение одного или нескольких атрибутов из списка веб-элементов.

        Args:
            locator (Union[tuple, List[WebElement]]): Поисковая стратегия и локатор веб-элементов.
                Может быть кортежем (стратегия, локатор) или списком веб-элементов.
            attrs (Union[str, List[str]]): Имя или список имен атрибутов для извлечения из веб-элементов.
            timeout (int): Время ожидания поиска веб-элементов (в секундах).

        Returns:
            Union[List[str], List[Dict[str, str]], None]: Список значений атрибутов или список словарей
            (имя атрибута и его значение) для каждого веб-элемента или None в случае ошибки.
        """
        elements = self.get_elements(locator=locator, timeout=timeout)
        attribute_values = []
        for element in elements:
            try:
                if isinstance(attrs, str):
                    attribute_values.append(element.get_attribute(attrs))
                elif isinstance(attrs, List):
                    kv = {}
                    for attr in attrs:
                        kv[attr] = (element.get_attribute(attr))
                    attribute_values.append(kv)
                else:
                    self.logger.error(
                        f"Недопустимый тип данных атрибута {type(attrs)=}")
                    return None
            except WebDriverException:
                self.logger.error(
                    f"{attrs=}' принят недопустимый атрибут элемента")
                return None
        return attribute_values
