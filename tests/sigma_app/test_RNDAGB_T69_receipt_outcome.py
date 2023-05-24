# coding: utf-8
import allure
from consts.locators import sigma_kassa_locators as sk_locator
from test_data.FFD_1_05.vat import vat_20
from core.dto import dto
from core.decorators.decorators import print_test_info


@print_test_info("Чек расхода")
@allure.title("Чек расхода")
@allure.feature("Сигма Касса")
@allure.story("Включает расход в настройках, добавляет и пробивает чек расхода, сравнивает ФД: эталон, ФН, ОФД")
@allure.id("#11543")
def test_RNDAGB_T69_receipt_outcome(sk_without_install_fixture, shift_manager, dto_comparer):

    # Инициализация объектов из фикстур
    app = sk_without_install_fixture
    comparer = dto_comparer

    # Словарь изменений, необходимых внести в эталонный ФД перед сравнением
    changes = {
        "1031": 1,
        "1081": 0,
        "1054": 3,
    }

    # Объявление эталона
    etalon = vat_20

    # Перемещение в кассовые операции
    app.transfer_to_cash_transaction()
    # Внесение
    app.deposit_cash(amount=50)
    # Перемещение в основное окно товары
    app.transfer_from_cash_transaction()

    # Включение настройки "Использовать расход"
    app.turn_on_outcome_items()

    # Добавление товара в корзину
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['vat'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['vat_20'])
    # Перемещение к оплате
    app.transfer_to_payment(tag_1054='outcome', payment_method='cash')
    # Обработка оплаты
    app.process_one_receipt_cash(cash_method='keep_change')

    # Сравнение ФД
    comparer.compare_etalon_fn_ofd(etalon=etalon, changes=changes)

