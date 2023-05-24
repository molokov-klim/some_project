# coding: utf-8
import logging
import time
import config
from consts.locators import sigma_kassa_locators as sk_locator


class AppiumActivity(object):
    """
    Класс работы с Appium.
    Обеспечивает работу с активити
    """

    def __init__(self):
        self.logger = logging.getLogger(config.LOGGER_NAME)

    # def get_current_activity(self):
    #     self.logger.debug("get_current_activity(self)")
    #     try:
    #         current_activity = self.driver.current_activity
    #         self.logger.debug(f"get_current_activity, found: {current_activity}")
    #         return current_activity
    #     except:
    #         self.logger.debug(f"get_current_activity, not found")
    #         return None
    #
    # def is_activity(self, activity_name):
    #     """
    #     This method should use the Appium driver to check if the specified activity is currently open.
    #     """
    #     self.logger.debug(f"is_activity(self, activity_name {activity_name})")
    #     try:
    #         current_activity = self.driver.current_activity
    #         if current_activity == activity_name:
    #             self.logger.debug(f"is_activity: True")
    #             return True
    #         else:
    #             self.logger.debug(f"is_activity: False")
    #             return False
    #     except Exception as e:  # TODO перехватывать конкретные исключения
    #         self._handle_exceptions(e)
    #         self.logger.error(f"is_activity, Error: {e}")
    #         return False