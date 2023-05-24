# coding: utf-8
import asyncio
import os
import time
import json
import logging
from datetime import datetime
from typing import Union

from allure_commons.types import AttachmentType
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, TimeoutException, ElementNotInteractableException, \
    ElementNotVisibleException, StaleElementReferenceException, InvalidElementStateException, WebDriverException, \
    InvalidSelectorException

import config
from core.adb import adb

import asyncio
import subprocess


class AppiumPage(object):

    def __init__(self):
        self.capabilities = None
        self.port = 4723
        self.url = 'http://localhost:4723/wd/hub'
        self.driver = None
        self.logger = logging.getLogger(config.LOGGER_NAME)

    # /////////////////////////////////////////////////////////////////////////////////////////////
    # \\\\\\\\\ CONNECTIONS CONNECTIONS CONNECTIONS CONNECTIONS CONNECTIONS CONNECTIONS \\\\\\\\\\
    # /////////////////////////////////////////////////////////////////////////////////////////////

    def connect(self, capabilities: dict, ext_appium_server_url=None):
        """
        Подключение к серверу Appium с указанными desired capabilities для контроля указанного в dc приложения
        """
        self.logger.debug(
            f"connect(capabilities {capabilities}, ext_appium_server_url {ext_appium_server_url}")
        self.capabilities = capabilities
        if not ext_appium_server_url:
            self.driver = webdriver.Remote(self.url, self.capabilities, keep_alive=True)
        else:
            self.driver = webdriver.Remote(ext_appium_server_url, self.capabilities, keep_alive=True)

        app_capabilities = json.dumps(self.capabilities)
        self.logger.info(f'Appium Client is ready with capacities {app_capabilities}')

    def disconnect(self):
        """
        Отключение от сервера Appium
        """
        if self.driver:
            self.logger.debug("disconnect(self)")
            self.driver.get_screenshot_as_png()
            self.driver.quit()
        self.driver = None

    # /////////////////////////////////////////////////////////////////////////////////////////////
    # \\\\\\\\\ WINDOWS  WINDOWS  WINDOWS  WINDOWS  WINDOWS  WINDOWS  WINDOWS  WINDOWS  \\\\\\\\\\
    # /////////////////////////////////////////////////////////////////////////////////////////////

    def is_window_displayed(self, locator: tuple, text: str):
        self.logger.debug(f"is_window_displayed(self, locator {locator}: tuple, text {text}: str)")
        try:
            if not self.is_element_displayed(locator=locator):
                return False
            if not self.find_element(locator=locator).is_enabled():
                return False
            if not self.get_element_attribute(locator=locator, attr='text').startswith(text):
                return False
            return True
        except:
            return False

    def wait_for_window(self, locator: tuple, text: str, timeout: int = 10, timesleep: int = 1) -> bool:
        time.sleep(timesleep)
        self.logger.debug(
            f"wait_for_window(locator: {locator}, text: {text}, timeout: {timeout}")
        if self.wait_for_element(locator=locator, timeout=timeout) and self.is_window(locator=locator, text=text):
            self.logger.debug(
                f"wait_for_window(locator: {locator}, text: {text}, timeout: {timeout}: True")
            return True
        if self.wait_for_element_with_text(locator=locator, text=text, timeout=timeout):
            self.logger.debug(
                f"wait_for_window(locator: {locator}, text: {text}, timeout: {timeout}: True")
            return True
        if self.wait_until_element_will_displayed(locator=locator, timeout=timeout) and self.is_window(locator=locator,
                                                                                                       text=text):
            self.logger.debug(
                f"wait_for_window(locator: {locator}, text: {text}, timeout: {timeout}: True")
            return True
        if self.wait_until_element_will_enabled(locator=locator, timeout=timeout) and self.is_window(locator=locator,
                                                                                                     text=text):
            self.logger.debug(
                f"wait_for_window(locator: {locator}, text: {text}, timeout: {timeout}: True")
            return True
        self.logger.debug(
            f"wait_for_window(locator: {locator}, text: {text}, timeout: {timeout}: False")
        return False

    def is_window(self, locator: tuple, text: str) -> bool:
        self.logger.debug(f"is_window({locator}, text: {text})")
        if not self.is_window_displayed(locator=locator, text=text):
            return False
        if not self.is_element_enabled(locator=locator):
            return False
        self.logger.debug(f"is_window({locator}, text: {text}): True")
        return True

    def wait_until_window_change(self, method, arg, tries: int = 2) -> bool:
        """
        Метод вызывает функцию из аргумента и ждет, пока страница не изменится.
        Принимает только один метод и один аргумент
        """
        self.logger.debug(f"wait_until_window_change()")
        source = self.get_page_source()
        count = 0
        while count < tries:
            method(arg)
            time.sleep(1)
            new_source = self.get_page_source()
            if source != new_source:
                return True
            count += 1
        return False

    # /////////////////////////////////////////////////////////////////////////////////////////////
    # \\\\\\\\\ ACTIVITY  ACTIVITY  ACTIVITY  ACTIVITY  ACTIVITY  ACTIVITY  ACTIVITY  \\\\\\\\\\
    # /////////////////////////////////////////////////////////////////////////////////////////////

    def get_current_activity(self):
        self.logger.debug("get_current_activity(self)")
        try:
            current_activity = self.driver.current_activity
            self.logger.debug(f"get_current_activity, found: {current_activity}")
            return current_activity
        except:
            self.logger.debug(f"get_current_activity, not found")
            return None

    def is_activity(self, activity_name):
        """
        This method should use the Appium driver to check if the specified activity is currently open.
        """
        self.logger.debug(f"is_activity(self, activity_name {activity_name})")
        try:
            current_activity = self.driver.current_activity
            if current_activity == activity_name:
                self.logger.debug(f"is_activity: True")
                return True
            else:
                self.logger.debug(f"is_activity: False")
                return False
        except Exception as e:  # TODO перехватывать конкретные исключения
            self._handle_exceptions(e)
            self.logger.error(f"is_activity, Error: {e}")
            return False

    # def wait_for_activity(self, activity_name: str, timeout: int = 10) -> bool:
    #     """
    #     This method should use the Appium driver to wait until the current activity changes to the specified activity.
    #     """
    #     self.logger.debug(f"wait_for_activity(activity_name {activity_name}, timeout {timeout}")
    #     try:
    #         WebDriverWait(self.driver, timeout).until(
    #             self.is_activity(activity_name)
    #         )
    #         self.logger.debug(f"wait_for_activity: True")
    #         return True
    #     except TimeoutException as e:
    #         self.logger.error(f'TimeoutException with {activity_name}:', '{}'.format(e))
    #         return False
    #     except Exception as e:
    #         self.logger.error(f'Exception with {activity_name}:', '{}'.format(e))
    #         return False

    # /////////////////////////////////////////////////////////////////////////////////////////////
    # \\\\\\\\\ ELEMENT  ELEMENT  ELEMENT  ELEMENT  ELEMENT  ELEMENT  ELEMENT  ELEMENT  \\\\\\\\\\
    # /////////////////////////////////////////////////////////////////////////////////////////////



    def wait_for_element(self, locator: tuple, timeout: int = 10) -> bool:
        """
        This method should use the Appium driver to wait until the current activity changes to the specified activity.
        """
        self.logger.debug(f"wait_for_element(self, locator {locator}, timeout {timeout}: int = 10)")
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            self.logger.debug(f"wait_for_element: True")
            return True
        except TimeoutException:
            self.logger.debug(f"wait_for_element: False")
            return False

    def wait_until_element_will_not_present(self, locator: tuple, timeout: int = 120) -> bool:
        time.sleep(3)
        self.logger.debug(
            f"try wait_until_element_is_not_present(locator {locator}, timeout {timeout})")
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until_not(EC.presence_of_element_located(locator))
            self.logger.debug(f"wait_until_element_will_not_present {locator}: True")
            return True
        except TimeoutException:
            self.logger.debug(f"wait_until_element_will_not_present {locator}: False")
            return False

    def wait_until_element_will_enabled(self, locator: tuple, timeout: int = 10) -> bool:
        self.logger.debug(
            f"wait_until_element_will_enabled(self, locator {locator}: tuple, timeout {timeout}: int = 150)")
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator=locator))
            wait.until(EC.element_to_be_clickable(locator))
            self.logger.debug(f"wait_until_element_will_enabled: True")
            return True
        except StaleElementReferenceException:
            self.logger.debug(f"wait_until_element_will_enabled: False")
            return False
        except TimeoutException:
            self.logger.debug(f"wait_until_element_will_enabled: False")
            return False

    def wait_until_element_will_not_enabled(self, locator: tuple, timeout: int = 10) -> bool:
        self.logger.debug(
            f"wait_until_element_will_not_enabled(self, locator {locator}: tuple, timeout {timeout}: int = 150)")
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator=locator))
            wait.until(EC.staleness_of(element))
            self.logger.debug(f"wait_until_element_will_not_enabled: True")
            return True
        except StaleElementReferenceException:
            self.logger.debug(f"wait_until_element_will_not_enabled: True")
            return True
        except TimeoutException:
            self.logger.debug(f"wait_until_element_will_not_enabled: False")
            return False

    def wait_until_element_will_displayed(self, locator: tuple, timeout: int = 10) -> bool:
        self.logger.debug(
            f"wait_until_element_will_displayed(locator {locator}, timeout {timeout}")
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located(locator=locator))
            wait.until(EC.visibility_of(element))
            self.logger.debug(f"wait_until_element_will_displayed: True")
            return True
        except StaleElementReferenceException:
            self.logger.debug(f"wait_until_element_will_displayed: False")
            return False
        except TimeoutException:
            self.logger.debug(f"wait_until_element_will_displayed: False")
            return False

    def wait_until_element_will_not_displayed(self, locator: tuple, timeout: int = 60) -> bool:
        self.logger.debug(
            f"wait_until_element_not_displayed(locator {locator}, timeout {timeout}")
        time.sleep(3)
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until_not(EC.visibility_of_element_located(locator=locator))
            self.logger.debug(f"wait_until_element_will_not_displayed: True")
            return True
        except TimeoutException:
            self.logger.debug(f"wait_until_element_will_not_displayed: False")
            return False

    def is_element_within_screen(self, element, screen_size):
        """
        Элемент полностью на экране?
        """
        self.logger.debug(f"is_element_within_screen(self, element {element}, screen_size {screen_size})")
        try:
            element_location = element.location
            element_size = element.size
            screen_height = screen_size['height']
            if element_location['y'] + element_size['height'] > screen_height:
                self.logger.debug(f"is_element_within_screen {element}: False")
                return False
            self.logger.debug(f"is_element_within_screen {element}: True")
            return True
        except WebDriverException:
            return False

    def click_to_element(self, locator: tuple, timeout=10) -> bool:
        self.logger.debug(f"click_to_element() {locator=}, {timeout=}")
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located(locator))
            action = ActionChains(self.driver)
            action.click(element)
            self.logger.debug(f"click_to_element() True")
            return True
        except WebDriverException:
            return False

        # self.logger.debug(
        #     f"click_to_element(self, locator_tuple {locator}: tuple, timeout {timeout}=10, check_visibility {check_visibility}=True)")
        # try:
        #     wait = WebDriverWait(self.driver, timeout)
        #     clickable_element = wait.until(EC.element_to_be_clickable(locator))
        # except Exception as e:
        #     self.logger.error(f"click_to_element. Element not found: {locator}", '{}'.format(e))
        #     return False
        #
        # if check_visibility and not clickable_element.is_displayed():
        #     self.logger.error(f"click_to_element. Element not visible: {locator}")
        #     return False
        #
        # try:
        #     clickable_element.click()
        # except ElementNotInteractableException as e:
        #     self.logger.error(f"click_to_element. Element not interactable: {locator}", '{}'.format(e))
        #     return False
        # time.sleep(1)
        # self.logger.debug(
        #     f"click_to_element {locator}: True")
        # return True

    def tap_to_element(self, locator: tuple, timeout=10, tries: int = 5):
        self.logger.debug(f"_tap: {locator}, timeout: {timeout}")
        # if not self.wait_until_element_will_enabled(locator=locator, timeout=timeout):
        #     self.logger.debug(f"_tap: {locator} False")
        #     return False
        wait = WebDriverWait(driver=self.driver, timeout=timeout)
        for i in range(tries):
            try:
                element = wait.until(EC.presence_of_element_located(locator))
                self.logger.debug(f"try _tap to {element}")
                TouchAction(self.driver).tap(element).perform()
                self.logger.debug(f"_tap: {locator} True")
                break  # exit the loop if the _tap is successful
            except (ElementNotInteractableException, StaleElementReferenceException, InvalidElementStateException):
                if i == tries - 1:
                    return False
                time.sleep(1)
            except Exception as e:
                self.logger.error(f"ERROR _tap: непредвиденная ошибка {e}")
        return True

    def directly_tap_to_element(self, element, timeout=10, tries: int = 5):
        self.logger.debug(f"directly_tap_to_element: {timeout=}")
        if element is None:
            self.logger.error(f"element is None")
            return False
        wait = WebDriverWait(driver=self.driver, timeout=timeout)
        for i in range(tries):
            try:
                self.logger.debug(f"try _tap to {element=}")
                TouchAction(self.driver).tap(element).perform()
                self.logger.debug(f"_tap: {element=} True")
                break  # exit the loop if the _tap is successful
            except (ElementNotInteractableException, StaleElementReferenceException, InvalidElementStateException,
                    Exception):
                if i == tries - 1:
                    return False
                time.sleep(1)
            except Exception as e:
                self.logger.error("ERROR _tap: непредвиденная ошибка %s", e)
        return True


    def tap_to_element_contain_text(self, type: str, text: str, timeout=10):
        self.logger.debug(f"tap_to_element_contain_text(type {type}, text {text}, timeout {timeout})")
        locator = ("xpath", f"//android.widget.{type}[contains(@text,'{text}')]")
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            if not self.wait_until_element_will_enabled(locator):
                self.logger.debug(f"_tap: {locator} False")
                return False
            TouchAction(self.driver).tap(element).perform()
            self.logger.debug(f"_tap: {locator} True")
            return True
        except Exception as e:
            self.logger.error(f"Element not found: {locator}", '{}'.format(e))
            return False

    def scroll_down_by_adb(self, max_scrolls: int = 1) -> bool:
        self.logger.debug(f"scroll_down_by_adb")
        try:
            screen_size = self.driver.get_window_size()
            height = screen_size['height']
            width = screen_size['width']
            start_x = int(width * 0.5)
            end_x = int(width * 0.5)
            start_y = int(height * 0.7)
            end_y = int(height * 0.4)

            scroll_count = 0

            while scroll_count < max_scrolls:
                adb.swipe(start_x=start_x, end_x=end_x, start_y=start_y, end_y=end_y)
                scroll_count += 1
            return True
        except Exception as e:
            self.logger.error("Error with scroll_down_by_adb: {}".format(e))
            return False

    def scroll_up_by_adb(self, max_scrolls: int = 1) -> bool:
        self.logger.debug(f"scroll_up_by_adb")
        try:
            screen_size = self.driver.get_window_size()
            height = screen_size['height']
            width = screen_size['width']
            start_x = int(width * 0.5)
            end_x = int(width * 0.5)
            start_y = int(height * 0.4)
            end_y = int(height * 0.7)
            scroll_count = 0

            while scroll_count < max_scrolls:
                adb.swipe(start_x=start_x, end_x=end_x, start_y=start_y, end_y=end_y)
                scroll_count += 1
            return True
        except Exception as e:
            self.logger.error("Error with scroll_up_by_adb: {}".format(e))
            return False

    def scroll_down_to_element_by_adb(self, locator: tuple, max_scrolls: int = 5) -> bool:
        """
        Метод через adb скроллит вниз, пока элемент не будет найден или не будет исчерпано max_scrolls.
        """
        self.logger.debug(
            f"scroll_down_to_element_by_adb(self, locator {locator}: tuple, max_scrolls {max_scrolls}: int = 5)")
        wait = WebDriverWait(self.driver, 5)
        screen_size = self.driver.get_window_size()
        height = screen_size['height']
        width = screen_size['width']
        scroll_count = 0

        while scroll_count < max_scrolls:
            try:
                element = wait.until(EC.visibility_of_element_located(locator))
                if self.is_element_within_screen(element, screen_size):
                    self.logger.debug(
                        f"scroll_down_to_element_by_adb: True")
                    return True
            except TimeoutException:
                pass

            start_x = int(width * 0.5)
            end_x = int(width * 0.5)

            start_y = int(height * 0.8)
            end_y = int(height * 0.5)

            adb.swipe(start_x=start_x, end_x=end_x, start_y=start_y, end_y=end_y)
            scroll_count += 1
        self.logger.debug(
            f"scroll_down_to_element_by_adb: False")
        return False

    def scroll_up_to_element_by_adb(self, locator: tuple, max_scrolls: int = 1) -> bool:
        """
        This method should use the adb to scroll up until the element is displayed.
        """
        self.logger.debug(
            f"scroll_up_to_element_by_adb(self, locator {locator}: tuple, max_scrolls {max_scrolls}: int = 5)")
        wait = WebDriverWait(self.driver, 5)
        screen_size = self.driver.get_window_size()
        height = screen_size['height']
        width = screen_size['width']
        scroll_count = 0

        while scroll_count < max_scrolls:
            try:
                element = wait.until(EC.visibility_of_element_located(locator))
                if self.is_element_within_screen(element, screen_size):
                    self.logger.debug(
                        f"scroll_up_to_element_by_adb: True")
                    return True
            except TimeoutException:
                pass

            start_x = int(width * 0.5)
            end_x = int(width * 0.5)

            start_y = int(height * 0.5)
            end_y = int(height * 0.8)

            adb.swipe(start_x=start_x, end_x=end_x, start_y=start_y, end_y=end_y)
            scroll_count += 1
        self.logger.debug(
            f"scroll_up_to_element_by_adb: False")
        return False

    # def scroll_down_to_element_by_appium(self, locator: tuple, max_scrolls: int = 5) -> bool:
    #     """
    #     This method should use the Appium driver to scroll down until the element is displayed.
    #     """
    #     self.logger.debug(
    #         f"scroll_down_to_element_by_appium(self, locator {locator}: tuple, max_scrolls {max_scrolls}: int = 5)")
    #     wait = WebDriverWait(self.driver, 5)
    #     screen_size = self.driver.get_window_size()
    #     height = screen_size['height']
    #     width = screen_size['width']
    #     scroll_count = 0
    #
    #     while scroll_count < max_scrolls:
    #         try:
    #             element = wait.until(EC.visibility_of_element_located(locator))
    #             if self.is_element_within_screen(element, screen_size):
    #                 self.logger.debug(
    #                     f"scroll_down_to_element_by_appium: True")
    #                 return True
    #         except TimeoutException:
    #             pass
    #
    #         start_y = int(height * 0.8)
    #         end_y = int(height * 0.2)
    #         action = TouchAction(self.driver)
    #         action.press(x=500, y=start_y).move_to(x=500, y=end_y).release().perform()
    #         scroll_count += 1
    #     self.logger.debug(
    #         f"scroll_down_to_element_by_appium: False")
    #     return False
    #
    # def scroll_up_to_element_by_appium(self, locator: tuple, max_scrolls: int = 5) -> bool:
    #     """
    #     This method should use the Appium driver to scroll up until the element is displayed.
    #     """
    #     self.logger.debug(
    #         f"scroll_up_to_element_by_appium(self, locator {locator}: tuple, max_scrolls {max_scrolls}: int = 5)")
    #     wait = WebDriverWait(self.driver, 5)
    #     screen_size = self.driver.get_window_size()
    #     height = screen_size['height']
    #     width = screen_size['width']
    #     scroll_count = 0
    #
    #     while scroll_count < max_scrolls:
    #         try:
    #             element = wait.until(EC.visibility_of_element_located(locator))
    #             if self.is_element_within_screen(element, screen_size):
    #                 self.logger.debug(
    #                     f"scroll_up_to_element_by_appium {element}: True")
    #                 return True
    #         except TimeoutException:
    #             pass
    #
    #         start_y = int(height * 0.2)
    #         end_y = int(height * 0.8)
    #         action = TouchAction(self.driver)
    #         action.press(x=500, y=start_y).move_to(x=500, y=end_y).release().perform()
    #         scroll_count += 1
    #     self.logger.debug(
    #         f"scroll_up_to_element_by_appium: False")
    #     return False

    def is_element_displayed(self, locator) -> bool:
        """
        This method should use the Appium driver to locate an element by the provided locator,
        and return a boolean value indicating whether the element is displayed on the screen or not.
        """
        self.logger.debug(f"is_element_displayed(locator {locator})")
        try:
            element = self.find_element(locator)
            if not element.is_displayed():
                self.logger.debug(f"is_element_displayed(locator {locator}): False")
                return False
            self.logger.debug(f"is_element_displayed(locator {locator}): True")
            return True
        except:
            self.logger.debug(f"is_element_displayed(locator {locator}): False")
            return False

    def is_element_enabled(self, locator) -> bool:
        self.logger.debug(f"is_element_enabled(locator {locator})")
        try:
            element = self.find_element(locator)
            if not element.is_enabled():
                self.logger.debug(f"is_element_enabled(locator {locator}): False")
                return False
            self.logger.debug(f"is_element_enabled(locator {locator}): True")
            return True
        except:
            self.logger.debug(f"is_element_enabled(locator {locator}): False")
            return False

    def is_element_active(self, locator) -> bool:
        self.logger.debug(f"is_element_active(locator {locator})")
        try:
            element = self.find_element(locator)
            if not element.is_displayed():
                self.logger.debug(f"is_element_active(locator {locator}): False")
                return False
            if not element.is_enabled():
                self.logger.debug(f"is_element_active(locator {locator}): False")
                return False
            self.logger.debug(f"is_element_active(locator {locator}): True")
            return True
        except Exception as e:
            self.logger.debug(f"is_element_active(locator {locator}): False", "{}".format(e))
            return False

    def get_element_attribute(self, locator: tuple, attr: str) -> Union[str, None]:
        self.logger.debug(f"get_element_attribute(locator {locator}, attr {attr})")
        try:
            element = self.find_element(locator)
            attribute_value = element.get_attribute(attr)
            self.logger.debug(f"get_element_attribute: {attribute_value}")
            return attribute_value
        except Exception as e:
            self.logger.debug("get_element_attribute: False {}".format(e))
            return None

    def is_element_attribute_value(self, locator: tuple, attr: str, value: str) -> bool:
        self.logger.debug(f"is_element_attribute_value() {locator=}, {attr=}")
        try:
            element_atrr = self.get_element_attribute(locator=locator, attr=attr)
            assert element_atrr is not None
            assert value == element_atrr
        except AssertionError:
            return False

    def find_element(self, locator: tuple):
        self.logger.debug(f"find_element(locator {locator})")
        try:
            element = self.driver.find_element(locator[0], locator[1])
            self.logger.debug(f"find_element(locator {locator}): True")
            return element
        except:
            self.logger.debug(f"find_element(locator {locator}): False")
            return None

    def wait_for_element_with_text(self, locator: tuple, text: str, timeout: int = 10):
        self.logger.debug(
            f"wait_for_element_with_text(locator {locator}, text {text}, timeout {timeout}")
        if not self.wait_for_element(locator=locator, timeout=timeout):
            self.logger.debug(
                f"wait_for_element_with_text(locator {locator}, text {text}, timeout {timeout}: False")
            return False
        if not self.get_element_attribute(locator=locator, attr='text').startswith(text):
            self.logger.debug(
                f"wait_for_element_with_text(locator {locator}, text {text}, timeout {timeout}: False")
            return False
        if self.wait_until_element_will_enabled(locator=locator, timeout=timeout):
            self.logger.debug(
                f"wait_for_element_with_text(locator {locator}, text {text}, timeout {timeout}: False")
            return False
        self.logger.debug(
            f"wait_for_element_with_text(locator {locator}, text {text}, timeout {timeout}: True")
        return True



    # /////////////////////////////////////////////////////////////////////////////////////////////
    # \\\\\\\\\ ELEMENTS  ELEMENTS  ELEMENTS  ELEMENTS  ELEMENTS  ELEMENTS  ELEMENTS \\\\\\\\\\
    # /////////////////////////////////////////////////////////////////////////////////////////////

    def extract_attr_from_elements(self, locator: tuple, attr: str) -> list:
        elements = self.driver.find_elements(*locator)
        attr_values = [element.get_attribute(attr) for element in elements]
        return attr_values

    def get_elements(self, type_of: str):
        self.logger.debug("get_elements()")
        self.wait_until_element_will_displayed(locator=("xpath", "//android.view.ViewGroup[@index='0']"))
        try:
            elements = self.driver.find_elements('xpath', f'//{type_of}')
            self.logger.debug(elements)
            self.logger.debug("Элементы найдены")
            return elements
        except NoSuchElementException:
            self.logger.error("Элемент не найден")
            return None

    def _get_element(self, locator: tuple):
        self.logger.debug(f"_get_element(locator {locator})")
        self.wait_until_element_will_displayed(locator=locator)
        try:
            if not self.wait_for_element(locator=locator):
                return False
            #element = self.driver.find_element(locator[0], locator[1])
            #element = self.driver.find_element(*locator)
            wait = WebDriverWait(self.driver, timeout=10)
            element = wait.until(EC.presence_of_element_located(locator))
            return element
        except NoSuchElementException as e:
            self.logger.error("Элемент не найден {}".format(e))

    def get_element_from_element(self, locator_parent: tuple, locator_child: tuple):
        """
        Метод извлекает элемент из элемента и возвращает его
        """
        element = None
        self.logger.debug("get_element_from_element()")
        self.wait_until_element_will_displayed(locator=locator_parent)
        try:
            parent_element = self.driver.find_element(*locator_parent)
            child_element = parent_element.find_element(*locator_child)
            self.logger.debug("Элемент найден")
            return child_element
        except NoSuchElementException:
            self.logger.error("Элемент не найден")
            return None

    def directly_get_element_from_element(self, parent_element, locator_child: tuple):
        """
        Метод извлекает элемент из элемента и возвращает его
        """
        self.logger.debug("get_element_from_element()")
        try:
            child_element = parent_element.find_element(*locator_child)
            self.logger.debug("Элемент внутри элемента найден")
            return child_element
        except NoSuchElementException:
            self.logger.error("Элемент внутри элемента не найден")
            self.logger.error(f"{locator_child=}")
            self.logger.error(f"{dir(parent_element)=}")
            return None

    # /////////////////////////////////////////////////////////////////////////////////////////////
    # \\\\\\\\\ ACTIONS  ACTIONS  ACTIONS  ACTIONS  ACTIONS  ACTIONS  ACTIONS  ACTIONS  \\\\\\\\\\
    # /////////////////////////////////////////////////////////////////////////////////////////////

    def swipe(self, start_x: int, start_y: int, end_x: int, end_y: int) -> bool:
        """
        This method should use the Appium driver to perform a swipe gesture between the provided coordinates,
        which are specified as a percentage of the screen width and height.
        """
        self.logger.debug(
            f"swipe(self, start_x {start_x}: int, start_y {start_y}: int, end_x {end_x}: int, end_y {end_y}: int)")
        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        start_x_px = int(screen_width * start_x)
        start_y_px = int(screen_height * start_y)
        end_x_px = int(screen_width * end_x)
        end_y_px = int(screen_height * end_y)

        try:
            self.driver.swipe(start_x_px, start_y_px, end_x_px, end_y_px, 1000)
            self.logger.debug(f"swipe: True")
            return True
        except Exception as e:
            self._handle_exceptions(e)
            self.logger.debug("swipe: False. Error: {}".format(e))
            return False

    def get_window_size(self):
        """
        This method should use the Appium driver to retrieve the size of the current window.
        """
        self.logger.debug(f"get_window_size()")
        try:
            window_size = self.driver.get_window_size()
            if window_size is not None:
                self.logger.debug(f"get_window_size(): {window_size}")
                return window_size
            else:
                self.logger.debug(f"get_window_size(): False")
                return False
        except Exception as e:
            self.logger.error("Failed to get window size: {}".format(e))
            return False

    def get_screenshot(self):
        self.logger.debug("get_screenshot()")
        try:
            screen = self.driver.get_screenshot_as_png()
            self.logger.debug(f"get_screenshot(): True")
            return screen
        except Exception as e:
            self.logger.error("get_screenshot(): Error: {}".format(e))
            return None

    def curl_session(self):
        self.logger.debug("curl_session(self)")
        self.logger.debug(os.system("curl http://localhost:4723/wd/hub/sessions"))

    def get_session(self):
        self.logger.debug("get_session(self)")
        self.logger.debug(self.driver.get_session())

    def get_page_source(self):
        source = self.driver.page_source
        return source

    def save_page_source(self, folder_path):
        try:
            os.makedirs(folder_path, exist_ok=True)
            filepath = os.path.join(folder_path, f'page_source.xml')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(self.get_page_source())
            return True
        except Exception as e:
            self.logger.error(f"AdbFullLogger [Error]: {e}")

    def make_locator(self, type: str, text: str) -> tuple:
        locator = ("xpath", f"//android.widget.{type}[contains(@text,'{text}')]")
        return locator

    # /////////////////////////////////////////////////////////////////////////////////////////////
    # \\\\\\\\\ APPLICATION  APPLICATION  APPLICATION  APPLICATION  APPLICATION   \\\\\\\\\\
    # /////////////////////////////////////////////////////////////////////////////////////////////

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
            adb.start_activity(*locator)
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

    # /////////////////////////////////////////////////////////////////////////////////////////////
    # \\\\\\\\\ HANDLERS  HANDLERS  HANDLERS  HANDLERS  HANDLERS  HANDLERS  HANDLERS   \\\\\\\\\\
    # /////////////////////////////////////////////////////////////////////////////////////////////

    def _handle_exceptions(self, e):
        self.logger.debug(f"_handle_exceptions(self, e {e})")
        if isinstance(e, NoSuchElementException):
            self.logger.error('No Such Element Exception occurred: {}'.format(e))
        elif isinstance(e, TimeoutException):
            self.logger.error('Timeout Exception occurred: {}'.format(e))
        elif isinstance(e, ElementNotInteractableException):
            self.logger.error('Element Not Interactable Exception occurred: {}'.format(e))
        elif isinstance(e, ElementNotVisibleException):
            self.logger.error('Element Not Visible Exception occurred: {}'.format(e))
        elif isinstance(e, StaleElementReferenceException):
            self.logger.error('Stale Element Reference Exception occurred: {}'.format(e))
        elif isinstance(e, InvalidElementStateException):
            self.logger.error('Invalid Element State Exception occurred: {}'.format(e))
        elif isinstance(e, WebDriverException):
            self.logger.error('WebDriver Exception occurred: {}'.format(e))
        elif isinstance(e, Exception):
            self.logger.error('Unexpected error: {}'.format(e))
        return

    # /////////////////////////////////////////////////////////////////////////////////////////////
    # \\\\\\\\\ SCROLLERS   \\\\\\\\\\
    # /////////////////////////////////////////////////////////////////////////////////////////////

    # def scroll_to_and_tap(self, locator, max_retries=3):
    #     self.logger.debug(f"def scroll_to_and_tap(locator {locator}, max_retries {max_retries})")
    #     time.sleep(1)
    #     for i in range(max_retries):
    #         try:
    #             if not self.is_element_displayed(locator=locator):
    #                 self.scroll_down_to_element_by_adb(locator=locator, max_scrolls=3)
    #                 if not self.is_element_displayed(locator):
    #                     self.scroll_up_to_element_by_adb(locator=locator, max_scrolls=5)
    #                     if not self.is_element_displayed(locator=locator):
    #                         continue
    #             self._tap(locator=locator)
    #             time.sleep(0.1)
    #             self.logger.debug(f"def scroll_to_and_tap(locator {locator}, max_retries {max_retries}): True")
    #             return True
    #         except Exception as e:
    #             self.logger.error(f"Exception occurred while trying to _tap element: {e}")
    #             self.logger.error(f"Exception occurred while trying to _tap element: {locator}")
    #     self.logger.debug(f"def scroll_to_and_tap(locator {locator}, max_retries {max_retries}): False")
    #     return False

    def scroll_to_and_tap(self, locator, timeout: int = 30):
        self.logger.debug(f"def scroll_to_and_tap() locator {locator}")
        time.sleep(1)
        if self.scroll_to(locator=locator):
            self.tap_to_element(locator=locator)
            return True
        return False
        # if self.scroll_down_to(locator=locator, timeout=timeout):
        #     assert self._tap(locator=locator)
        #     self.logger.debug(f"def scroll_to_and_tap(): True")
        #     return True
        # else:
        #     if self.scroll_up_to(locator=locator, timeout=timeout):
        #         assert self._tap(locator=locator)
        #         self.logger.debug(f"def scroll_to_and_tap(): True")
        #         return True
        # self.logger.debug(f"def scroll_to_and_tap(): False")
        # return False

    def scroll_to(self, locator, max_retries=2):
        self.logger.debug(f"scroll_to(locator {locator}, max_retries {max_retries})")
        time.sleep(1)
        for i in range(max_retries):
            try:
                if not self.is_element_displayed(locator=locator):
                    self.scroll_down_to(locator=locator)
                    if not self.is_element_displayed(locator):
                        self.scroll_up_to(locator=locator)
                        if not self.is_element_displayed(locator=locator):
                            continue
                time.sleep(0.1)
                self.logger.debug(f"scroll_to(locator {locator}, max_retries {max_retries}): True")
                return True
            except Exception as e:
                self.logger.error(f"Exception occurred while trying to _tap element: {e}")
                self.logger.error(f"Exception occurred while trying to _tap element: {locator}")
        self.logger.debug(f"scroll_to(locator {locator}, max_retries {max_retries}): False")
        return False

    def scroll_down_to(self, locator: tuple, timeout: int = 600):
        self.logger.debug(f"scroll_down_to() locator {locator})")
        time.sleep(2)
        source = self.get_page_source()
        new_source = None
        start_time = time.time()
        while source != new_source and not time.time() - start_time > timeout:
            time.sleep(1)
            if self.is_element_displayed(locator=locator):
                if self.is_element_within_screen(self.find_element(locator=locator),
                                                 screen_size=self.driver.get_window_size()):
                    self.logger.info("Элемент найден")
                    return True
            self.scroll_down_by_adb(max_scrolls=1)
            time.sleep(1)
            new_source = self.get_page_source()
        self.logger.debug(f"scroll_down_to() False)")
        return False

    def scroll_up_to(self, locator: tuple, timeout: int = 600):
        self.logger.debug(f"scroll_up_to() locator {locator})")
        source = self.get_page_source()
        new_source = None
        start_time = time.time()
        while source != new_source and not time.time() - start_time > timeout:
            if self.scroll_up_to_element_by_adb(locator=locator, max_scrolls=1):
                self.logger.debug(f"scroll_up_to() True)")
                return True
            time.sleep(1)
            new_source = self.get_page_source()
        self.logger.debug(f"scroll_up_to() False)")
        return False

    def scroll_to_element_with_text_and_tap(self, type_of: str, text: str, max_retries=3):  # TODO change me
        self.logger.debug(
            f"scroll_to_element_with_text_and_tap(type {type_of}, text {text}, max_retries {max_retries})")
        locator = ("xpath", f"//android.widget.{type_of}[contains(@text,'{text}')]")
        self.logger.debug(f"locator_: {locator}")
        for i in range(max_retries):
            try:
                if not self.is_element_displayed(locator=locator):
                    self.scroll_down_to_element_by_adb(locator=locator, max_scrolls=3)
                    if not self.is_element_displayed(locator):
                        self.scroll_up_to_element_by_adb(locator=locator, max_scrolls=5)
                        if not self.is_element_displayed(locator=locator):
                            if not self.is_element_displayed(locator=locator):
                                self.scroll_down_to_element_by_adb(locator=locator, max_scrolls=30)
                                if not self.is_element_displayed(locator):
                                    self.scroll_up_to_element_by_adb(locator=locator, max_scrolls=50)
                                    if not self.is_element_displayed(locator=locator):
                                        continue
                time.sleep(1)
                self.tap_to_element(locator=locator)
                time.sleep(0.1)
                self.logger.debug(f"scroll_to_element_with_text_and_tap(text {text}, max_retries {max_retries}): True")
                return True
            except InvalidElementStateException as e:
                self.logger.error(f"InvalidElementStateException occurred while trying to _tap element {locator}: {e}")
            except Exception as e:
                self.logger.error(f"Exception occurred while trying to _tap element {locator}: {e}")
        self.logger.debug(f"scroll_to_element_with_text_and_tap(text {text}, max_retries {max_retries}): False")
        return False

    def scroll_to_and_get_element(self, locator, max_retries=3) -> webdriver.webelement:
        self.logger.debug(f"scroll_to_and_get_element(locator {locator}, max_retries {max_retries})")
        time.sleep(1)
        for i in range(max_retries):
            try:
                element = self.find_element(locator=locator)
                if element.is_displayed():
                    self.logger.debug(f"scroll_to_and_get_element(locator {locator}, max_retries {max_retries}): True")
                    return element
                else:
                    self.scroll_down_to_element_by_adb(locator=locator, max_scrolls=3)
                    if element.is_displayed():
                        self.logger.debug(
                            f"scroll_to_and_get_element(locator {locator}, max_retries {max_retries}): True")
                        return element
                    else:
                        self.scroll_up_to_element_by_adb(locator=locator, max_scrolls=3)
                        if element.is_displayed():
                            self.logger.debug(
                                f"scroll_to_and_get_element(locator {locator}, max_retries {max_retries}): True")
                            return element
            except Exception as e:
                self.logger.error(f"Exception occurred while trying to find element: {e}")
        self.logger.debug(f"scroll_to_and_get_element(locator {locator}, max_retries {max_retries}): None")
        return None

    def scroll_to_element_with_text_and_get_element(self, text: str):
        locator = ("xpath", f".//*[contains(@text, '{text}')]")
        if self.scroll_down_to(locator):
            return self.get_element(locator)
        if self.scroll_up_to(locator):
            return self.get_element(locator)


        # self.logger.debug(f"scroll_to_element_with_text_and_get_element(text {text}, max_retries {max_retries})")
        # locator = ("xpath", f".//*[contains(@text, '{text}')]")
        # for i in range(max_retries):
        #     try:
        #         element = self.find_element(locator=locator)
        #         if element:
        #             self.logger.debug(
        #                 f"scroll_to_element_with_text_and_get_element(text {text}, max_retries {max_retries}): True")
        #             return element
        #         else:
        #             self.scroll_down_to_element_by_adb(locator=locator, max_scrolls=3)
        #             if element.is_displayed():
        #                 self.logger.debug(
        #                     f"scroll_to_element_with_text_and_get_element(text {text}, max_retries {max_retries}): True")
        #                 return element
        #             else:
        #                 self.scroll_up_to_element_by_adb(locator=locator, max_scrolls=3)
        #                 if element.is_displayed():
        #                     self.logger.debug(
        #                         f"scroll_to_element_with_text_and_get_element(text {text}, max_retries {max_retries}): True")
        #                     return element
        #     except Exception as e:
        #         self.logger.error(f"Exception occurred while trying to find element: {e}")
        # self.logger.debug(f"scroll_to_element_with_text_and_get_element(text {text}, max_retries {max_retries}): None")
        # return None

    # async def polling(self):
    #     """
    #     тык в аппиум чтоб не спал
    #     """
    #     while True:
    #         print("POLL")
    #         print("caps: %s", await self.driver.capabilities)
    #         await asyncio.sleep(25)
