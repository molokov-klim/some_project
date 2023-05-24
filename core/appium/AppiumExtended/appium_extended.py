# coding: utf-8
from typing import Union, Tuple, Dict, List

from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from core.appium.AppiumExtended.appium_is import AppiumIs
from core.appium.AppiumExtended.appium_scroll import AppiumScroll
from core.appium.AppiumExtended.appium_swipe import AppiumSwipe
from core.appium.AppiumExtended.appium_window import AppiumWindow

from core.appium.AppiumWebElementExtended.web_element_extended import WebElementExtended
from core.decorators.decorators import time_it


class AppiumExtended(AppiumSwipe, AppiumIs, AppiumScroll, AppiumWindow):
    """
    Класс работы с Appium.
    Обеспечивает работу с устройством
    """

    def __init__(self):
        super().__init__()

    def __del__(self):
        self.disconnect()

    @time_it
    def get_element(self,
                    locator: Union[Tuple, WebElementExtended, Dict[str, str], str] = None,
                    by: Union[MobileBy, AppiumBy, By, str] = None,
                    value: Union[str, Dict, None] = None,
                    timeout_elem: int = 10,
                    timeout_method: int = 600,
                    elements_range: Union[Tuple, List[WebElementExtended], Dict[str, str], None] = None,
                    contains: bool = True
                    ) -> Union[WebElementExtended, None]:
        element = super()._get_element(locator=locator,
                                       by=by,
                                       value=value,
                                       timeout_elem=timeout_elem,
                                       timeout_method=timeout_method,
                                       elements_range=elements_range,
                                       contains=contains)
        return WebElementExtended(element.parent, element.id)

    @time_it
    def get_elements(self,
                     locator: Union[Tuple, List[WebElement], Dict[str, str], str] = None,
                     by: Union[MobileBy, AppiumBy, By, str] = None,
                     value: Union[str, Dict, None] = None,
                     timeout_elements: int = 10,
                     timeout_method: int = 600,
                     elements_range: Union[Tuple, List[WebElement], Dict[str, str], None] = None,
                     contains: bool = True) -> \
            Union[List[WebElementExtended], List]:
        elements = super()._get_elements(locator=locator,
                                         by=by,
                                         value=value,
                                         timeout_elements=timeout_elements,
                                         timeout_method=timeout_method,
                                         elements_range=elements_range,
                                         contains=contains)
        elements_ext = []
        for element in elements:
            elements_ext.append(WebElementExtended(element.parent, element.id))
        return elements_ext

    @time_it
    def get_image_coordinate(self):
        """
        Возвращает координаты х у по изображению
        """
        raise NotImplementedError("This method is not implemented yet.")

    @time_it
    def get_image_in_image_coordinate(self):
        """
        Возвращает координаты x y (относительно экрана) по изображению внутри другого изображения
        """
        raise NotImplementedError("This function is not implemented yet.")

    @time_it
    def is_text_on_screen(self):
        """
        pytesseract to ocr
        """
        raise NotImplementedError("This function is not implemented yet.")

    @time_it
    def get_text_coordinate(self):
        """
        pytesseract to ocr

        """
        raise NotImplementedError("This function is not implemented yet.")

    @time_it
    def tap(self):
        """
        Тап по координатам / элементу / изображению
        """
        raise NotImplementedError("This method is not implemented yet.")

    # SWIPE

    @time_it
    def swipe(self, startx, starty, direction360, distancePX, hold: bool):
        """
        Свайпает
        от точки / элемента / изображения до точки / элемента / изображения
        от точки в направлении с дистанцией
        """
        raise NotImplementedError("This method is not implemented yet.")

    @time_it
    def swipe_two_fingers(self, direction360, distancePX, hold: bool):
        """
        Свайпает двумя пальцами
        от точки / элемента / изображения до точки / элемента / изображения
        от точки в направлении с дистанцией
        """
        raise NotImplementedError("This method is not implemented yet.")

    @time_it
    def swipe_three_fingers(self, direction360, distancePX, hold: bool):
        """
        Свайпает тремя пальцами
        от точки / элемента / изображения до точки / элемента / изображения
        от точки в направлении с дистанцией
        """
        raise NotImplementedError("This method is not implemented yet.")

    # DOM

    @time_it
    def get_element_contains(self):
        """
        Возвращает элемент содержащий определенный элемент
        """
        raise NotImplementedError("This method is not implemented yet.")

    @time_it
    def get_elements_contains(self):
        """
        Возвращает элементы содержащие определенный(е) элемент(ы)
        """
        raise NotImplementedError("This method is not implemented yet.")
