# coding: utf-8

from core.appium.AppiumExtended.appium_base import AppiumBase
from core.appium.AppiumExtended.appium_elements import AppiumElements


class AppiumSwipe(AppiumElements):
    """
    Класс работы с Appium.
    Обеспечивает выполнение свайпов
    """

    def __init__(self):
        super().__init__()

    # @log_debug()
    # def swipe(self, start_x: int, start_y: int, end_x: int, end_y: int) -> bool:
    #     """
    #     Метод для выполнения жеста смахивания между предоставленными координатами,
    #     которые указаны в процентах от ширины и высоты экрана.
    #     """
    #     screen_width = self.driver.get_window_size()["width"]
    #     screen_height = self.driver.get_window_size()["height"]
    #
    #     start_x_px = int(screen_width * start_x)
    #     start_y_px = int(screen_height * start_y)
    #     end_x_px = int(screen_width * end_x)
    #     end_y_px = int(screen_height * end_y)
    #
    #     touch_action = TouchAction(self.driver)
    #     touch_action.press(x=start_x_px, y=start_y_px).move_to(x=end_x_px, y=end_y_px).release().perform()
    #
    #     return True

