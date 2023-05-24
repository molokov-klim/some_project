import logging
import time

from selenium.common import WebDriverException

from core.selenium.web_page import WebPage
from core.selenium.web_elements import WebElement
import consts.locators.sigma_cloud_locators as sc_locator


class AuthPage(WebPage):
    """

    Класс описывающий страницу аутентификации
    https://cloud-qa2.sigma.land/login

    """

    def __init__(self, web_driver):
        url = 'https://cloud-qa2.sigma.land/login'
        super().__init__(web_driver, url)

    email_input = WebElement(xpath=sc_locator.XPATH_INPUT_EMAIL)
    password_input = WebElement(xpath=sc_locator.XPATH_INPUT_PASSWORD)
    submit_button = WebElement(xpath=sc_locator.XPATH_SUBMIT_BUTTON)

    def sign_in(self, email, password) -> bool:
        try:
            self.email_input.send_keys(email)
            self.password_input.send_keys(password)
            self.submit_button.click()
            self.wait_page_loaded(wait_for_element=sc_locator.XPATH_CURRENT_CASH_REGISTER)
            return True
        except WebDriverException as e:
            logging.error('Ошибка аутентификации: '.format(e))
            return False
