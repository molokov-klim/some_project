# coding: utf-8
import allure
import pytest
from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import print_test_info
from test_data.FFD_1_05.vat import vat_20

# Динамические тестовые данные для параметризации теста
# 0 - способ оплаты, 1 - способ возврата/отмены, 2 - сумма наличных, 3 - сумма безналичных
test_data = (
    ("cash", "cancel", 1, 0),
    ("card", "cancel", 0, 1),
    ("combo", "refund", 0.2, 0.8),
)


@print_test_info("Чек возврата прихода")
@allure.feature("Сигма Касса")
@allure.story("Проведение чека прихода оплатой наличными, картой, комбооплатой (в разных итерациях). "
              "Возврат чека, сравнение ФД.")
@pytest.mark.parametrize("data", test_data)
@allure.id("#11544")
def test_RNDAGB_T109_receipt_income_refund(sk_without_install_fixture, shift_manager, dto_comparer, data):
    allure.dynamic.title(f"Чек возврата прихода: способ оплаты {data[0]}, способ возврата/отмены {data[1]}, "
                         f"сумма наличных {data[2]}, сумма безналичных {data[3]}")
    # Инициализация
    app = sk_without_install_fixture
    comparer = dto_comparer

    # Словарь зависимости значения способа оплаты в тестовых данных и вызываемого метода для его обработки
    process_one_receipt = {
        "cash": app.process_one_receipt_cash,
        "card": app.process_one_receipt_card,
        "combo": app.process_one_receipt_combo,
    }
    # Аргументы для вызываемых методов определенных в словаре зависимости способа оплаты
    args = {
        "cash": ('keep_change', 100.0),
        "card": (),
        "combo": ('digit_buttons', '0,2')
    }
    # Словарь изменений, необходимых внести в эталонный ФД перед сравнением
    changes = {
        "1031": data[2],    # сумма по чеку (БСО) наличными
        "1081": data[3],    # сумма по чеку (БСО) безналичными
        "1054": 2,          # признак расчета (2 - возврат прихода)
    }
    # Прием переменных из тестовых данных
    payment_method = data[0]
    card_cancel_method = data[1]
    # Объявление эталона
    etalon = vat_20
    # Добавление товара в корзину
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['vat'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['vat_20'])
    # Перемещение к оплате
    app.transfer_to_payment(tag_1054='income', payment_method=payment_method)
    # Обработка оплаты
    process_one_receipt[payment_method](*args[payment_method])
    # Перемещение в чеки и возвраты
    app.transfer_to_receipts_and_returns()
    # Возврат последнего чека
    app.refund_last_receipt(refund_method=payment_method, card_cancel_method=card_cancel_method)
    # Перемещение в основное окно товары
    app.transfer_from_receipts_and_returns()
    # Сравнение ФД
    comparer.compare_etalon_fn_ofd(etalon=etalon, changes=changes)
