# coding: utf-8
from consts.locators import sigma_kassa_locators as sk_locator

from applications.SigmaCashRegister.sk_num_pad import SigmaAppNumPad


class SigmaAppFirstRun(SigmaAppNumPad):
    def __init__(self):
        super().__init__()

    def process_welcome_window(self):
        """
        Обработка окна приветствия
        """
        assert self.wait_for_window(locator=sk_locator.WELCOME_TV_MESSAGE,
                                    text=sk_locator.WELCOME_TV_MESSAGE_TEXT,
                                    timeout=10)
        assert self.tap_to_element(sk_locator.WELCOME_BTN_NEXT)
        return True

    def process_choose_country_window(self):
        """
        Обработка выбора страны
        """
        assert self.wait_for_window(locator=sk_locator.COUNTRY_TV_TITLE,
                                    text=sk_locator.COUNTRY_TV_TITLE_TEXT,
                                    timeout=10)
        assert self.tap_to_element(sk_locator.COUNTRY_BTN_RUSSIA)
        assert self.tap_to_element(sk_locator.COUNTRY_BTN_NEXT)
        return True

    def process_choose_business_type_window(self):
        """
        Обработка выбора типа бизнеса
        """
        assert self.wait_for_window(locator=sk_locator.BUSINESS_TYPE_TV_TITLE,
                                    text=sk_locator.BUSINESS_TYPE_TV_TITLE_TEXT,
                                    timeout=10)
        assert self.tap_to_element(sk_locator.BUSINESS_TYPE_BTN_RETAIL)
        assert self.tap_to_element(sk_locator.BUSINESS_TYPE_BTN_NEXT)
        return True

    def process_change_server(self):
        """
        Обработка выбора тестового сервера
        """
        assert self.wait_for_window(locator=sk_locator.REGISTRATION_TV_WELCOME_MESSAGE,
                                    text=sk_locator.REGISTRATION_TV_WELCOME_MESSAGE_TEXT,
                                    timeout=10)
        assert self.tap_to_element(sk_locator.REGISTRATION_BTN_LOGO)
        assert self.tap_to_element(sk_locator.MODAL_CHANGE_SERVER_BTN_SWITCH)
        assert self.tap_to_element(sk_locator.MODAL_CHANGE_SERVER_MENU_ITEM_ENTER_QA2)
        assert self.tap_to_element(sk_locator.MODAL_CHANGE_SERVER_BTN_OK)
        return True

    def process_enter_device_code(self, device_code):
        """
        Ввод кода устройства
        """
        assert self.wait_for_window(locator=sk_locator.ENTER_DEVICE_CODE_TV_TITLE,
                                    text=sk_locator.ENTER_DEVICE_CODE_TV_TITLE_TEXT,
                                    timeout=10)
        assert self.tap_to_element(sk_locator.REGISTRATION_BTN_DEVICE_CODE)
        assert self.input_device_code(device_code)
        assert self.process_modal_already_have_cashregister()
        return True

    def process_modal_already_have_cashregister(self):
        """
        Проверка и обработка модального окна 'уже есть работающая касса'
        """
        if self.wait_for_window(locator=sk_locator.MODAL_ALREADY_HAVE_CASHREGISTER_TV_TITLE,
                                text=sk_locator.MODAL_ALREADY_HAVE_CASHREGISTER_TV_TITLE_TEXT,
                                timeout=3):
            assert self.tap_to_element(locator=sk_locator.MODAL_ALREADY_HAVE_CASHREGISTER_BTN_OK, timeout=3)
        return True

    def process_loading_wait(self):
        """
        Ожидание получения данных из ЛК
        """
        assert self.wait_until_element_will_not_displayed(locator=sk_locator.LOADING_FIRST_LAUNCH_IMG_PROGRESS,
                                                          timeout=300)
        return True

    def process_list_items(self):
        """
        Обработка модального окна выбора типа отображения товаров
        """
        if self.wait_for_element(locator=sk_locator.MODAL_CHANGE_DISPLAY_TYPE_BTN_CANCEL, timeout=10):
            assert self.tap_to_element(sk_locator.MODAL_CHANGE_DISPLAY_TYPE_BTN_CANCEL)
            assert self.wait_for_window(locator=sk_locator.MAIN_HEADER_TV_TITLE,
                                        text=sk_locator.MAIN_HEADER_TV_TITLE_GOODS_TEXT,
                                        timeout=10)
        return True
