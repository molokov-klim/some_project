# coding: utf-8
import time

import allure
import pytest

import config
from consts.locators import sigma_kassa_locators as sk_locator
from core.dto import dto
from test_data.FFD_1_05.tag_1214 import tag_1214
from core.decorators.decorators import print_test_info

options = [
    'внести предоплату',
    'зачесть предоплату',
    'передача в кредит',
    'оплата кредита',
]


@print_test_info("Проверка значений 1214")
@allure.title("Проверка значений 1214")
@allure.feature("Сигма Касса")
@allure.story("")
@allure.id("")
def test_RNDAGB_T107_check_1214(sk_without_install_fixture, dto_comparer, shift_manager):
    # Инициализация
    app = sk_without_install_fixture
    comparer = dto_comparer

    # Словарь изменений, необходимых внести в эталонный ФД перед сравнением
    # None - удалить
    changes = {
        "1012": None,  # дата и время
        "1038": None,  # номер смены
        "1040": None,  # номер ФД
    }

    # Объявление эталона
    etalon = tag_1214

    # Добавление в корзину товаров своя цена
    app.add_custom_price(quantity=5)

    # Добавление скидки
    app.transfer_to_cart()

    for option in options:
        app.choose_custom_price_item_options(option=option)
        app.input_by_num_pad(number='0,5', num_pad=sk_locator.SIMPLE_NUM_PAD)
        app.tap_to_element(locator=sk_locator.ADD_CASH_NEXT)

    app.tap_to_element(locator=sk_locator.CART_BTN_BACK)

    # Перемещение к оплате
    app.transfer_to_payment(tag_1054='income', payment_method="cash")
    # Обработка оплаты
    app.process_one_receipt_cash()

    # Сравнение ФД
    comparer.compare_etalon_fn_ofd(etalon=etalon, changes=changes)
