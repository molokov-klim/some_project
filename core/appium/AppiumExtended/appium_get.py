# coding: utf-8
import time
from typing import Union, Dict, List, Tuple

from appium.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from core.appium.AppiumExtended.appium_base import AppiumBase
from core.appium.AppiumHelpers.appium_helpers import AppiumHelpers
from core.decorators.decorators import log_debug


class AppiumGet(AppiumBase):
    """
    Класс расширяющий Appium.
    Обеспечивает получение чего-либо со страницы.
    """

    def __init__(self):
        super().__init__()
        self.helper = None

    @log_debug()
    def _get_element(self,
                    locator: Union[Tuple, WebElement, 'WebElementExtended', Dict[str, str], str] = None,
                    by: Union[MobileBy, AppiumBy, By, str] = None,
                    value: Union[str, Dict, None] = None,
                    timeout_elem: int = 10,
                    timeout_method: int = 600,
                    elements_range: Union[Tuple, List[WebElement], Dict[str, str], None] = None,
                    contains: bool = False
                    ) -> \
            Union[WebElement, None]:
        """
        Метод обеспечивает поиск элемента в текущей DOM структуре.
        Должен принимать либо локатор, либо значения by и value.

        Usage:
            element = app._get_element(locator=("id", "foo")).
            element = app._get_element(element).
            element = app._get_element(locator={'text': 'foo'}).
            element = app._get_element(locator='/path/to/file/pay_agent.png').
            element = app._get_element(locator=part_image, elements_range={'class':'android.widget.FrameLayout', 'package':'ru.app.debug'}).
            element = app._get_element(by="id", value="ru.sigma.app.debug:id/backButton").
            element = app._get_element(by=MobileBy.ID, value="ru.sigma.app.debug:id/backButton").
            element = app._get_element(by=AppiumBy.ID, value="ru.sigma.app.debug:id/backButton").
            element = app._get_element(by=By.ID, value="ru.sigma.app.debug:id/backButton").

        Args:
            locator: tuple / WebElement / dict / str, определяет локатор элемента.
                tuple - локатор в виде ('атрибут', 'значение')
                WebElement - объект веб элемента
                dict - словарь, содержащий пары атрибут: значение
                str - путь до файла с изображением элемента.
            by: MobileBy, AppiumBy, By, str, тип локатора для поиска элемента (всегда в связке с value)
            value: str, dict, None, значение локатора или словарь аргументов, если используется AppiumBy.XPATH.
            timeout_elem: int, время ожидания элемента.
            timeout_method: int, время ожидания метода поиска элемента.
            elements_range: tuple, list, dict, None, ограничивает поиск элемента в указанном диапазоне
            (для поиска по изображению).
            contains: для поиска по dict, ищет элемент содержащий фрагмент значения

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

        # Объявление стратегии поиска элементов
        self.helper = AppiumHelpers(driver=self.driver)

        locator_handler = {
            # возвращает себя же
            WebElement: self.helper.handle_webelement_locator,
            # возвращает себя же
            'WebElementExtended': self.helper.handle_webelement_locator,
            # составляет локатор типа tuple из словаря с атрибутами искомого элемента
            dict: self.helper.handle_dict_locator,
            # производит поиск элементов по фрагменту изображения, возвращает список элементов
            str: self.helper.handle_string_locator,
        }

        # Цикл подготовки локатора и поиска элементов
        start_time = time.time()
        while not isinstance(locator, WebElement) and time.time() - start_time < timeout_method:
            # Выявление типа данных локатора для его подготовки
            locator_type = type(locator)
            # Если локатор типа tuple, то выполняется извлечение элементов
            if isinstance(locator, tuple):
                wait = WebDriverWait(driver=self.driver, timeout=timeout_elem)
                try:
                    element = wait.until(EC.presence_of_element_located(locator))
                    return element
                except WebDriverException as e:
                    self.logger.error(f"Элемент не обнаружен!\n"
                                      f"{locator=}\n"
                                      f"{timeout_elem=}\n\n" +
                                      "{}\n".format(e))
                    self.logger.error("page source ", self.driver.page_source)
                    return None
            # Выполнение подготовки локатора
            handler = locator_handler.get(locator_type)
            locator = handler(locator=locator, timeout=timeout_elem, elements_range=elements_range, contains=contains)
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


    def get_window_size(self):  # FIXME проанализировать и покрыть юнит тестом
        """
        This method should use the Appium driver to retrieve the size of the current window.
        """
        self.logger.debug(f"get_window_size()")
        try:
            window_size = self.driver.get_window_size()
            if window_size is not None:
                self.logger.debug(f"get_window_size(): {window_size}")
                return window_size
            else:
                self.logger.debug(f"get_window_size(): False")
                return False
        except Exception as e:
            self.logger.error("Failed to get window size: {}".format(e))
            return False

    def get_screenshot(self):  # FIXME проанализировать и покрыть юнит тестом
        self.logger.debug("get_screenshot()")
        try:
            screen = self.driver.get_screenshot_as_png()
            self.logger.debug(f"get_screenshot(): True")
            return screen
        except Exception as e:
            self.logger.error("get_screenshot(): Error: {}".format(e))
            return None
