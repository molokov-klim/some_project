import logging
import time

from consts.locators import open_vpn_locators as vpn_locator
from selenium.common import WebDriverException
from core.appium.AppiumPage.appium_page import AppiumPage
import os
from core.adb import adb
import config
import shutil

logger = logging.getLogger(config.LOGGER_NAME)


class OpenVPN(AppiumPage):

    def __init__(self):

        self.path_to_apk = os.path.abspath(os.path.join('', 'apk', 'open_vpn.apk'))
        if not os.path.exists(self.path_to_apk):
            shutil.copyfile(config.OPEN_VPN_APP_PATH, self.path_to_apk)

        super().__init__()
        self._package = adb.get_package_name(self.path_to_apk)
        self._activity_launchable = adb.get_launchable_activity_from_apk(self.path_to_apk)

        self.capabilities_without_install = {
            "platformName": "android",
            "appium:automationName": "uiautomator2",
            "appium:deviceName": adb.get_device_model(),
            "appium:udid": adb.get_device_uuid(),
            "appium:noReset": True,

        }  # "appium:skipServerInstallation": True

        self.logger = logging.getLogger('info')

    def connect_without_install(self):
        try:
            self.connect(self.capabilities_without_install)
            adb.install(config.OPEN_VPN_APP_PATH)
            adb.start_activity("net.openvpn.openvpn", "net.openvpn.unified.MainActivity")
            time.sleep(5)
            return True
        except WebDriverException as e:
            logger.error("Ошибка подключения", e)
            return False

    def push_keys(self) -> bool:
        if not adb.push(config.OPEN_VPN_KEYS_PATH, '/sdcard/Download/vpn'):
            return False
        return True

    def agree_permissions(self) -> bool:
        if not self.tap_to_element(vpn_locator.MODAL_LICENSE_BTN_AGREE):
            return False
        time.sleep(0.5)
        if not self.tap_to_element(vpn_locator.MAIN_FIRST_LAUNCH_BTN_FILE):
            return False
        time.sleep(0.5)
        if not self.tap_to_element(vpn_locator.PERMISSION_BTN_AGREE):
            return False
        return True

    def add_keys(self) -> bool:
        if not self.scroll_to_and_tap(vpn_locator.FILE_SYSTEM_TV_DOWNLOAD_FOLDER):
            return False
        time.sleep(1)
        if not self.scroll_to_and_tap(vpn_locator.FILE_SYSTEM_TV_VPN_FOLDER):
            return False
        time.sleep(1)
        if not self.scroll_to_and_tap(vpn_locator.FILE_SYSTEM_TV_KEYS_FOLDER):
            return False
        time.sleep(1)
        if not self.scroll_to_and_tap(vpn_locator.FILE_SYSTEM_TV_OVPN_FILE):
            return False
        time.sleep(1)
        if not self.scroll_to_and_tap(vpn_locator.FILE_SYSTEM_BTN_IMPORT):
            return False
        time.sleep(1)
        return True

    def turn_on(self) -> bool:
        if not self.tap_to_element(vpn_locator.ADD_FILE_VG_FLAG_CONNECT_AFTER_IMPORT):
            return False
        time.sleep(0.5)
        if not self.tap_to_element(vpn_locator.ADD_FILE_BTN_ADD):
            return False
        if not self.check_request():
            return False
        return True

    def check_request(self) -> bool:
        try:
            time.sleep(2)  # не трогать
            if self.is_window_connection_request():
                if not self.tap_to_element(vpn_locator.MODAL_CONNECTION_REQUEST_BTN_OK):
                    return False
            return True
        except:
            return False

    def is_window_connection_request(self):
        if not self.is_window_displayed(locator=vpn_locator.MODAL_CONNECTION_REQUEST_TV_TITLE,
                                        text=vpn_locator.MODAL_CONNECTION_REQUEST_TV_TITLE_TEXT):
            return False
        return True

    def check_vpn_for_readiness(self):
        if not self.wait_for_window(locator=vpn_locator.MAIN_TV_TITLE,
                                    text=vpn_locator.MAIN_TV_TITLE_TEXT,
                                    timeout=5):
            return False
        if self.tap_to_element(locator=vpn_locator.MAIN_BTN_CONNECT):
            if self.wait_for_element(locator=vpn_locator.MAIN_BTN_DISCONNECT):
                return True
        return False
