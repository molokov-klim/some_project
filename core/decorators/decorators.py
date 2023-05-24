# coding: utf-8
import functools
import logging
import os
import sys
import time
from functools import wraps

import numpy as np
from PIL import Image
import io


import allure
import config
from datetime import datetime
from core.appium.AppiumHelpers.appium_image import AppiumImage
from core.dto import dto

logger = logging.getLogger(config.LOGGER_NAME)

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.2f} seconds")
        return result

    return wrapper

def my_step_info(my_str):
    """
    Декоратор, который перед вызовом метода вызывает logger.info и @allure.step,
    передавая в них строковую переменную, принятую в параметрах.

    Аргументы:
        my_str (str): Строковая переменная для использования в logger.info и @allure.step.

    Возвращает:
        function: Декоратор функций.

    Пример использования:
        @my_step_info("Мой шаг")
        def my_function():
            ...
    """

    # Определяем декоратор функций
    def func_decorator(func):
        # Создаем обертку функции, сохраняющую метаданные исходной функции
        @allure.step(my_str)
        def wrapper(*args, **kwargs):
            # Логируем информацию перед вызовом метода
            logger.info(my_str)
            # Выполняем исходную функцию
            result = func(*args, **kwargs)
            # Логируем информацию после успешного выполнения метода
            logger.info(f"{my_str} [выполнено успешно]")
            # Возвращаем результат выполнения исходной функции
            return result

        # Возвращаем обертку функции
        return wrapper

    # Возвращаем декоратор функций
    return func_decorator


def screenshots():
    """
    В случае возникновения AssertionError в обернутом методе - прикрепляет к allure report скриншот до выполнения
    метода и после возникновения исключения, а также информацию об ошибке.
    В ином случае скриншот не прикрепляется.
    """

    # Определяем декоратор функций
    def func_decorator(func):
        # Создаем обертку функции, сохраняющую метаданные исходной функции
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            # Получаем скриншот до вызова метода
            screenshot = self.driver.get_screenshot_as_png()
            # Генерируем временную метку для имени скриншота
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            # Устанавливаем имя скриншота до вызова метода
            screenshot_name_begin = f"screenshot_begin_{timestamp}.png"
            try:
                # Выполняем исходную функцию
                result = func(self, *args, **kwargs)
            except AssertionError as e:
                # Если произошло исключение, прикрепляем скриншот до вызова метода к отчету
                allure.attach(screenshot, name=screenshot_name_begin, attachment_type=allure.attachment_type.PNG)
                # Прикрепляем информацию об ошибке AssertionError к отчету
                allure.attach(str(e), name="AssertionError", attachment_type=allure.attachment_type.TEXT)
                # Рейзим исключение AssertionError с сохраненным traceback
                raise AssertionError(str(e)).with_traceback(sys.exc_info()[2])
            finally:
                # Получаем скриншот после вызова метода
                screenshot = self.driver.get_screenshot_as_png()
                # Обновляем временную метку для имени скриншота
                timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                # Устанавливаем имя скриншота после вызова метода
                screenshot_name_end = f"screenshot_end_{timestamp}.png"
                # Прикрепляем скриншот после вызова метода к отчету
                allure.attach(screenshot, name=screenshot_name_end, attachment_type=allure.attachment_type.PNG)
            # Возвращаем результат выполнения исходной функции
            return result

        # Возвращаем обертку функции
        return wrapper

    # Возвращаем декоратор функций
    return func_decorator


def log_debug():
    """
    Логирует начало и завершение обернутого метода
    """

    # Определяем декоратор функций
    def func_decorator(func):
        # Создаем обертку функции, сохраняющую метаданные исходной функции
        def wrapper(*args, **kwargs):
            # Получаем имя метода
            method_name = func.__name__
            # Логируем начало выполнения метода и переданные аргументы
            logger.debug(f"{method_name}() < {', '.join(map(str, args))}, "
                         f"{', '.join(f'{k}={v}' for k, v in kwargs.items())}")
            # Выполняем исходную функцию
            result = func(*args, **kwargs)
            # Если результат существует, логируем его
            if result:
                logger.debug(f"{method_name}() > {str(result)}")
            # Возвращаем результат выполнения исходной функции
            return result

        # Возвращаем обертку функции
        return wrapper

    # Возвращаем декоратор функций
    return func_decorator


