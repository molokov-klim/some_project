# coding: utf-8
import allure
from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import print_test_info
from test_data.FFD_1_05.vat import vat_20

@print_test_info("Чек возврата расхода")
@allure.title("Чек возврата расхода")
@allure.feature("Сигма Касса")
@allure.story("Внесение, проведение чека расхода оплатой наличными, картой, комбооплатой (в разных итерациях). "
              "Возврат чека, сравнение ФД.")
@allure.id("#11545")
def test_RNDAGB_T78_receipt_outcome_refund(sk_without_install_fixture, shift_manager, dto_comparer):
    # Инициализация
    app = sk_without_install_fixture
    comparer = dto_comparer

    # Словарь изменений, необходимых внести в эталонный ФД перед сравнением
    changes = {
        "1031": 1,  # сумма по чеку (БСО) наличными
        "1081": 0,  # сумма по чеку (БСО) безналичными
        "1054": 4,  # признак расчета (4 - возврат расхода)
    }
    # Объявление эталона
    etalon = vat_20

    # Перемещение в кассовые операции
    app.transfer_to_cash_transaction()
    # Внесение
    app.deposit_cash(amount=50)
    # Перемещение в основное окно товары
    app.transfer_from_cash_transaction()
    # Добавление товара в корзину
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['vat'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['vat_20'])
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
    # Сравнение ФД
    comparer.compare_etalon_fn_ofd(etalon=etalon, changes=changes)
