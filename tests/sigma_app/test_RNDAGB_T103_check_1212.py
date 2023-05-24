# coding: utf-8
import time

import allure
import pytest

import config
from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import print_test_info
from core.dto import dto
from test_data.FFD_1_05.tag_1212 import tag_1212

item_types = [
    "Подакцизный товар",
    "Работа",
    "Услуга",
    "Ставка азартной игры",
    "Выигрыш азартной игры",
    "Лотерейный билет",
    "Выигрыш лотереи",
    "Предоставление результатов интеллектуальной деятельности",
    "Платеж",
    "Агентское вознаграждение",
    "Имущественное право",
    "Внереализационный доход",
    "Иные платежи и взносы",
    "Торговый сбор",
    "Курортный сбор",
    "Выплата",
    "Иной предмет расчета",
    "Залог",
    "Расход",
    "Взносы на ОПС ИП",
    "Взносы на ОПС",
    "Взносы на ОМС ИП",
    "Взносы на ОМС",
    "Взносы на ОСС",
    "Платеж казино",
    "Товар"
]


@print_test_info("Проверка значений 1212")
@allure.title("Проверка значений 1212")
@allure.feature("Сигма Касса")
@allure.story("")
@allure.id("")
def test_RNDAGB_T103_check_1212(sk_without_install_fixture, dto_comparer, shift_manager):
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
    etalon = tag_1212

    # Включение 'использовать полный список признаков расчета'
    app.turn_on_complete_list_settlement()

    # Добавление в корзину товаров своя цена
    app.add_custom_price(quantity=27)

    # Изменение типа товара
    app.transfer_to_cart()
    for item_type in item_types:
        app.choose_type_custom_price_item(item_type=item_type)
    app.tap_to_element(locator=sk_locator.CART_BTN_BACK)

    # Перемещение к оплате
    app.transfer_to_payment(tag_1054='income', payment_method="cash")
    # Обработка оплаты
    app.process_one_receipt_cash()

    # Сравнение ФД
    comparer.compare_etalon_fn_ofd(etalon=etalon, changes=changes)


