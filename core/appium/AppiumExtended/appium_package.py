# coding: utf-8
import logging
import time
import config
from consts.locators import sigma_kassa_locators as sk_locator
from core.appium.AppiumWebElementExtended.web_element_get import WebElementGet


class AppiumPackage(WebElementGet):
    """
    Класс работы с Appium.
    Обеспечивает выполнение свайпов
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = None
        self.driver = args[0]
        self.logger = logging.getLogger(config.LOGGER_NAME)




    def background_app(self, duration: int = 1) -> bool:
        """
        This method should use the Appium driver to place the app in the background for the specified duration (in seconds).
        If the operation is successful, the method will return True. If an error occurs, it will return False.
        """
        self.logger.debug(f"background_app(self, duration {duration}: int = 1)")
        try:
            self.driver.background_app(duration)
            self.logger.debug(f"background_app: True")
            return True
        except Exception as e:
            self.logger.error(f"Error occurred while placing app in the background: {e}")
            return False

    def foreground_app(self, package_name: str, activity_name: str):
        """
        This method should use the Appium driver to bring the app with the specified package name and activity name
        to the foreground.
        """
        self.logger.debug(f"foreground_app(package_name {package_name}, activity_name {activity_name})")
        try:
            self.driver.start_activity(app_package=package_name, app_activity=activity_name)
            self.logger.debug(f"foreground_app(package_name {package_name}, activity_name {activity_name}): True")
            return True
        except Exception as e:
            self.logger.error(f"Foreground app failed: {e}")
            return False

    def foreground_app_by_adb(self, locator: tuple):
        """
        Запускает активити по adb.
        Принимает tuple, в котором первым значением должен быть package, вторым activity name
        Не рэйзит исключение если вернулось другое активити
        """
        self.logger.debug(f"foreground_app_by_adb(locator {locator})")
        time.sleep(8)
        # if not self.wait_for_activity(locator[1]):
        try:
            adb.start_activity(locator[0], locator[1])
            time.sleep(5)
            self.logger.debug(f"foreground_app_by_adb(locator {locator}): True")
            return True
        except Exception as e:
            self._handle_exceptions(e)
            return False
        # return False

    def current_app(self):
        self.logger.debug("current_app()")
        time.sleep(3)
        try:
            current_app = adb.get_current_app_package()
            self.logger.debug(f"current_app(): {current_app}")
            return current_app
        except:
            self.logger.debug(f"current_app(): False")
            return False

    def is_app(self, app: str) -> bool:
        self.logger.debug(f"is_app(app {app})")
        time.sleep(3)
        current_app = self.current_app()
        if app != current_app:
            self.logger.debug(f"is_app({app} != {current_app})")
            return False
        self.logger.debug(f"is_app({app} == {current_app})")
        return True
