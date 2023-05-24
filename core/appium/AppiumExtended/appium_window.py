# coding: utf-8
import time
from typing import Union, List, Dict

from appium.webdriver.webelement import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from core.appium.AppiumExtended.appium_elements import AppiumElements
from core.appium.AppiumExtended.appium_get import AppiumGet
from core.decorators.decorators import log_debug


class AppiumWindow(AppiumElements):
    """
    Класс работы с Appium.
    Обеспечивает работу с окнами
    """

    def __init__(self):
        super().__init__()

    # @log_debug()
    # def is_window(self,
    #               image: str = None,
    #               locators: List = None,
    #               by: Union[MobileBy, AppiumBy, By, str] = None,
    #               value: Union[str, Dict, None] = None,
    #               timeout_elem: int = 10, ) -> bool:
    #     """
    #     Проверяет, присутствует ли окно или элемент на экране.
    #
    #     Usage:
    #         driver.is_window(locators=[(By.ID, 'my_element')])
    #         driver.is_window(locators=[(By.ID, 'my_element'), (By.CLASS_NAME, 'my_class')])
    #         driver.is_window(image='my_image.png')
    #
    #     Args:
    #         image: Строка, содержащая имя файла частичного изображения для поиска.
    #         locators: Список содержащий tuple / WebElement / dict / str, определяет локатор.
    #             tuple - локатор в виде ('атрибут', 'значение')
    #             WebElement - объект веб элемента
    #             dict - словарь, содержащий пары атрибут: значение
    #             str - путь до файла с изображением элемента.
    #         by: Тип локатора для поиска элемента (всегда в связке с value)
    #         value: Значение локатора или словарь аргументов, если используется AppiumBy.XPATH.
    #         timeout_elem: время ожидания элемента.
    #
    #     Returns:
    #         bool: True, если изображение или элемент(ы) присутствует на экране; False в противном случае.
    #     """
    #     if not any([image, locators, by, value]):
    #         self.logger.error(f"Некорректные аргументы!\n"
    #                           f"{locators=}\n"
    #                           f"{by=}\n"
    #                           f"{value=}\n"
    #                           f"{timeout_elem=}\n")
    #         return False
    #     if not locators and image:
    #         if not self.is_image_on_the_screen(image):
    #             return False
    #     if not locators and (by and value):
    #         locators = [(by, value)]
    #     if locators:
    #         for locator in locators:
    #             if not isinstance(self.get_element(locator=locator, timeout_elem=timeout_elem), WebElement):
    #                 return False
    #     return True
    #
    # def wait_for_window(self,
    #                     image: str = None,
    #                     locators: List = None,
    #                     by: Union[MobileBy, AppiumBy, By, str] = None,
    #                     value: Union[str, Dict, None] = None,
    #                     timeout: int = 30,
    #                     poll_frequency: float = 0.5) -> bool:
    #     """
    #     Ожидает появления изображения или элемента на экране.
    #
    #     Usage:
    #         app.wait_for_window(
    #             locators=[(By.ID, 'my_element')],
    #             timeout=10,
    #             poll_frequency=0.5
    #         )
    #         app.wait_for_window(
    #             image='my_image.png',
    #             timeout=20,
    #             poll_frequency=1
    #         )
    #         app.wait_for_window(
    #             by=By.XPATH,
    #             value="//input[@name='email'][@type='text']",
    #             timeout=15,
    #             poll_frequency=0.5
    #         )
    #
    #     Args:
    #         image: Строка, содержащая имя файла частичного изображения для поиска.
    #         locators: Список содержащий tuple / WebElement / dict / str, определяет локатор.
    #             tuple - локатор в виде ('атрибут', 'значение')
    #             WebElement - объект веб элемента
    #             dict - словарь, содержащий пары атрибут: значение
    #             str - путь до файла с изображением элемента.
    #         by: Тип локатора для поиска элемента (всегда в связке с value).
    #         value: Значение локатора или словарь аргументов, если используется AppiumBy.XPATH.
    #         timeout: Время ожидания (сек.).
    #         poll_frequency: Частота проверки.
    #
    #     Returns:
    #         bool: True если изображение или элемент отобразились, False в ином случае.
    #     """
    #     start_time = time.time()
    #     while time.time() - start_time < timeout:
    #         if self.is_window(
    #                 image=image,
    #                 locators=locators,
    #                 by=by,
    #                 value=value
    #         ):
    #             return True
    #         time.sleep(poll_frequency)
    #     return False



