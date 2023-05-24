# coding: utf-8
import os

import allure

import config
from core.adb import adb

from applications.SigmaCashRegister.sk_first_run import SigmaAppFirstRun
from applications.SigmaCashRegister.sk_shift import SigmaAppShift
from applications.SigmaCashRegister.sk_cart import SigmaAppCart
from applications.SigmaCashRegister.sk_payment import SigmaAppPayment
from applications.SigmaCashRegister.sk_settings import SigmaAppSettings
from applications.SigmaCashRegister.sk_refund import SigmaAppRefund
from applications.SigmaCashRegister.sk_cash_transactions import SigmaAppCashTransactions
from applications.SigmaCashRegister.sk_correction import SigmaAppCorrection


# TODO к степам добавить step_ (ex. def step_do_something(self):)
# TODO логирование в teardown

class SigmaCashRegister(SigmaAppFirstRun, SigmaAppShift,
                        SigmaAppCart, SigmaAppPayment, SigmaAppSettings,
                        SigmaAppRefund, SigmaAppCashTransactions, SigmaAppCorrection, ):

    @allure.step("Инициализация SigmaCashRegister")
    def __init__(self): # TODO РЕШИТЬ ПРОБЛЕМУ С ОТВАЛИВАНИЕМ ДРАЙЕВА APPIUM ПОСЛЕ 60 СЕКУНД
        super().__init__()
        if not os.path.exists('apk'):
            os.makedirs('apk')
        self.path_to_apk = os.path.abspath(os.path.join('apk', 'sigma-debug.apk'))
        if not os.path.exists(self.path_to_apk):
            os.system(f'curl -o {self.path_to_apk} {config.SIGMA_KASSA_APP_LINK}')
        self._package = adb.get_package_name(self.path_to_apk)
        self._activity_launchable = adb.get_launchable_activity_from_apk(self.path_to_apk)

        self.capabilities_without_install = {
            "platformName": "android",
            "appium:automationName": "uiautomator2",
            "appium:deviceName": adb.get_device_model(),
            "appium:udid": adb.get_device_uuid(),
            "appium:noReset": True,
            "appium: autoGrantPermissions": True,
            "appium: newCommandTimeout": 99999,
        }
        self.capabilities_with_install = {
            "platformName": "android",
            "appium:automationName": "uiautomator2",
            "appium:deviceName": adb.get_device_model(),
            "appium:udid": adb.get_device_uuid(),
            "appium:app": self.path_to_apk,
            "appium:appPackage": self._package,
            "appium:appWaitActivity": self._activity_launchable,
            "appium: autoGrantPermissions": True,
            "appium: newCommandTimeout": 99999,
        }

    def start(self, install: bool = False):
        if install:
            self.connect(capabilities=self.capabilities_with_install)
        else:
            self.connect(capabilities=self.capabilities_without_install)

    def is_running(self):
        return self.driver.is_running()

    # TODO если не нужно то удалить
    # def save_page_source(self, folder_path):
    #     try:
    #         os.makedirs(folder_path, exist_ok=True)
    #         filepath = os.path.join(folder_path, f'page_source.xml')
    #         with open(filepath, 'w', encoding='utf-8') as f:
    #             f.write(self.get_page_source())
    #         return True
    #     except Exception as e:
    #         self.logger.error(f"AdbFullLogger [Error]: {e}")
    #
    # def make_locator(self, type: str, text: str) -> tuple:
    #     locator = ("xpath", f"//android.widget.{type}[contains(@text,'{text}')]")
    #     return locator

