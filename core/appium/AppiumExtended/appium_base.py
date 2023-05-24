# coding: utf-8
import logging
import json
import time

from appium import webdriver

import config
from core.appium.AppiumServer.appium_server import AppiumServer


class AppiumBase(object):
    """
    Класс работы с Appium.
    Обеспечивает подключение к устройству
    """

    def __init__(self, keep_alive_server: bool = False):
        self.keep_alive_server = keep_alive_server
        self.capabilities = None
        self.port = 4723
        self.url = 'http://localhost:4723/wd/hub'
        self.driver = None
        self.logger = logging.getLogger(config.LOGGER_NAME)
        self.server = AppiumServer()

    def connect(self, capabilities: dict, ext_appium_server_url=None):
        """
        Подключение к устройству
        """
        self.logger.debug(
            f"connect(capabilities {capabilities}, ext_appium_server_url {ext_appium_server_url}")
        self.capabilities = capabilities
        if not self.server.is_alive():
            self.server.start()
            time.sleep(10)
            self.server.wait_until_alive()
        if not ext_appium_server_url:
            self.driver = webdriver.Remote(self.url, self.capabilities, keep_alive=True)
        else:
            self.driver = webdriver.Remote(ext_appium_server_url, self.capabilities, keep_alive=True)
        app_capabilities = json.dumps(self.capabilities)
        self.logger.info('Подключение установлено: '.format(app_capabilities))
        self.logger.info(f'Сессия №: {self.driver.session_id}')

    def disconnect(self):
        """
        Отключение от устройства
        """
        if self.driver:
            self.logger.debug(f"Отключение от сессии №: {self.driver.session_id}")
            self.driver.quit()
            self.driver = None
        if not self.keep_alive_server:
            self.server.stop()

    def is_running(self):
        return self.driver.is_running()

    def get_session(self):
        self.logger.debug("get_session(self)")
        self.logger.debug(self.driver.get_session())
