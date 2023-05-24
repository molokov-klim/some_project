# coding: utf-8
import allure
import pytest

import config
from core.decorators.decorators import print_test_info
from test_data.FFD_1_05.shift import open_shift

# # Динамические тестовые данные для параметризации теста
# 0 - сумма внесения для первой итерации, 1 - сумма внесения для второй итерации
testdata = ('0', '50')


@print_test_info("Открытие смены")
@allure.feature("Сигма Касса")
@allure.story("Открытие смены")
@pytest.mark.parametrize("cash", testdata)
@allure.id("#11534")
def test_RNDAGB_T75_open_shift(sk_without_install_fixture, cash, dto_comparer):
    allure.dynamic.title(f"Открытие смены, внесение: {cash}")
    # Инициализация
    app = sk_without_install_fixture
    comparer = dto_comparer

    app.input_pin_code(number=config.SIGMA_KASSA_PIN_CODE, timeout=3)
    # Открытие смены
    app.open_shift(cash=cash, timeout=30)

    # Объявление эталона
    etalon = open_shift

    # Словарь изменений, необходимых внести в эталонный ФД перед сравнением
    # None - удалить тег
    changes = {
        "1012": None,
        "1188": None,
        "1040": None,
        "1038": None,
    }

    # Сравнение ФД
    comparer.compare_etalon_fn_ofd(etalon=etalon, changes=changes)

    # Закрытие смены
    app.close_shift()

