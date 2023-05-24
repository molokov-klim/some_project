# coding: utf-8
import logging
import config
import allure

from core.decorators.decorators import print_test_info
from test_data.FFD_1_05.correction import correction_income

logger = logging.getLogger(config.LOGGER_NAME)


@print_test_info("Чек коррекции прихода")
@allure.title("Чек коррекции прихода")
@allure.feature("Сигма Касса")
@allure.story("Переход в формирование чека коррекции, пробитие чека коррекции прихода, "
              "сравнение ФД: Эталон - ФН; ФН - ОФД")
@allure.id("#11546")
def test_RNDAGB_T116_correction_receipt_income(sk_without_install_fixture, shift_manager, dto_comparer):
    # Инициализация объектов из фикстур
    app = sk_without_install_fixture
    comparer = dto_comparer

    # Словарь изменений, необходимых внести в эталонный ФД перед сравнением
    # При значении None - тег удаляется из эталона
    changes = {
        "1012": None,  # дата, время (ФД)
        "1038": None,  # номер смены
        "1040": None,  # номер ФД
    }

    # Объявление эталона
    etalon = correction_income

    # Переход в чек коррекции
    app.transfer_to_correction_receipt(timeout=25)
    # Формирование и запись чека коррекции
    app.make_correction_receipt_FFD_1_05(corr_type='income',
                                         corr_basis='myself',
                                         corr_fd_number='25',
                                         corr_date="15.09.2022",
                                         corr_payment_type='cash',
                                         corr_amount=4,
                                         corr_vat_type='Без НДС',
                                         corr_vat_amount=1,
                                         quantity_character_remove=1,
                                         additional_vats=[('20%', 0.5, 4), ])
    # Переход в основное окно товары
    app.transfer_from_cash_transaction()
    # Сравнение ФД
    comparer.compare_etalon_fn_ofd(etalon=etalon, changes=changes)
