# coding: utf-8
import time

from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import my_step_info, screenshots
from core.adb import adb

from applications.SigmaCashRegister.sk_transfer import SigmaAppTransfer


class SigmaAppCorrection(SigmaAppTransfer):
    def __init__(self):
        super().__init__()

        self.valid_correction_types = sk_locator.VALID_1054
        self.correction_types = sk_locator.CORRECTION_TYPES_LOCATORS
        self.valid_correction_bases = sk_locator.VALID_CORRECTION_BASES
        self.correction_bases = sk_locator.CORRECTION_BASES_LOCATORS_FFD_MENU_ITEMS_1_05
        self.valid_correction_payment_types = sk_locator.VALID_PAYMENT_TYPES
        self.correction_payment_methods = sk_locator.CORRECTION_PAYMENT_TYPES_LOCATORS_MENU_ITEMS
        self.valid_correction_vat_types = sk_locator.VALID_VAT_TYPES
        self.correction_vat_types = sk_locator.VAT_TYPES_LOCATORS_MENU_ITEMS_FFD_1_05

    @my_step_info("Формирование и пробитие чека коррекции")
    @screenshots()
    def make_correction_receipt_FFD_1_05(self, corr_type: str, corr_basis: str, corr_fd_number: str, corr_date: str,
                                         corr_payment_type: str, corr_amount: float, corr_vat_type: str,
                                         corr_vat_amount: float = None, additional_vats: list = None,
                                         quantity_character_remove: int = 8):
        """
        Метод формирования и пробития чека коррекции.
        Ожидает окно формирования чека коррекции, отдает окно кассовые операции
        $corr_type: тип коррекции, допустимые значения - ['income', 'outcome'] (приход, расход).
        $corr_basis: основание коррекции, допустимые значения - ['myself', 'fns'] (самостоятельно, по предписанию ФНС).
        $corr_fd_number: номер корректируемого ФД.
        $corr_date: дата корректируемого ФД, формат переменной - str "dd.mm.YY", пример "30.01.2023".
        $corr_payment_type: тип оплаты, допустимые значения - ['cash', 'electronically'] (наличными, безналичными).
        $corr_vat_type: ставка НДС, допустимые значения - ['0%', '10%', '10/110', '20%', '20/120', 'Без НДС']
        $additional_vats: дополнительные ставки НДС. Представляет собой list содержащий tuples значения которых:
        0 - ставка НДС, 1 - сумма НДС, 2 - количество стираемых символов в поле ввода, перед вводом суммы НДС.
        [(corr_vat_type: str, corr_vat_amount: float, quantity_character_remove: int), ],
        $quantity_character_remove, количество стираемых символов в поле ввода, перед вводом суммы НДС.
        """
        assert corr_type in self.valid_correction_types, \
            self.logger.error(f"assertion error: {corr_type} not in {self.valid_correction_types}")
        assert corr_basis in self.valid_correction_bases, \
            self.logger.error(f"assertion error: {corr_basis} not in {self.valid_correction_bases}")
        assert corr_payment_type in self.valid_correction_payment_types, \
            self.logger.error(f"assertion error: {corr_payment_type} not in {self.valid_correction_payment_types}")
        assert corr_vat_type in self.valid_correction_vat_types, \
            self.logger.error(f"assertion error: {corr_vat_type} not in {self.valid_correction_vat_types}")
        assert self.choose_correction_type(corr_type=corr_type)
        assert self.choose_correction_basis(corr_basis=corr_basis)
        assert self.set_correction_fd_number(corr_fd_number=corr_fd_number)
        assert self.set_correction_fd_date(corr_date=corr_date)
        assert self.choose_correction_payment_method(payment_method=corr_payment_type)
        assert self.set_correction_amount(corr_amount=corr_amount)
        assert self.choose_vat_type(corr_vat_type=corr_vat_type)
        if corr_vat_amount is not None:
            assert self.set_vat_amount(corr_vat_amount=corr_vat_amount,
                                       quantity_character_remove=quantity_character_remove)
        if additional_vats is not None:
            for additional_vat in additional_vats:
                assert self.add_vat_type(*additional_vat)
        assert self.submit_correction()
        return True

    def choose_correction_type(self, corr_type: str):
        """
        Метод выбора типа коррекции.
        Ожидает окно формирования чека коррекции, отдает окно формирования чека коррекции
        valid_correction_types = ['income', 'outcome', ]
        """
        assert corr_type in self.valid_correction_types
        assert self.tap_to_element(locator=self.correction_types[corr_type])
        return True

    def choose_correction_basis(self, corr_basis: str):
        """
        Метод выбора основания коррекции.
        Ожидает окно формирования чека коррекции, отдает окно формирования чека коррекции
        valid_correction_bases = ['myself', 'fns', ]
        """
        assert corr_basis in self.valid_correction_bases
        locator = sk_locator.CORRECTION_RECEIPT_FFD_1_05_TV_BASIS
        menu_item_locator = self.correction_bases[corr_basis]
        if not self.is_element_displayed(locator=locator):
            assert self.scroll_to(locator=locator)
        assert self.tap_to_element(locator=locator)
        assert self.tap_to_element(locator=menu_item_locator)
        return True

    def set_correction_fd_number(self, corr_fd_number: str):
        """
        Метод ввода номера корректируемого ФД.
        Ожидает окно формирования чека коррекции, отдает окно формирования чека коррекции
        """
        locator = sk_locator.CORRECTION_RECEIPT_FFD_1_05_ET_FD_NUMBER
        if not self.is_element_displayed(locator=locator):
            assert self.scroll_to(locator=locator)
        assert self.tap_to_element(locator=locator)
        assert adb.input_by_virtual_keyboard(key=corr_fd_number, keyboard=sk_locator.PT5_VIRTUAL_KEYBOARD_NUMBERS)
        adb.press_back()
        return True

    def set_correction_fd_date(self, corr_date: str):
        """
        Метод ввода даты корректируемого ФД.
        Ожидает окно формирования чека коррекции, отдает окно формирования чека коррекции
        corr_date: str, example "30.01.2023", (dd.mm.YY)
        """
        locator = sk_locator.CORRECTION_RECEIPT_FFD_1_05_BTN_DATE
        if not self.is_element_displayed(locator=locator):
            assert self.scroll_to(locator=locator)
        assert self.tap_to_element(locator=locator)
        assert self.modal_set_date(corr_date)
        return True

    def choose_correction_payment_method(self, payment_method: str):
        """
        Метод выбора типа оплаты корректируемого ФД.
        Ожидает окно формирования чека коррекции, отдает окно формирования чека коррекции
        valid_correction_payment_types = ['cash', 'electronically', ]
        """
        assert payment_method in self.valid_correction_payment_types
        locator = sk_locator.CORRECTION_RECEIPT_FFD_1_05_TV_PAYMENT_METHOD
        menu_item_locator = self.correction_payment_methods[payment_method]
        if not self.is_element_displayed(locator=locator):
            assert self.scroll_to(locator=locator)
        assert self.tap_to_element(locator=locator)
        assert self.tap_to_element(locator=menu_item_locator)
        return True

    def set_correction_amount(self, corr_amount: float):
        """
        Метод ввода суммы корректируемого ФД.
        Ожидает окно формирования чека коррекции, отдает окно формирования чека коррекции
        """
        locator = sk_locator.CORRECTION_RECEIPT_FFD_1_05_ET_FD_AMOUNT
        if not self.is_element_displayed(locator=locator):
            assert self.scroll_to(locator=locator)
        assert self.tap_to_element(locator=locator)
        assert adb.input_by_virtual_keyboard(key=str(corr_amount).replace(".", ","),
                                             keyboard=sk_locator.PT5_VIRTUAL_KEYBOARD_NUMBERS)
        adb.press_back()
        return True

    def choose_vat_type(self, corr_vat_type: str):
        """
        Метод выбора ставки НДС корректируемого ФД.
        Ожидает окно формирования чека коррекции, отдает окно формирования чека коррекции
        valid_correction_vat_types = ['0%', '10%', '10/110', '20%', '20/120', 'Без НДС', ]
        """
        assert corr_vat_type in self.valid_correction_vat_types
        locator = sk_locator.CORRECTION_RECEIPT_FFD_1_05_TV_VAT_TYPE
        menu_item_locator = self.correction_vat_types[corr_vat_type]
        if not self.is_element_displayed(locator=locator):
            assert self.scroll_to(locator=locator)
        assert self.tap_to_element(locator=locator)
        assert self.tap_to_element(locator=menu_item_locator)
        return True

    def set_vat_amount(self, corr_vat_amount: float, quantity_character_remove: int = 8):
        """
        Метод ввода суммы НДС корректируемого ФД. Стирает содержимое и вводит новое.
        Ожидает окно формирования чека коррекции, отдает окно формирования чека коррекции
        """
        locator = sk_locator.CORRECTION_RECEIPT_FFD_1_05_ET_VAT_AMOUNT
        if not self.is_element_displayed(locator=locator):
            assert self.scroll_to(locator=locator)
        assert self.tap_to_element(locator=locator)
        for i in range(quantity_character_remove):
            adb.input_keycode(keycode="KEYCODE_DEL")
        assert adb.input_by_virtual_keyboard(key=str(corr_vat_amount).replace(".", ","),
                                             keyboard=sk_locator.PT5_VIRTUAL_KEYBOARD_NUMBERS)
        adb.press_back()
        return True

    def add_vat_type(self, vat_type: str, vat_amount: float = None, quantity_character_remove: int = 8):
        """
        Метод добавления ставки НДС корректируемого ФД.
        Находит и тапает по кнопке "Добавить НДС", выбирает ставку и вводит сумму добавленной НДС.
        Ожидает окно формирования чека коррекции, отдает окно формирования чека коррекции
        """
        add_vat_locator = sk_locator.CORRECTION_RECEIPT_FFD_1_05_BTN_ADD_VAT
        # Нажатие на кнопку "Добавить ставку НДС"
        if not self.is_element_displayed(locator=add_vat_locator):
            assert self.scroll_to(locator=add_vat_locator)
        assert self.tap_to_element(locator=add_vat_locator)
        self.scroll_down_by_adb(max_scrolls=1)

        # Выбор ставки НДС (самый нижний элемент)
        menu_item_locator = self.correction_vat_types[vat_type]
        vat_type_elements = self.driver.find_elements("xpath", "//android.widget.TextView[@text='0%']")
        target_element_index = 1
        if len(vat_type_elements) > 1:
            target_element_index = len(vat_type_elements)
        count = 1
        for element in vat_type_elements:
            if count == target_element_index:
                assert self.directly_tap_to_element(element)
                assert self.tap_to_element(locator=menu_item_locator)
            count += 1

        # Ввод суммы НДС (самый нижний элемент)
        if vat_amount is not None:
            vat_amount_elements = self.driver.find_elements('id', 'ru.sigma.app.debug:id/ndsSumView')
            target_element_index = 1
            if len(vat_amount_elements) > 1:
                target_element_index = len(vat_amount_elements)
            count = 1
            for element in vat_amount_elements:
                if count == target_element_index:
                    assert self.directly_tap_to_element(element)
                    for i in range(quantity_character_remove):
                        adb.tap(*sk_locator.PT5_VIRTUAL_KEYBOARD_NUMBERS["BACKSPACE"])
                    assert adb.input_by_virtual_keyboard(key=str(vat_amount).replace(".", ","),
                                                         keyboard=sk_locator.PT5_VIRTUAL_KEYBOARD_NUMBERS)
                    adb.press_back()
                count += 1
        return True

    def submit_correction(self):
        """
        Метод печати корректируемого ФД.
        Ожидает окно формирования чека коррекции, отдает главное окно товары (если введены все поля).
        """
        locator = sk_locator.CORRECTION_RECEIPT_FFD_1_05_BTN_OK
        assert self.tap_to_element(locator=locator)
        time.sleep(1)
        assert self.wait_until_element_will_not_displayed(
            locator=sk_locator.CORRECTION_RECEIPT_FFD_1_05_IMG_PROGRESS)
        assert self.wait_for_window(locator=sk_locator.CASH_TRANSACTIONS_TV_TITLE,
                                    text=sk_locator.CASH_TRANSACTIONS_TV_TITLE_TEXT,
                                    timeout=60)
        return True

