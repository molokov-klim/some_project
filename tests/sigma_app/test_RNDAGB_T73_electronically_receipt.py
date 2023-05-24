# coding: utf-8
import time

import allure
import pytest

import config
from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import print_test_info
from core.dto import dto


@print_test_info("Электронный чек")
@allure.title("Электронный чек")
@allure.feature("Сигма Касса")
@allure.story("")
@allure.id("")
def test_RNDAGB_T73_electronically_receipt(sk_without_install_fixture, shift_manager):
    # Инициализация
    app = sk_without_install_fixture

    # Выключение принтера чеков
    app.turn_receipt_printer(on=False)

    # Добавление товара в корзину
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['bank_pay_agent'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['agent_bank_pay_agent'],
                                  quantity=1)

    # Перемещение к оплате
    app.transfer_to_payment(tag_1054='income', payment_method='cash', electronically=True)
    # Замер прогона ТПГ
    TPG = dto.get_TPG_count()
    # Обработка оплаты
    app.process_one_receipt_cash(cash_method='keep_change')
    # Проверка прогона ТПГ
    TPG_NEW = dto.get_TPG_count()
    assert TPG == TPG_NEW


    # Добавление email электронного чека
    app.add_email_electronically_receipt(quantity_character_remove=20, email=config.ELECTRONICALLY_FD_EMAIL)
    # Добавление товара в корзину
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['bank_pay_agent'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['agent_bank_pay_agent'],
                                  quantity=1)
    # Перемещение к оплате
    app.transfer_to_payment(tag_1054='income', payment_method='cash',
                            company_email=config.ELECTRONICALLY_FD_EMAIL, electronically=True)
    # Замер прогона ТПГ
    TPG = dto.get_TPG_count()
    # Обработка оплаты
    app.process_one_receipt_cash(cash_method='keep_change')
    # Проверка прогона ТПГ
    TPG_NEW = dto.get_TPG_count()
    assert TPG == TPG_NEW

    # Переключает печать чеков
    app.turn_receipt_printer(on=True)
