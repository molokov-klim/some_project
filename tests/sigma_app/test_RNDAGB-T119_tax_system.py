# coding: utf-8
import allure
import pytest
from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import print_test_info
from test_data.FFD_1_05 import tax_system

# # Динамические тестовые данные для параметризации теста
# 0 - эталон, 1- локатор категории, 2 - локатор товара
testdata = (
    (tax_system.patent,
     sk_locator.CATALOG_CATEGORIES_LOCATORS['patent'],
     sk_locator.CATALOG_ITEM_LOCATORS['tax_system_patent']),
    (tax_system.general,
     sk_locator.CATALOG_CATEGORIES_LOCATORS['general'],
     sk_locator.CATALOG_ITEM_LOCATORS['tax_system_general']),
    (tax_system.agricultural,
     sk_locator.CATALOG_CATEGORIES_LOCATORS['agricultural'],
     sk_locator.CATALOG_ITEM_LOCATORS['tax_system_agricultural']),
    (tax_system.simplified_income,
     sk_locator.CATALOG_CATEGORIES_LOCATORS['simplified_income'],
     sk_locator.CATALOG_ITEM_LOCATORS['tax_system_simplified_income']),
    (tax_system.simplified_income_minus_expenses,
     sk_locator.CATALOG_CATEGORIES_LOCATORS['simplified_income_minus_expenses'],
     sk_locator.CATALOG_ITEM_LOCATORS['tax_system_simplified_income_minus_expenses']),
)


@print_test_info("Проверка СНО")
@allure.feature("Сигма Касса")
@allure.story("Проведение чека прихода оплатой наличными со всеми типами СНО,"
              "проверка записи ФД в ФН и передачи в ОФД")
@allure.id("#11531")
@pytest.mark.parametrize("data", testdata)
def test_RNDAGB_T119_tax_system(sk_without_install_fixture, shift_manager, dto_comparer, data):
    allure.dynamic.title(f"Проверка СНО: {data[1]}")
    # Инициализация
    app = sk_without_install_fixture
    comparer = dto_comparer

    # Словарь изменений, необходимых внести в эталонный ФД перед сравнением
    # None - удалить
    changes = {
        "1054": 1,  # признак расчета (1 - приход)
        "1012": None,  # 1012
        "1031": 1,     # сумма наличных
        "1081": 0,     # сумма безналичных
        "1038": None,  # номер смены
        "1040": None,  # номер ФД
    }

    # Объявление эталона
    etalon = data[0]

    # Добавление товара в корзину
    app.add_item_to_cart_specific(category=data[1],
                                  item=data[2])
    # Перемещение к оплате
    app.transfer_to_payment(tag_1054='income', payment_method='cash')
    # Обработка оплаты
    app.process_one_receipt_cash()

    # Сравнение ФД
    comparer.compare_etalon_fn_ofd(etalon=etalon, changes=changes)
