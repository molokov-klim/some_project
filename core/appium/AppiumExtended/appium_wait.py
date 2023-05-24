# coding: utf-8
import logging
import time
import config
from consts.locators import sigma_kassa_locators as sk_locator


class AppiumWait(object):
    """
    Класс работы с Appium.
    Обеспечивает выполнение ожидания
    """

    def __init__(self):
        self.logger = logging.getLogger(config.LOGGER_NAME)

    # def wait_for_element(self, locator: tuple, timeout: int = 10) -> bool:
    #     """
    #     This method should use the Appium driver to wait until the current activity changes to the specified activity.
    #     """
    #     self.logger.debug(f"wait_for_element(self, locator {locator}, timeout {timeout}: int = 10)")
    #     try:
    #         wait = WebDriverWait(self.driver, timeout)
    #         wait.until(EC.presence_of_element_located(locator))
    #         self.logger.debug(f"wait_for_element: True")
    #         return True
    #     except TimeoutException:
    #         self.logger.debug(f"wait_for_element: False")
    #         return False
    #
    #
    # def wait_until_element_will_not_present(self, locator: tuple, timeout: int = 120) -> bool:
    #     time.sleep(3)
    #     self.logger.debug(
    #         f"try wait_until_element_is_not_present(locator {locator}, timeout {timeout})")
    #     try:
    #         wait = WebDriverWait(self.driver, timeout)
    #         wait.until_not(EC.presence_of_element_located(locator))
    #         self.logger.debug(f"wait_until_element_will_not_present {locator}: True")
    #         return True
    #     except TimeoutException:
    #         self.logger.debug(f"wait_until_element_will_not_present {locator}: False")
    #         return False
    #
    # def wait_until_element_will_enabled(self, locator: tuple, timeout: int = 10) -> bool:
    #     self.logger.debug(
    #         f"wait_until_element_will_enabled(self, locator {locator}: tuple, timeout {timeout}: int = 150)")
    #     try:
    #         wait = WebDriverWait(self.driver, timeout)
    #         wait.until(EC.presence_of_element_located(locator=locator))
    #         wait.until(EC.element_to_be_clickable(locator))
    #         self.logger.debug(f"wait_until_element_will_enabled: True")
    #         return True
    #     except StaleElementReferenceException:
    #         self.logger.debug(f"wait_until_element_will_enabled: False")
    #         return False
    #     except TimeoutException:
    #         self.logger.debug(f"wait_until_element_will_enabled: False")
    #         return False
    #
    # def wait_until_element_will_not_enabled(self, locator: tuple, timeout: int = 10) -> bool:
    #     self.logger.debug(
    #         f"wait_until_element_will_not_enabled(self, locator {locator}: tuple, timeout {timeout}: int = 150)")
    #     try:
    #         wait = WebDriverWait(self.driver, timeout)
    #         element = wait.until(EC.presence_of_element_located(locator=locator))
    #         wait.until(EC.staleness_of(element))
    #         self.logger.debug(f"wait_until_element_will_not_enabled: True")
    #         return True
    #     except StaleElementReferenceException:
    #         self.logger.debug(f"wait_until_element_will_not_enabled: True")
    #         return True
    #     except TimeoutException:
    #         self.logger.debug(f"wait_until_element_will_not_enabled: False")
    #         return False
    #
    # def wait_until_element_will_displayed(self, locator: tuple, timeout: int = 10) -> bool:
    #     self.logger.debug(
    #         f"wait_until_element_will_displayed(locator {locator}, timeout {timeout}")
    #     try:
    #         wait = WebDriverWait(self.driver, timeout)
    #         element = wait.until(EC.visibility_of_element_located(locator=locator))
    #         wait.until(EC.visibility_of(element))
    #         self.logger.debug(f"wait_until_element_will_displayed: True")
    #         return True
    #     except StaleElementReferenceException:
    #         self.logger.debug(f"wait_until_element_will_displayed: False")
    #         return False
    #     except TimeoutException:
    #         self.logger.debug(f"wait_until_element_will_displayed: False")
    #         return False
    #
    # def wait_until_element_will_not_displayed(self, locator: tuple, timeout: int = 60) -> bool:
    #     self.logger.debug(
    #         f"wait_until_element_not_displayed(locator {locator}, timeout {timeout}")
    #     time.sleep(3)
    #     try:
    #         wait = WebDriverWait(self.driver, timeout)
    #         wait.until_not(EC.visibility_of_element_located(locator=locator))
    #         self.logger.debug(f"wait_until_element_will_not_displayed: True")
    #         return True
    #     except TimeoutException:
    #         self.logger.debug(f"wait_until_element_will_not_displayed: False")
    #         return False
    #
    # def wait_for_element_with_text(self, locator: tuple, text: str, timeout: int = 10):
    #     self.logger.debug(
    #         f"wait_for_element_with_text(locator {locator}, text {text}, timeout {timeout}")
    #     if not self.wait_for_element(locator=locator, timeout=timeout):
    #         self.logger.debug(
    #             f"wait_for_element_with_text(locator {locator}, text {text}, timeout {timeout}: False")
    #         return False
    #     if not self.get_element_attribute(locator=locator, attr='text').startswith(text):
    #         self.logger.debug(
    #             f"wait_for_element_with_text(locator {locator}, text {text}, timeout {timeout}: False")
    #         return False
    #     if self.wait_until_element_will_enabled(locator=locator, timeout=timeout):
    #         self.logger.debug(
    #             f"wait_for_element_with_text(locator {locator}, text {text}, timeout {timeout}: False")
    #         return False
    #     self.logger.debug(
    #         f"wait_for_element_with_text(locator {locator}, text {text}, timeout {timeout}: True")
    #     return True
