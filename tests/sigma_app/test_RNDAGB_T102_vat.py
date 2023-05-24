# coding: utf-8
import allure
import pytest
from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import print_test_info
from test_data.FFD_1_05.vat import all


@print_test_info("Проверка ставок НДС")
@allure.title("Проверка ставок НДС")
@allure.feature("Сигма Касса")
@allure.story("Проведение чека прихода с товарами содержащими все ставки НДС. "
              "Сравнение ФД")
@allure.id("#11530")
def test_RNDAGB_T102_vat(sk_without_install_fixture, shift_manager, dto_comparer):
    # Инициализация
    app = sk_without_install_fixture
    comparer = dto_comparer

    vat = ['vat_0',
           'vat_without',
           'vat_20',
           'vat_20_120',
           'vat_10',
           'vat_10_110',
           ]

    # Словарь изменений, необходимых внести в эталонный ФД перед сравнением
    # None - удалить
    changes = {
        "1054": 1,  # признак расчета (1 - приход)
        "1012": None,  # 1012
        "1038": None,  # номер смены
        "1040": None,  # номер ФД
    }

    # Объявление эталона
    etalon = all

    # Добавление товара в корзину
    for item in vat:
        app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['vat'],
                                      item=sk_locator.CATALOG_ITEM_LOCATORS[item])
    # Перемещение к оплате
    app.transfer_to_payment(tag_1054='income', payment_method='cash')
    # Обработка оплаты
    app.process_one_receipt_cash()

    # Сравнение ФД
    comparer.compare_etalon_fn_ofd(etalon=etalon, changes=changes)