# def wait_for_window_change(poll_frequency: float = 1.5):
#     """
#     Декоратор ожидает изменения окна после вызова обернутого метода.
#
#     Usage:
#         @wait_for_window_change()
#         def tap_to_element_and_wait_for_window_change(self,
#                                                       locator: Union[tuple, WebElement],
#                                                       timeout_elem: int = 10,
#                                                       decorator_args=None) \
#                 -> bool:
#                 ...
#
#         decorator_args = {"timeout_window": 5,
#                           "tries": 5}
#         app.tap_to_element(locator=locator, decorator_args=decorator_args, wait=True)
#
#     Args:
#         poll_frequency (float): Частота (в секундах), проверки, изменилось ли окно.
#
#     Returns:
#         Результат обернутого метода
#
#     Expected function args:
#         timeout_window: int = 10,
#         tries: int = 3
#     """
#
#     # Определяем декоратор функций
#     def func_decorator(func):
#         # Создаем обертку функции, сохраняющую метаданные исходной функции
#         @functools.wraps(func)
#         def wrapper(self, *args, **kwargs):
#             # Устанавливаем имя изображения
#             image = 'screenshot.png'
#             # Инициализируем переменные
#             result = False
#             func_result = None
#             # Получаем аргументы декоратора
#             decorator_args = kwargs.get('decorator_args', {})
#             # Получаем значения аргументов или устанавливаем значения по умолчанию
#             timeout_window = decorator_args.get('timeout_window', 10)
#             tries = decorator_args.get('tries', 3)
#
#             # if not timeout_window:
#             #     timeout_window = 10
#             # if not tries:
#             #     tries = 3
#
#             # Создаем скриншот
#             with open(image, 'wb') as f:
#                 f.write(self.driver.get_screenshot_as_png())
#
#             # Проверяем изменение окна в течение определенного времени и количества попыток
#             for i in range(tries):
#                 start_time = time.time()
#                 # Если изображение присутствует на экране, вызываем исходную функцию
#                 if AppiumImage(self.driver).is_image_on_the_screen(
#                         part_image=image):  # почему-то всегда заходит на вторую итерацию, поэтому нужно условие
#                     func_result = func(self, *args, **kwargs)
#                 time.sleep(2)
#                 # Проверяем изменение окна в течение заданного времени
#                 while time.time() - start_time < timeout_window:
#                     if not AppiumImage(self.driver).is_image_on_the_screen(part_image=image):
#                         os.remove(image)
#                         logger.debug("Окно изменилось")
#                         return True
#                     time.sleep(poll_frequency)
#             # Удаляем изображение и возвращаем результаты
#             os.remove(image)
#             if not result:
#                 logger.info(f"{func.__name__}() > {func_result}. Изменение окна: False")
#                 return False
#
#         # Возвращаем обертку функции
#         return wrapper
#
#     # Возвращаем декоратор функций
#     return func_decorator


def wait_for_window_change(poll_frequency: float = 0.1):
    def func_decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            # Initialize
            result = False
            func_result = None
            decorator_args = kwargs.get('decorator_args', {})
            timeout_window = decorator_args.get('timeout_window', 10)
            tries = decorator_args.get('tries', 3)

            # Take screenshot and keep it in memory
            #self.driver.set_window_size(800, 600)  # set lower resolution
            image_bytes = self.driver.get_screenshot_as_png()
            image = Image.open(io.BytesIO(image_bytes)).convert('L')  # convert to grayscale
            # Crop screenshot to a certain area
            box = (50, 50, 400, 400)  # left, top, right, bottom
            image = image.crop(box)


            # Try to detect screen change
            for _ in range(tries):
                start_time = time.time()
                func_result = func(self, *args, **kwargs)

                # Detect screen change with exponential backoff
                poll_interval = poll_frequency
                while time.time() - start_time < timeout_window:
                    time.sleep(poll_interval)
                    new_image_bytes = self.driver.get_screenshot_as_png()
                    new_image = Image.open(io.BytesIO(new_image_bytes)).convert('L')  # convert to grayscale
                    new_image = new_image.crop(box)
                    if not np.sum(image) == np.sum(new_image):
                        logger.debug("Screen changed")
                        return True
                    poll_interval *= 2  # double the waiting time for each poll

            if not result:
                logger.info(f"{func.__name__}() > {func_result}. Screen change: False")
                return False

        return wrapper

    return func_decorator





def print_test_info(title: str):
    """
    Печатает на ЧЛ наименование вызываемого метода и переданный в аргументах текст.
    """

    # Определяем функцию декоратор, которая принимает целевую функцию в качестве аргумента
    def decorator(func):
        # Создаем функцию-обертку, которая сохраняет метаданные целевой функции
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Получаем имя целевой функции
            method_name = func.__name__
            # Создаем текст для печати
            text = (
                "===============================",
                "===============================",
                "===============================",
                method_name,  # Включаем имя метода в текст
                title,  # Включаем заголовок, переданный декоратору, в текст
                method_name,  # Включаем имя метода снова в текст
                "===============================",
                "===============================",
                "===============================",
            )
            # Печатаем настраиваемый текст, используя модуль dto
            dto.print_custom_text(text)
            # Вызываем декорированную функцию с ее исходными аргументами
            return func(*args, **kwargs)

        # Возвращаем функцию-обертку в качестве декорированной функции
        return wrapper

    # Возвращаем функцию декоратор
    return decorator





