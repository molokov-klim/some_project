import logging
import os
from typing import Tuple, Dict, Union, List, Optional, Any

from appium.webdriver import WebElement
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
from core.appium.AppiumHelpers.appium_image import AppiumImage


class AppiumHelpers(AppiumImage):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def handle_webelement_locator(self,
                                  locator, timeout: int,
                                  elements_range=None,
                                  contains: bool = False) -> Union[
        WebElement, None]:
        """
        Обрабатывает локатор типа WebElement, возвращая его без дополнительных действий.

        Args:
            locator: Локатор типа WebElement.
            timeout: Время ожидания элемента в секундах (игнорируется).
            elements_range: Диапазон элементов для поиска (игнорируется).

        Returns:
            Union[WebElement, None]: Возвращает заданный WebElement.
        """
        return locator

    def handle_dict_locator(self,
                            locator,
                            timeout: int = 10,
                            elements_range=None,
                            contains: bool = False) -> Union[Tuple, None]:
        """
        Создает локатор xpath на основе переданного словаря-локатора Dict[str, str] и использует его для поиска элемента.

        Args:
            locator: Словарь-локатор типа Dict[str, str].
            timeout: Время ожидания элемента в секундах (игнорируется).
            elements_range: Диапазон элементов для поиска (игнорируется).
            contains: Ищет элемент содержащий фрагмент значения

        Returns:
            Union[Tuple, None]: Найденный WebElement или None, если элемент не найден.
        """
        if 'class' not in locator:
            xpath = "//*"
        else:
            xpath = "//" + locator['class']
        try:
            if contains:
                for attr, value in locator.items():
                    xpath += f"[contains(@{attr}, '{value}')]"
                new_locator = ("xpath", xpath)
                return new_locator
            else:
                for attr, value in locator.items():
                    xpath += f"[@{attr}='{value}']"
                new_locator = ("xpath", xpath)
                return new_locator
        except KeyError as e:
            self.logger.error(f"Ошибка dict: {locator}")
            self.logger.error("{}".format(e))
            return None

    def handle_string_locator(self,
                              locator,
                              timeout: int,
                              elements_range: Union[dict, list, tuple] = None,
                              contains: bool = False
                              ) -> Union[WebElement, None]:
        """
        Обрабатывает строковый локатор и возвращает найденный элемент.

        Args:
            locator: Строковый локатор для поиска элемента.
            timeout: Время ожидания элемента в секундах.
            elements_range: Диапазон элементов, в котором нужно искать ближайший к точке элемент.
                                                        Если параметр не указан, будет произведен поиск среди всех элементов на странице.

        Returns:
            Union[WebElement, None]: Найденный WebElement, либо None, если элемент не найден.
        """
        # поиск координат фрагмента изображения на экране
        with open('full_image.png', 'wb') as f:
            f.write(self.driver.get_screenshot_as_png())
        max_loc = self.find_coordinates_by_image(full_image='full_image.png', part_image=locator)
        x = max_loc[0]
        y = max_loc[1]
        os.remove('full_image.png')

        # определение списка элементов для поиска
        elements = None
        locator = ("xpath", "//*")
        if isinstance(elements_range, dict):
            locator = self.handle_dict_locator(elements_range)
        elif isinstance(elements_range, list):
            elements = elements_range
        elif isinstance(elements_range, tuple):
            locator = elements_range
        if not elements:
            elements = self.driver.find_elements(*locator)

        # Поиск ближайшего к координатам элемента
        element = self.get_closest_element_to_point(x=x, y=y, elements=elements)
        if not element:
            self.logger.error(f"Элемент не обнаружен\n"
                              f"{locator=}\n"
                              f"{elements_range=}\n")
        return element

    def get_closest_element_to_point(self, x, y,
                                     by=None,
                                     value=None,
                                     elements=None,
                                     ) -> Union[WebElement, None]:
        """
        Ищет ближайший элемент к заданным координатам на экране.

        Args:
            x (int): Координата по оси X.
            y (int): Координата по оси Y.
            by (str, optional): Критерий поиска элементов. Используется совместно с параметром `value`.
            value (str, optional): Значение для критерия поиска элементов. Используется совместно с параметром `by`.
            elements_range (Union[Tuple, List[WebElement], Dict[str, str], None], optional):
                Список элементов или параметры локатора для поиска элементов. Если параметр не задан,
                поиск элементов будет выполнен на всей странице.

        Returns:
            Optional[WebElement]: Найденный элемент, или `None`, если ни один элемент не был найден.
        """

        if elements is None:
            return None
        closest_element = None
        closest_distance = float("inf")

        for element in elements:
            left, top, right, bottom = map(int,
                                           element.get_attribute('bounds').strip("[]").replace("][", ",").split(","))
            distance = ((x - left) ** 2 + (y - top) ** 2) ** 0.5

            if distance < closest_distance and left <= x and top <= y:
                closest_distance = distance
                closest_element = element

        return closest_element

    # def handle_tuple_locator_elements(self,
    #                                   locator: Tuple[str, str],
    #                                   timeout: int = 10,
    #                                   elements_range: Union[Tuple, List[WebElement], Dict[str, str], None] = None) -> \
    #         Union[List[WebElement], None]:
    #     """
    #     Обрабатывает локатор типа tuple и возвращает все найденные элементы.
    #
    #     Args:
    #         locator (Tuple[str, str]): Локатор типа tuple для поиска элементов.
    #         timeout (int): Максимальное время ожидания появления элементов в секундах.
    #
    #     Returns:
    #         Union[WebElement, None]: Найденные элементы в виде списка, либо None, если элементы не найдены.
    #     """
    #     wait = WebDriverWait(driver=self.driver, timeout=timeout)
    #     try:
    #         elements = wait.until(EC.presence_of_all_elements_located(locator))
    #         return elements
    #     except WebDriverException as e:
    #         self.logger.error(f"Элемент не обнаружен!\n"
    #                           f"{locator=}\n"
    #                           f"{timeout=}\n\n" +
    #                           "{}\n".format(e))
    #     return None

    def handle_webelement_locator_elements(self,
                                           locator: List[WebElement],
                                           timeout: int,
                                           elements_range: Union[
                                               Tuple, List[WebElement], Dict[str, str], None] = None,
                                     contains: bool = True) -> \
            Union[List[WebElement], None]:
        """
        Обрабатывает локатор типа WebElement и возвращает его без дополнительных действий.

        Args:
            locator (WebElement): Локатор типа WebElement для обработки.
            timeout (int): Время ожидания элемента (игнорируется).

        Returns:
            Union[WebElement, None]: Заданный WebElement.
        """
        if not isinstance(locator[0], WebElement):
            self.logger.error(f"Элементы списка не WebElement\n"
                              f"{locator=}\n"
                              f"{timeout=}\n\n")
            print("ERROR in handle_webelement_locator_elements()")
            return None
        return locator

    def handle_dict_locator_elements(self,
                                     locator: Dict[str, str],
                                     timeout: int = 10,
                                     elements_range: Union[Tuple, List[WebElement], Dict[str, str], None] = None,
                                     contains: bool = True) -> \
            Optional[Tuple[str, str]]:
        """
        Обрабатывает локатор типа Dict[str, str], создавая на его основе локатор типа xpath и используя его для поиска элемента.
        XPATH нельзя подавать в качестве ключа.

        Args:
            locator (Dict[str, str]): Локатор типа Dict[str, str].
            timeout (int): Время ожидания элемента.

        Returns:
            Union[WebElement, None]: Найденный WebElement в виде списка, либо None, если элемент не найден.
        """
        if 'class' not in locator:
            xpath = "//*"
        else:
            xpath = "//" + locator['class']
        try:
            if contains:
                for attr, value in locator.items():
                    xpath += f"[contains(@{attr}, '{value}')]"
                new_locator = ("xpath", xpath)
                return new_locator
            else:
                for attr, value in locator.items():
                    xpath += f"[@{attr} = '{value}']"
                new_locator = ("xpath", xpath)
                return new_locator
        except KeyError as e:
            self.logger.error(f"Ошибка dict: {locator}")
            self.logger.error("{}".format(e))
            return None

    def handle_string_locator_elements(self,        # FIXME оптимизировать используя силу xpath и/или xml tree
                                       locator: str,
                                       timeout: int = 10,
                                       elements_range: Union[Tuple, List[WebElement], Dict[str, str], None] = None,
                                       cv_threshold: float = 0.7,  # веса откалиброваны
                                       coord_threshold: int = 1,
                                     contains: bool = True) -> \
            Union[List, None]:
        """
        Обрабатывает строковый локатор, используя его как путь до файла с изображением.
        Находит элемент на странице, соответствующий указанному изображению.
        Настоятельно рекомендуется использовать диапазон поиска elements_range.

        Args:
            locator (str): Путь до файла с изображением.
            timeout (int): Максимальное время ожидания появления элемента в секундах.

        Returns:
            Union[List[Tuple], None]: Найденные элементы, либо None, если элементы не найдены.
        """
        #  Сохранение скриншота изображения и поиск координат совпадающих изображений
        with open('full_image.png', 'wb') as f:
            f.write(self.driver.get_screenshot_as_png())
        max_locs = self.find_many_coordinates_by_image(full_image='full_image.png',
                                                       part_image=locator,
                                                       cv_threshold=cv_threshold,
                                                       coord_threshold=coord_threshold)
        if not max_locs:
            self.logger.error("Элементы не обнаружены")
            return None
        os.remove('full_image.png')

        # определение списка элементов для поиска
        elements = None
        locator = ("xpath", "//*")
        if isinstance(elements_range, dict):
            locator = self.handle_dict_locator(elements_range)
        elif isinstance(elements_range, list):
            elements = elements_range
        elif isinstance(elements_range, tuple):
            locator = elements_range
        if not elements:
            elements = self.driver.find_elements(*locator)

        # Поиск ближайших к координатам элементов
        result = []
        for max_loc in max_locs:
            x = max_loc[0]
            y = max_loc[1]
            element = self.get_closest_element_to_point(x=x, y=y, elements=elements)
            result.append(element)

        # удаление родительских элементов
        result = self.remove_nesting(result)
        # сортировка по координатам
        result = self.sort_elements_by_bounds(result)

        # debug save to folder
        for index, element in enumerate(result):
            file_path = os.path.join('unit_test', 'str_elements', f'screenshot_{index}.png')
            with open(file_path, 'wb') as file:
                file.write(element.screenshot_as_png)

        return result

    def add_bounds(self, elements: List[WebElement]) -> list[list[Union[WebElement, Any]]]:
        """
        Добавляет координаты в список элементов
        """
        elements_with_bounds = []
        for element in elements:
            try:
                coord = element.get_attribute("bounds")
                left, top, right, bottom = map(int, coord[1:-1].replace("][", ",").split(','))
                elements_with_bounds.append([element, left, top, right, bottom])
            except WebDriverException as e:
                self.logger.error("Error sorting elements: {}".format(e))
        return elements_with_bounds

    @staticmethod
    def remove_bounds(elements_with_bounds):
        """
        Удаляет координаты из списка элементов. Работает только в связке с add_bounds.
        """
        elements_without_bounds = [lst[0] for lst in elements_with_bounds]
        return elements_without_bounds

    def sort_elements_by_bounds(self, elements: List[WebElement], desc: bool = False) -> Optional[List[WebElement]]:
        """
        Сортирует список из WebElement, по значению их верхней координаты.

        Args:
            elements (List[WebElement]): список из WebElement объектов.
            desc (bool): Если False (default), сортирует в обратном порядке.

        Returns:
            List[WebElement]: сортированный список WebElement объектов.
            Если подан не корректный аргумент elements, возвращает None.

        Usage:
            elements = driver.find_elements_by_xpath("//div[@class='my-class']")
            sorted_elements = sort_elements_by_bounds(elements, desc=False)
        """
        if not elements or not isinstance(elements, list) or not isinstance(elements[0], WebElement):
            self.logger.error(f"Список невозможно сортировать, {elements=}")
            return None

        elements_with_coords = self.add_bounds(elements)
        sorted_elements = sorted(elements_with_coords, key=lambda x: x[2], reverse=desc)
        result = self.remove_bounds(sorted_elements)
        return result

    def remove_nesting(self, elements) -> List[WebElement]:     # FIXME реализовать через Axis а не координаты
        """
        Проверяет вхождение элементов в другие элементы по координатам.
        При обнаружении удаляет большие по размеру.
        """
        # удаление дубликатов
        elements = list(set(elements))

        # добавление координат
        elements_with_coords = self.add_bounds(elements)

        # поиск элементов имеющих дочерние (по координатам, точное вхождение, без учета оверлапса)
        for index, el1 in enumerate(elements_with_coords):
            # координаты 0.0 в левом верхнем углу экрана
            el1_left_top_x = el1[1]
            el1_left_top_y = el1[2]
            el1_right_bottom_x = el1[3]
            el1_right_boot_y = el1[4]
            for el2 in elements_with_coords:
                el2_left_top_x = el2[1]
                el2_left_top_y = el2[2]
                el2_right_bottom_x = el2[3]
                el2_right_boot_y = el2[4]
                if el1_left_top_x < el2_left_top_x and el1_left_top_y < el2_left_top_y and el1_right_bottom_x > \
                        el2_right_bottom_x and el1_right_boot_y > el2_right_boot_y:
                    elements_with_coords[index] = [el1[0], el1[1], el1[2], el1[3], el1[4], 'parent']  # метка
        elements_no_parent = []

        # формирование списка не имеющих родительских элементов (по координатам)
        for element in elements_with_coords:
            if len(element) < 6:
                elements_no_parent.append(element)

        # удаление координат, приведение к списку элементов
        result = self.remove_bounds(elements_no_parent)
        return result

    def find_only_children(self, element, elements):
        return

        # def remove_related_elements(self, elements: List[WebElement], depth: int = 1) -> List[WebElement]:
    #     """
    #     Удаляет из List[WebElement] все связанные отношением предок-потомок элементы,
    #     кроме последнего дочернего элемента. Проверка осуществляется на указанную глубину.
    #     """
    #     filtered_elements = set()
    #     parent_last_child = {}
    #
    #     for element in elements:
    #         if element not in filtered_elements:
    #             is_related = False
    #             for other_element in elements:
    #                 if element != other_element and self.is_parenthood(element, other_element, depth):
    #                     is_related = True
    #                     break
    #             if not is_related:
    #                 filtered_elements.add(element)
    #             else:
    #                 parent_element = element.find_element(By.XPATH, '..')
    #                 if parent_element not in parent_last_child:
    #                     last_child = parent_element.find_elements(By.XPATH, '*')[-1]
    #                     parent_last_child[parent_element] = last_child
    #                 if element != parent_last_child[parent_element]:
    #                     filtered_elements.add(element)
    #
    #     return list(filtered_elements)
    #
    # def is_parenthood(self, parent_element: WebElement, child_element: WebElement, depth: int = 1) -> bool:
    #     """
    #     Возвращает True, если родительский элемент содержит дочерний элемент на указанной глубине.
    #     """
    #
    #     def search_children(element, current_depth):
    #         if element == child_element:
    #             return True
    #         if current_depth < depth:
    #             for child_locator in element.find_elements():
    #                 if search_children(child_locator, current_depth + 1):
    #                     return True
    #         return False
    #
    #     return search_children(parent_element, 1)
