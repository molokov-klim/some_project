# coding: utf-8
import allure
import pytest
from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import print_test_info
from test_data.FFD_1_05.vat import vat_20

# # Динамические тестовые данные для параметризации теста
# 0 - сумма фактической оплаты наличными, 1 - сумма безналичными (1081), 2 - сумма наличными (1031)
testdata = (
    (100, 0, 1),
    (0.2, 0.8, 0.2),
    (0, 1, 0),
)


@print_test_info("Смешанная оплата всех типов чеков")
@allure.feature("Сигма Касса")
@allure.story("Проведение чека расхода комбооплатой, проверка пин пада, "
              "проверка отображения сдачи, сравнение ФД: Эталон - ФН; ФН - ОФД")
@pytest.mark.parametrize("data", testdata)
@allure.id("#11553")
def test_RNDAGB_T121_pay_combo_all_types_receipts(sk_without_install_fixture, shift_manager, data: tuple, dto_comparer):
    allure.dynamic.title(f"Смешанная оплата всех типов чеков: сумма фактической оплаты наличными: {data[0]},  "
                         f"сумма безналичными (1081): {data[1]}, сумма наличными (1031): {data[2]}")
    # Инициализация
    app = sk_without_install_fixture
    comparer = dto_comparer

    # Сумма оплаты наличными
    amount_cash = data[0]

    # Словарь изменений, необходимых внести в эталонный ФД перед сравнением
    changes = {
        "1031": data[2],    # сумма по чеку (БСО) наличными
        "1081": data[1],    # сумма по чеку (БСО) безналичными
        "1054": 1,          # признак расчета (1 - приход)
    }
    # Объявление эталона
    etalon = vat_20
    # Добавление товара в корзину
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['vat'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['vat_20'])
    # Перемещение к оплате
    app.transfer_to_payment(tag_1054='income', payment_method='combo')
    # Обработка оплаты
    app.process_one_receipt_combo(cash_method='digit_buttons',
                                  amount_cash=str(amount_cash))
    # Сравнение ФД
    comparer.compare_etalon_fn_ofd(etalon=etalon, changes=changes)
