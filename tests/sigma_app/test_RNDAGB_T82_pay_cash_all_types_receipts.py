# coding: utf-8
import allure
import pytest
from consts.locators import sigma_kassa_locators as sk_locator
from applications.SigmaCashRegister.sk_payment import SigmaAppPayment
from core.decorators.decorators import print_test_info
from test_data.FFD_1_05.vat import vat_20

# Динамические тестовые данные для параметризации теста
# self.cash_methods = {
# 'keep_change': self.receive_cash_payment_keep_change, - прием наличных кнопкой "без сдачи"
# 'banknote_buttons': self.receive_cash_payment_banknote_buttons,   - прием наличных кнопками банкнот
# 'digit_buttons': self.receive_cash_payment_digits,    - прием наличных цифровыми кнопками
# }
testdata = SigmaAppPayment().cash_methods


@print_test_info("Оплата наличными всех типов чеков")
@allure.feature("Сигма Касса")
@allure.story("Проведение чека расхода оплатой наличными, проверка недоступности кнопки оплаты при "
              "недостаточной сумме, проверка отображения сдачи и ее соответствия, "
              "проверка записи ФД в ФН и передачи в ОФД, соответствия документов")
@pytest.mark.parametrize("cash_method", testdata)
@allure.id("#11529")
def test_RNDAGB_T82_pay_cash_all_types_receipts(sk_without_install_fixture, shift_manager, cash_method, dto_comparer):
    allure.dynamic.title(f"Оплата наличными всех типов чеков: {cash_method}")
    # Инициализация
    app = sk_without_install_fixture
    comparer = dto_comparer

    # Объявление эталона
    etalon = vat_20
    # Словарь изменений, необходимых внести в эталонный ФД перед сравнением
    changes = {
        "1081": 0,      # сумма по чеку (БСО) безналичными
        "1031": 1,      # сумма по чеку (БСО) наличными
        "1054": 1,      # признак расчета (1 - приход)
    }

    # Добавление товара в корзину
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['vat'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['vat_20'])
    # Перемещение к оплате
    app.transfer_to_payment(tag_1054='income', payment_method='cash')
    # Проверка неактивности кнопки проведения оплаты при вводе суммы оплаты 0,01 руб.
    app.is_pay_btn_inactive()
    # Обработка оплаты
    app.process_one_receipt_cash(cash_method=cash_method,
                                 amount='9876')

    # Сравнение ФД
    comparer.compare_etalon_fn_ofd(etalon=etalon, changes=changes)

