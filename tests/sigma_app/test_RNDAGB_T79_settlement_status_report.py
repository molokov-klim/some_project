# coding: utf-8
import allure
import pytest
from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import print_test_info


@print_test_info("Отчет о состоянии расчетов")
@allure.title("Отчет о состоянии расчетов")
@allure.feature("Сигма Касса")
@allure.story("")
@allure.id("")
def test_RNDAGB_T79_settlement_status_report(sk_without_install_fixture, shift_manager):
    # Инициализация
    app = sk_without_install_fixture

    # ПРИХОД
    # Добавление товара в корзину
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['vat'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['vat_20'],
                                  quantity=5)
    # Добавление товара в корзину
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['vat'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['vat_10'],
                                  quantity=3)
    # Добавление товара в корзину
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['vat'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['vat_0'],
                                  quantity=3)
    # Перемещение к оплате
    app.transfer_to_payment(tag_1054='income', payment_method='combo')
    # Обработка оплаты
    app.process_one_receipt_combo(cash_method='digit_buttons', amount_cash='3')
    # Перемещение в чеки и возвраты
    app.transfer_to_receipts_and_returns()
    # Возврат последнего чека
    app.refund_last_receipt(refund_method='combo')
    # Перемещение в основное окно товары
    app.transfer_from_receipts_and_returns()

    # РАСХОД
    # Перемещение в кассовые операции
    app.transfer_to_cash_transaction()
    # Внесение
    app.deposit_cash(amount=50)
    # Перемещение в основное окно товары
    app.transfer_from_cash_transaction()
    # Добавление товара в корзину
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['vat'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['vat_20'],
                                  quantity=5)
    # Добавление товара в корзину
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['vat'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['vat_10'],
                                  quantity=3)
    # Добавление товара в корзину
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['vat'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['vat_without'],
                                  quantity=3)
    # Перемещение к оплате
    app.transfer_to_payment(tag_1054='outcome', payment_method="cash")
    # Обработка оплаты
    app.process_one_receipt_cash()
    # Перемещение в чеки и возвраты
    app.transfer_to_receipts_and_returns()
    # Возврат последнего чека
    app.refund_last_receipt(refund_method="cash")
    # Перемещение в основное окно товары
    app.transfer_from_receipts_and_returns()

    # КОРРЕКЦИЯ ПРИХОД
    # Переход в чек коррекции
    app.transfer_to_correction_receipt(timeout=25)
    # Формирование и запись чека коррекции
    app.make_correction_receipt_FFD_1_05(corr_type='income',
                                         corr_basis='myself',
                                         corr_fd_number='25',
                                         corr_date="15.09.2022",
                                         corr_payment_type='cash',
                                         corr_amount=4,
                                         corr_vat_type='Без НДС',
                                         corr_vat_amount=1,
                                         quantity_character_remove=1,
                                         additional_vats=[('20%', 0.5, 4), ])
    # Переход в основное окно товары
    app.transfer_from_cash_transaction()

    # КОРРЕКЦИЯ РАСХОД
    # Переход в чек коррекции
    app.transfer_to_correction_receipt(timeout=25)
    # Формирование и запись чека коррекции
    app.make_correction_receipt_FFD_1_05(corr_type='outcome',
                                         corr_basis='fns',
                                         corr_fd_number='28',
                                         corr_date="15.09.2022",
                                         corr_payment_type='electronically',
                                         corr_amount=4.25,
                                         corr_vat_type='10/110',
                                         corr_vat_amount=0.2,
                                         quantity_character_remove=4,
                                         additional_vats=[('20/120', 0.33, 4), ])
    # Переход в основное окно товары
    app.transfer_from_cash_transaction()

    # ВНЕСЕНИЕ / ВЫПЛАТА
    # Сумма внесения
    deposit = 50
    # Сумма изъятия
    withdraw = 25
    # Перемещение в кассовые операции
    app.transfer_to_cash_transaction()
    # Внесение
    app.deposit_cash(amount=deposit)
    # Изъятие
    app.withdraw_cash(amount=withdraw)
    # Перемещение в основное окно товары
    app.transfer_from_cash_transaction()

    # Отчет о состоянии расчетов
    # Перемещение в кассовые операции
    app.transfer_to_cash_transaction()

    # Отчет о состоянии расчетов
    app.make_calc_report()

    # Перемещение в главное окно
    app.transfer_from_cash_transaction()


