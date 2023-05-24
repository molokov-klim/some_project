# coding: utf-8
import subprocess
import time

import requests
import logging

import config


class AppiumServer(object):
    def __init__(self, port: int = 4723, log_level: str = 'error'):
        self.logger = logging.getLogger(config.LOGGER_NAME)
        self.port = port
        self.log_level = log_level

    def start(self) -> bool:
        self.logger.info("Start Appium server")
        cmd = f'appium server --log-level {self.log_level} --use-plugins images -p {self.port} -a 127.0.0.1 -pa /wd/hub'
        try:
            subprocess.Popen(cmd, shell=True)
            return True
        except subprocess.CalledProcessError:
            self.logger.error("Error starting Appium server: subprocess.CalledProcessError")
            return False
        except OSError:
            self.logger.error("Error starting Appium server: OSError")
            return False

    def is_alive(self) -> bool:
        self.logger.info("Checking Appium server status")
        try:
            response = requests.get("http://127.0.0.1:4723/wd/hub/sessions")
            if response.status_code == 200:
                self.logger.info("Appium server ready")
                return True
            else:
                self.logger.warning(f"Appium server responded with status code {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error checking Appium server status: {e}")
            return False

    def stop(self) -> bool:
        self.logger.info("Stop Appium server")
        try:
            cmd = 'taskkill /F /IM node.exe'
            subprocess.check_output(cmd, shell=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def wait_until_alive(self, timeout: int = 60, poll: int = 2):
        self.logger.info("Wait for Appium server")
        start_time = time.time()
        while time.time() < start_time + timeout:
            if self.is_alive():
                return True
            time.sleep(poll)
        return False
