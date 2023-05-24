import cv2
import numpy as np
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import networkx as nx
import os

from core.adb import adb
from core.appium.AppiumExtended.appium_extended import AppiumExtended
from core.appium.AppiumWebElementExtended.web_element_extended import WebElementExtended
from core.decorators.decorators import time_it

# logging.basicConfig(level=logging.DEBUG)

app = AppiumExtended()
caps = {
    "platformName": "android",
    "appium:automationName": "uiautomator2",
    "appium:deviceName": adb.get_device_model(),
    "appium:udid": adb.get_device_uuid(),
    "appium:noReset": True,
    "appium: autoGrantPermissions": True,
    "appium: newCommandTimeout": 600000,
}
app.connect(caps)

class AppAnalyser:
    def __init__(self, desired_caps):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.graph = nx.DiGraph()
        self.windows_count = 0

    def reset_app(self):
        # Вернуть приложение в исходное состояние
        pass

    def tap_and_check_changes(self, x, y):
        action = TouchAction(self.driver)
        action.tap(x=x, y=y).perform()
        after_screenshot = self.driver.get_screenshot_as_png()
        after_screenshot = cv2.imdecode(np.frombuffer(after_screenshot, np.uint8), cv2.IMREAD_COLOR)
        difference = cv2.absdiff(self.before_screenshot, after_screenshot)
        _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
        change_percentage = np.sum(difference) / difference.size
        if change_percentage > 0.2:
            # Найдена точка перехода на другое окно
            self.graph.add_edge(self.current_window, self.windows_count, action=(x, y))
            self.windows_count += 1
            self.reset_app()
        else:
            # Найдена точка взаимодействия внутри окна
            self.graph.add_edge(self.current_window, self.current_window, action=(x, y))

        self.before_screenshot = after_screenshot

    def create_app_graph(self):
        self.before_screenshot = self.driver.get_screenshot_as_png()
        self.before_screenshot = cv2.imdecode(np.frombuffer(self.before_screenshot, np.uint8), cv2.IMREAD_COLOR)
        for i in range(self.before_screenshot.shape[1]):  # X
            for j in range(self.before_screenshot.shape[0]):  # Y
                self.tap_and_check_changes(i, j)

    def find_shortest_path(self, start, end):
        return nx.shortest_path(self.graph, start, end)

    def run(self):
        self.reset_app()
        self.create_app_graph()


desired_caps = {
    'platformName': 'Android',
    'deviceName': 'YOUR_DEVICE_NAME',
    'appPackage': 'YOUR_APP_PACKAGE',
    'appActivity': 'YOUR_APP_ACTIVITY',
    # Другие необходимые capabilities
}

analyser = AppAnalyser(desired_caps)
analyser.run()

# Найдите кратчайший путь между двумя точками
start = 0
end = 10
path = analyser.find_shortest_path(start, end)
print(path)
