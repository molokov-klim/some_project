# coding: utf-8
import allure
from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import print_test_info
from test_data.FFD_1_05.tax_system import patent


@print_test_info("Оплата безналичными всех типов чеков")
@allure.title("Оплата безналичными всех типов чеков")
@allure.feature("Сигма Касса")
@allure.story("Чек прихода оплатой безналичными")
@allure.id("#11552")
def test_RNDAGB_T65_pay_card_all_types_receipts(sk_without_install_fixture, shift_manager, dto_comparer):
    # Инициализация объектов из фикстур
    app = sk_without_install_fixture
    comparer = dto_comparer

    # Словарь изменений, необходимых внести в эталонный ФД перед сравнением
    changes = {
        "1081": 1,
        "1031": 0,
    }

    # Объявление эталона
    etalon = patent

    # Добавление товара в корзину
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['patent'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['tax_system_patent'])
    # Перемещение к оплате
    app.transfer_to_payment(tag_1054='income', payment_method='card')
    # Обработка оплаты
    app.process_one_receipt_card()

    # Сравнение ФД
    comparer.compare_etalon_fn_ofd(etalon=etalon, changes=changes)

