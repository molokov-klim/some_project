import logging
from typing import Union, Any

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException

from core.selenium.web_page import WebPage
from core.selenium.web_elements import WebElement, WebElements, WebElementsFrom
import consts.locators.sigma_cloud_locators as sc_locator


class SubscriptionPage(WebPage):
    """

    Класс описывающий страницу подписок
    https://cloud-qa2.sigma.land/settings/subscription

    """

    def __init__(self, web_driver, url=''):
        url = 'https://cloud-qa2.sigma.land/settings/subscription'
        super().__init__(web_driver, url)

    current_cash_register = WebElement(xpath=sc_locator.XPATH_CURRENT_CASH_REGISTER)
    new_code_button = WebElement(xpath=sc_locator.XPATH_NEW_CODE_BUTTON)
    secret_code_label = WebElement(xpath=sc_locator.XPATH_SECRET_CODE)
    close_modal_window = WebElement(xpath=sc_locator.XPATH_CLOSE_MODAL_WINDOW)
    users = WebElement(xpath=sc_locator.XPATH_USERS)
    profile = WebElement(xpath=sc_locator.XPATH_PROFILE)
    pin = WebElement(xpath=sc_locator.XPATH_PIN)

    def open_current_cash_register(self) -> bool:
        try:
            self.wait_page_loaded(wait_for_element=self.current_cash_register)
            self.current_cash_register.wait_to_be_clickable()
            self.current_cash_register.click()
            return True
        except NoSuchElementException as e:
            logging.error("NoSuchElementException occurred: {}".format(e))
            return False

    def generate_new_device_code(self) -> bool:
        try:
            self.wait_page_loaded(wait_for_element=self.new_code_button)
            for i in range(3):
                self.new_code_button.wait_to_be_clickable()
                self.new_code_button.click()
            return True
        except NoSuchElementException as e:
            logging.error("NoSuchElementException occurred: {}".format(e))
            return False

    def get_secret_code(self) -> Union[bool, str]:
        try:
            self.wait_page_loaded(wait_for_element=self.secret_code_label)
            self.secret_code_label.wait_to_be_clickable()
            secret_code = self.secret_code_label.get_text()
            self.close_modal_window.wait_to_be_clickable()
            self.close_modal_window.click()
            return secret_code
        except NoSuchElementException as e:
            logging.error("NoSuchElementException occurred: {}".format(e))
            return False

    def open_profile(self) -> bool:
        try:
            self.wait_page_loaded(wait_for_element=self.users)
            self.users.wait_to_be_clickable()
            self.users.click()
            return True
        except NoSuchElementException as e:
            logging.error("NoSuchElementException occurred: {}".format(e))
            return False

    def get_pin(self) -> Union[bool, str]:
        try:
            self.wait_page_loaded(wait_for_element=self.profile)
            self.profile.wait_to_be_clickable()
            self.profile.click()
            self.wait_page_loaded(wait_for_element=self.pin)
            self.pin.wait_to_be_clickable()

            pin_code = self.pin.extract_data_values('div', 'data-value')

            return str(pin_code)
        except NoSuchElementException as e:
            logging.error("NoSuchElementException occurred: {}".format(e))
            return False

