# coding: utf-8
import logging
import os
from typing import Union, List, Tuple

import cv2
import numpy as np
from appium.webdriver import WebElement

import config
from core.appium.AppiumExtended.appium_base import AppiumBase


class AppiumImage(object):
    """
    Класс работы с Appium.
    Обеспечивает работу с изображениями
    """

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(config.LOGGER_NAME)

    def is_image_on_the_screen(self,
                               part_image: str = None,
                               threshold: float = 0.9) -> bool:
        """
        Сравнивает, присутствует ли заданное изображение на экране.

        Args:
            part_image: Строка, содержащая имя файла частичного изображения для поиска.
            threshold: Пороговое значение схожести части изображения со снимком экрана

        Returns:
            Логическое значение, указывающее, было ли частичное изображение найдено на экране.
        """

        screenshot = self.driver.get_screenshot_as_png()

        # Чтение снимка экрана и частичного изображения
        full_image = cv2.imdecode(np.frombuffer(screenshot, np.uint8), cv2.IMREAD_COLOR)
        small_image = cv2.imread(part_image, cv2.IMREAD_COLOR)

        # Сопоставление частичного изображения и снимка экрана
        result = cv2.matchTemplate(full_image, small_image, cv2.TM_CCOEFF_NORMED)

        # Извлечение коэффициента схожести и координат схожего участка
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        # Логирование
        self.logger.debug(f"Коэффициент схожести изображения: {max_val}")

        # Сравнение коэффициента схожести и порогового значения
        if max_val >= threshold:
            return True
        else:
            return False

    def find_coordinates_by_image(self,
                                  full_image: str,
                                  part_image: str = None,
                                  threshold: float = 0.7) -> Union[Tuple, None]:
        """
        Находит расположение частичного изображения внутри полного изображения.

        Usage:
            full_image = "path/to/full/image.png"
            part_image = "path/to/partial/image.png"
            threshold = 0.8
            location = image_finder.find_coordinates_by_image(full_image, part_image, threshold)

        Args:
            full_image (str): Путь к файлу полного изображения.
            part_image (str): Путь к файлу частичного изображения, которое нужно найти внутри полного изображения.
            threshold (float, опционально): Пороговое значение для определения того, найдено ли частичное изображение внутри
                полного изображения. По умолчанию равно 0.7.

        Returns:
            Union[Tuple, None]: Кортеж, представляющий координаты (x,y) верхнего левого угла частичного изображения внутри
                полного изображения. Возвращает None, если частичное изображение не найдено в полном изображении.
        """

        big_image = cv2.imread(full_image)
        small_image = cv2.imread(part_image)

        # Find partial image within full image
        result = cv2.matchTemplate(big_image, small_image, cv2.TM_CCOEFF_NORMED)

        # Get maximum value and location of match
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if not max_val >= threshold:
            return None

        return max_loc

    def find_many_coordinates_by_image(self,
                                       full_image: str,
                                       part_image: str,
                                       cv_threshold: float = 0.7,
                                       coord_threshold: int = 5) -> \
            Union[List[Tuple], None]:
        """
        Находит все вхождения частичного изображения внутри полного изображения.

        Args:
        full_image (str): путь к файлу полного изображения.
        part_image (str): путь к файлу частичного изображения, которое нужно найти внутри полного изображения.
        threshold (float, optional): минимальный порог совпадения, необходимый для считывания совпадения допустимым.

        Returns:
        list of tuples: список кортежей, содержащий расположение каждого найденного совпадения.
        """

        big_image = cv2.imread(full_image, cv2.IMREAD_GRAYSCALE)
        small_image = cv2.imread(part_image, cv2.IMREAD_GRAYSCALE)

        # Find partial image within full image
        result = cv2.matchTemplate(big_image, small_image, cv2.TM_CCOEFF_NORMED)

        # Get all matches above threshold
        locations = np.where(result >= cv_threshold)
        matches = list(zip(*locations[::-1]))

        matches = self._exclude_too_close_from_list_tuple(matches, coord_threshold=coord_threshold)

        if not matches:
            self.logger.error(f"No matches found for {part_image=}")
            return None
        matches = sorted(matches, key=lambda x: x[1])  # сортировка сверху вниз
        return matches




    def _exclude_too_close_from_list_tuple(self, list_of_tuples: List[Tuple], coord_threshold: int = 5) -> List[Tuple]:
        """
        Удаляет из списка кортежей те кортежи, которые слишком близки друг к другу в пределах заданного порога.

        Args:
            list_of_tuples: список кортежей, которые нужно отфильтровать.
            threshold: целое число, представляющее максимальное различие между значениями x и y двух кортежей,
            чтобы они считались слишком близкими друг к другу. По умолчанию равно 2.

        Returns:
            Список кортежей, которые не слишком близки друг к другу, в заданном пороге.
        """
        unique_list = []
        for i, (x1, y1) in enumerate(list_of_tuples):
            exclude = False
            for (x2, y2) in unique_list:
                if abs(x1 - x2) <= coord_threshold and abs(y1 - y2) <= coord_threshold:
                    exclude = True
                    break
            if not exclude:
                unique_list.append((x1, y1))
        return unique_list



