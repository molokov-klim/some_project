# coding: utf-8
import allure
from consts.locators import sigma_kassa_locators as sk_locator
from core.decorators.decorators import print_test_info
from test_data.FFD_1_05.agents import all_agents


@print_test_info("Проверка агентов")
@allure.title("Проверка агентов")
@allure.feature("Сигма Касса")
@allure.story("Добавление в корзину всех типов агентов, пробитие чека наличными без сдачи, "
              "сравнение эталона и ФН, сравнение ФН и ОФД")
@allure.id("#12494")
def test_RNDAGB_T1010_check_agents(sk_without_install_fixture, shift_manager, dto_comparer):
    # Инициализация
    app = sk_without_install_fixture
    comparer = dto_comparer

    # Словарь изменений, необходимых внести в эталонный ФД перед сравнением
    # При значении None - тег удаляется
    changes = {
        "1012": None,
        "1038": None,
        "1040": None,
    }

    # Объявление эталона
    etalon = all_agents

    # # Добавление товаров в корзину
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['bank_pay_agent'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['agent_bank_pay_agent'])
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['bank_pay_subagent'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['agent_bank_pay_subagent'])
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['pay_agent'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['agent_pay_agent'])
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['pay_subagent'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['agent_pay_subagent'])
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['other_agent'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['agent_other'])
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['comissioner'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['agent_comissioner'])
    app.add_item_to_cart_specific(category=sk_locator.CATALOG_CATEGORIES_LOCATORS['attorney'],
                                  item=sk_locator.CATALOG_ITEM_LOCATORS['agent_attorney'])
    # Перемещение к оплате
    app.transfer_to_payment(tag_1054='income', payment_method='cash')
    # Обработка оплаты
    app.process_one_receipt_cash(cash_method='keep_change')
    # Сравнение ФД
    comparer.compare_etalon_fn_ofd(etalon=etalon, changes=changes)
