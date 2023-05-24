# coding: utf-8
import allure

from core.decorators.decorators import print_test_info


@print_test_info("Внесение/выплата")
@allure.title("Внесение/выплата")
@allure.feature("Сигма Касса")
@allure.story("Перемещение в кассовые операции, проведение внесения, изъятия и "
              "после этого сравнение наличных в кассе с начальным значением")
@allure.id("#11556")
def test_RNDAGB_T71_income_outcome(sk_without_install_fixture, shift_manager):
    # Инициализация
    app = sk_without_install_fixture

    # Сумма внесения
    deposit = 50
    # Сумма изъятия
    withdraw = 25
    # Перемещение в кассовые операции
    app.transfer_to_cash_transaction()
    # Получение текущей суммы в кассе
    start_amount = app.get_cash_in_cashbox()
    # Внесение
    app.deposit_cash(amount=deposit)
    # Изъятие
    app.withdraw_cash(amount=withdraw)
    # Получение текущей суммы в кассе
    after_withdraw_amount = app.get_cash_in_cashbox()
    # Перемещение в основное окно товары
    app.transfer_from_cash_transaction()
    app.deposit_withdraw_compare(after_withdraw_amount=after_withdraw_amount,
                                 start_amount=start_amount,
                                 deposit=deposit,
                                 withdraw=withdraw)
