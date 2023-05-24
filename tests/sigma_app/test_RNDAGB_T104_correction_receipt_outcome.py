# coding: utf-8
import allure

from core.decorators.decorators import print_test_info
from test_data.FFD_1_05.correction import correction_outcome

@print_test_info("Чек коррекции расхода")
@allure.title("Чек коррекции расхода")
@allure.feature("Сигма Касса")
@allure.story("Переход в формирование чека коррекции, пробитие чека коррекции расхода, "
              "сравнение ФД: Эталон - ФН; ФН - ОФД")
@allure.id("#12212")
def test_RNDAGB_T104_correction_receipt_outcome(sk_without_install_fixture, shift_manager, dto_comparer):
    # Инициализация
    app = sk_without_install_fixture
    comparer = dto_comparer

    # Объявление эталона
    etalon = correction_outcome
    # Словарь изменений, необходимых внести в эталонный ФД перед сравнением
    changes = {
        "1012": None,  # время ФД
        "1038": None,  # номер смены
        "1040": None,  # номер ФД
        "1042": None,  # номер чека за смену
    }
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
    # Сравнение ФД
    comparer.compare_etalon_fn_ofd(etalon=etalon, changes=changes)
