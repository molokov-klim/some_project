# coding: utf-8
from typing import Union, List, Dict, Tuple

from appium.webdriver import WebElement
from selenium.common import WebDriverException, NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.appium.AppiumExtended.appium_elements import AppiumElements
from core.decorators.decorators import log_debug


class AppiumDOM(AppiumElements):
    """
    Класс работы с Appium.
    Обеспечивает работу с элементами в DOM-структуре
    """

    def __init__(self):
        super().__init__()
        self.parent = None

    # @log_debug()
    # def get_parent_of_element(self,
    #                           child_locator: Union[Tuple[str, str], WebElement, Dict[str, str], str],
    #                           depth: int = 999) -> Union[WebElement, None]:
    #     """
    #     Метод находит родительский элемент.
    #     Ищет по координатам верхнего левого угла
    #     """
    #     child_element = self.get_element(child_locator)
    #     left, top, right, bottom = map(int, child_element.get_attribute('bounds').strip("[]").replace("][", ",").split(","))
    #     parent_element = self.get_closest_element_to_point(x=left-1, y=top-1)
    #     return parent_element
    #
    #
    # def is_element_contains_child(self,
    #                               parent_locator: Union[Tuple[str, str], WebElement, Dict[str, str], str],
    #                               child_locator: Union[Tuple[str, str], WebElement, Dict[str, str], str]) -> bool:
    #     """
    #     Проверяет, содержит элемент указанный элемент
    #     """
    #     try:
    #         parent_element = self.get_element(locator=parent_locator)
    #
    #         return True
    #     except NoSuchElementException:
    #         return False
    #
    #
    # @log_debug()
    # def get_element_from_element(self,
    #                              parent: Union[Tuple[str, str], WebElement, Dict[str, str]],
    #                              child: Union[Tuple[str, str], WebElement, Dict[str, str]]) -> \
    #         Union[WebElement, None]:
    #     """
    #     Метод для получения дочернего элемента из родительского элемента.
    #     :param parent: tuple, WebElement, dict
    #         Локатор или элемент родительского элемента.
    #     :param child: tuple, WebElement, dict
    #         Локатор или элемент дочернего элемента.
    #     :return: WebElement or None
    #         Возвращает элемент дочернего элемента или None, если элемент не найден.
    #     """
    #     parent_elem = self.get_element(locator=parent)
    #     if isinstance(child, Tuple):
    #         children_elements = parent_elem.find_elements(*child)
    #     elif isinstance(child, WebElement):
    #         child_elem = child
    #     elif isinstance(child, Dict):
    #         xpath = "//*"
    #         for attr, value in child.items():
    #             xpath += f"[contains(@{attr}, '{value}')]"
    #         locator = ("xpath", xpath)
    #         child_elem = parent_elem.find_element(*locator)
    #     else:
    #         self.logger.error(f"Элемент не найден, {child=}")
    #         child_elem = None
    #     return child_elem
    #
    # @log_debug()
    # def get_elements_from_element(self,
    #                               parent: Union[Tuple[str, str], WebElement, Dict[str, str]],
    #                               child: Union[Tuple[str, str], WebElement, Dict[str, str]]) -> \
    #         Union[List[WebElement], None]:
    #     """
    #     Метод для получения дочернего элемента из родительского элемента.
    #     :param parent: tuple, WebElement, dict
    #         Локатор или элемент родительского элемента.
    #     :param child: tuple, WebElement, dict
    #         Локатор или элемент дочернего элемента.
    #     :return: list of WebElements or None
    #         Возвращает список дочерних элементов или None, если элементы не найдены.
    #     """
    #     parent_elem = self.get_element(locator=parent)
    #     if isinstance(child, Tuple):
    #         child_elem = parent_elem.find_elements(*child)
    #     elif isinstance(child, WebElement):
    #         child_elem = child
    #     elif isinstance(child, Dict):
    #         xpath = "//*"
    #         for attr, value in child.items():
    #             xpath += f"[contains(@{attr}, '{value}')]"
    #         locator = ("xpath", xpath)
    #         child_elem = parent_elem.find_elements(*locator)
    #     else:
    #         self.logger.error(f"Элемент не найден, {child=}")
    #         child_elem = None
    #     return child_elem
    #
    # @log_debug()
    # def get_top_child_from_parent(self,
    #                               parent: Union[Tuple[str, str], WebElement, Dict[str, str]],
    #                               child: Union[Tuple[str, str], WebElement, Dict[str, str]]) -> \
    #         Union[WebElement, None]:
    #     """
    #     Возвращает самый верхний дочерний элемент родительского элемента.
    #
    #     Args:
    #         parent: Кортеж (состоящий из стратегии локатора и значения локатора) / объект WebElement / словарь,
    #                 представляющий локатор для родительского элемента.
    #         child: Кортеж / объект WebElement / словарь, представляющий локатор для дочернего элемента.
    #
    #     Returns:
    #         Самый верхний дочерний элемент родительского элемента, указанному в локаторе дочерних элементов,
    #         или None, если соответствующий дочерний элемент не найден.
    #
    #     Usage:
    #         locator = (By.ID, 'my_parent')
    #         child_locator = (By.CLASS_NAME, 'my-button-class')
    #         top_button = driver.get_top_child_from_parent(locator, child_locator)
    #     """
    #     children = self.get_elements_from_element(parent=parent, child=child)
    #     if len(children) == 0:
    #         return None
    #     else:
    #         top_child = sorted(children, key=lambda x: x.location['y'])[0]
    #         return top_child
    #
    # @log_debug()
    # def get_bottom_child_from_parent(self,
    #                                  parent: Union[Tuple[str, str], WebElement, Dict[str, str]],
    #                                  child: Union[Tuple[str, str], WebElement, Dict[str, str]]) -> \
    #         Union[WebElement, None]:
    #     """
    #     Метод возвращает нижний дочерний элемент родительского элемента с заданным классом.
    #     Args:
    #         parent: WebElement, родительский элемент.
    #         child: str, имя класса дочернего элемента.
    #     Returns:
    #         Найденный элемент или None, в случае его отсутствия.
    #     """
    #     children = self.get_elements_from_element(parent=parent, child=child)
    #     if len(children) == 0:
    #         return None
    #     else:
    #         bottom_child = sorted(children, key=lambda x: x.location['y'] + x.size['height'])[-1]
    #         return bottom_child
    #
    #
    #
    # @log_debug()
    # def is_parent(self, parent_locator, child_locator, depth: int = 1) -> bool:
    #     """
    #     Возвращает True, если родительский элемент содержит дочерний элемент на указанной глубине.
    #     """
    #     parent_element = self.get_element(parent_locator)
    #     child_element = self.get_element(child_locator)
    #
    #     def search_children(element, current_depth):
    #         if element == child_element:
    #             return True
    #         if current_depth < depth:
    #             for child in element.find_elements():
    #                 if search_children(child, current_depth + 1):
    #                     return True
    #         return False
    #
    #     return search_children(parent_element, 1)
    #
    # @log_debug()
    # def is_contains_element(self, parent_locator, child_locator, depth: int = 1) -> bool:
    #     """
    #     Возвращает True, если дочерний элемент содержится внутри родительского элемента на указанной глубине.
    #     """
    #     parent_element = self.get_element(parent_locator)
    #     child_element = self.get_element(child_locator)
    #
    #     def search_children(element, current_depth):
    #         if element == parent_element:
    #             return True
    #         if current_depth < depth:
    #             parent = element.find_element(*parent_locator)
    #             if search_children(parent, current_depth + 1):
    #                 return True
    #         return False
    #
    #     return search_children(child_element, 1)
    #
    #
    #
    # def get_first_child_class(self, parent_locator) -> str:
    #     """
    #     Возвращает класс первого дочернего элемента, отличный от родительского
    #     """
    #     parent_element = self.get_element(locator=parent_locator)
    #     parent_class = parent_element.get_attribute('class')
    #     child_elements = parent_element.find_elements("xpath", "//*[1]")
    #     for i, child_element in enumerate(child_elements):
    #         child_class = child_element.get_attribute('class')
    #         if parent_class != child_class:
    #             return str(child_class)
