# coding: utf-8
import logging

from appium.webdriver import WebElement

import config

from core.adb import adb
from core.appium.AppiumWebElementExtended.web_element_get import WebElementGet
from core.decorators.decorators import wait_for_window_change
from core.utils.utils import find_coordinates_by_vector


class WebElementAdbActions(WebElementGet):
    """
    Класс для выполнения adb-действий с элементами.
    Наследуется от класса WebElementGet.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = args[0]
        self.logger = logging.getLogger(config.LOGGER_NAME)

    def _adb_tap(self,
                 decorator_args: dict = None,
                 wait: bool = False) -> bool:
        """
        Выполняет нажатие на элемент с помощью adb.

        Аргументы:
            decorator_args (dict): Дополнительные аргументы для использования в декораторе.
                timeout_window (int): Время ожидания нового окна (умножается на количество попыток).
                tries (int): Количество попыток нажатия (по умолчанию 3).
            wait (bool): Флаг, указывающий, нужно ли ожидать изменения окна.

        Возвращает:
            bool: True, если нажатие выполнено успешно; False в противном случае.
        """
        if wait:
            # Если нужно ожидать изменения окна.
            if not decorator_args:
                decorator_args = {"timeout_window": 5,
                                  "tries": 5}
            return self._adb_tap_to_element_and_wait(decorator_args=decorator_args)
        else:
            # Если не нужно ожидать изменения окна.
            return self._adb_tap_to_element()

    def _adb_tap_to_element(self) -> bool:
        return self.__adb_tap()

    @wait_for_window_change()
    def _adb_tap_to_element_and_wait(self,
                                     decorator_args: dict = None) -> bool:
        return self.__adb_tap()

    def __adb_tap(self) -> bool:
        """
        Выполняет нажатие на элемент с помощью adb.

        Возвращает:
            bool: True, если нажатие выполнено успешно, False в противном случае.
        """
        try:
            x, y = self._get_center()
            return adb.tap(x=x, y=y)
        except Exception:
            return False

    def _adb_multi_tap(self,
                       decorator_args: dict = None,
                       wait: bool = False) -> bool:
        """
        Выполняет несколько нажатий с помощью adb.

        Args:
            decorator_args (dict, optional): Дополнительные аргументы для декоратора.
                По умолчанию None.
                Если None то будут преобразованы в decorator_args = {"timeout_window": 5, "tries": 5}), где
                    timeout_window: время ожидания изменения окна в секундах.
                    tries: количество попыток (выполнения настоящего метода) для изменения окна.
            wait (bool, optional): Флаг, указывающий, нужно ли ожидать изменение окна после нажатия.
                По умолчанию False.

        Returns:
            bool: True, если нажатие выполнено успешно, False в противном случае.
        """
        if wait:
            if not decorator_args:
                decorator_args = {"timeout_window": 5,
                                  "tries": 5}
            return self._adb_multi_tap_to_element_and_wait(decorator_args=decorator_args)
        else:
            return self._adb_multi_tap_to_element()

    def _adb_multi_tap_to_element(self) -> bool:
        """
        Выполняет три быстрых нажатия с помощью adb.
        """
        return self.__adb_multi_tap()

    @wait_for_window_change()
    def _adb_multi_tap_to_element_and_wait(self,
                                           decorator_args: dict = None) -> bool:
        """
        Выполняет три быстрых нажатия с помощью adb и ожидает изменения окна.
        """
        return self.__adb_multi_tap()

    def __adb_multi_tap(self) -> bool:
        """
        Выполняет три быстрых нажатия с помощью adb.
        Если подавать последовательно, через ";", то выполняются с задержкой в пару секунд.
        Если подавать два тапа, то выполняются одновременно и сливаются.
        С текущей конфигурацией команды - в 90% нажимает два раза. В 10% нажимает 3 раза.
        Для выделения текста подходит.
        """
        try:
            x, y = self._get_center()
            # command = f'adb shell "input tap {x} {y} & input tap {x} {y} & input tap {x} {y}"'
            command = ['adb', 'shell', f'input tap {x} {y} & input tap {x} {y} & input tap {x} {y}']

            adb.run_cmd(command)
            # os.system(f'command')
            return True
        except Exception as e:
            self.logger.error("__adb_multi_tap() ERROR:\n", e)
            return False

    def _adb_swipe(self,
                   root,
                   element: WebElement = None,
                   x: int = None,
                   y: int = None,
                   direction: int = None,
                   distance: int = None,
                   duration: int = 1) -> bool:
        """
        Выполняет прокрутку с помощью adb.

        Аргументы:
            root: Корневой элемент на странице.
            element (WebElement): Целевой элемент.
            x (int): Координата X целевой позиции прокрутки.
            y (int): Координата Y целевой позиции прокрутки.
            direction (int): Направление прокрутки в градусах (от 0 до 360).
            distance (int): Расстояние прокрутки в пикселях.
            duration (int): Длительность прокрутки в секундах.

        Возвращает:
            bool: True, если прокрутка выполнена успешно; False в противном случае.
        """
        # Проверка наличия входных данных
        if element is None and (x is None or y is None) and (direction is None or distance is None):
            return False

        # Получение координат центра начальной позиции прокрутки
        x1, y1 = self._get_center()
        x2, y2 = self._get_center()

        # Расчет целевой позиции прокрутки на основе предоставленных входных данных
        if element is not None:
            # Если предоставлен локатор, получаем координаты центра целевого элемента
            x2, y2 = self._get_center(element)
        elif x is not None and y is not None:
            # Если предоставлены координаты x и y, используем их в качестве целевой позиции прокрутки
            x2, y2 = x, y
        elif direction is not None and distance is not None:
            # Если предоставлены направление и расстояние, вычисляем целевую позицию прокрутки
            window_size = self.driver.get_window_size()
            width = window_size['width']
            height = window_size['height']
            x2, y2 = find_coordinates_by_vector(width=width, height=height,
                                                direction=direction, distance=distance,
                                                start_x=x1, start_y=y1)

        # Выполнение adb-команды прокрутки с заданными координатами и длительностью
        command = ['adb', 'shell', 'input', 'swipe', str(x1), str(y1), str(x2), str(y2), str(duration * 1000)]
        adb.run_cmd(command)

        return True
