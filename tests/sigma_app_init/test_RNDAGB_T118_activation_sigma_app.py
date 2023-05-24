import allure
import config
from core.adb import adb
from consts.locators import sigma_kassa_locators as sk_locator
from applications.SigmaCashRegister.sk_main import SigmaCashRegister
import logging

logger = logging.getLogger(config.LOGGER_NAME)


@allure.title("Активация Sigma Касса")
@allure.feature("Сигма Касса")
@allure.description("https://jira.atol.ru/secure/Tests.jspa#/testCase/RNDAGB-T118")
@allure.story(
    "Прохождение сценария активации Сигма Кассы. Тип бизнеса: розничная торговля, страна: Россия. "
    "Код устройства и пин код от кассы забирается из облака")
@allure.id("#12096")
def test_RNDAGB_T118_activation_sigma_app(device_code):
    logger.info("Запуск теста: активация Sigma Касса")
    # Запуск Sigma Kassa
    adb.close_app(sk_locator.PACKAGE)
    app = SigmaCashRegister(install=True)

    # Нажатие по кнопке 'Настроить кассу'
    assert app.process_welcome_window()

    # "Выбор страны 'Россия'
    assert app.process_choose_country_window()

    # Выбор типа бизнес 'Розничная торговля'
    assert app.process_choose_business_type_window()

    # "Изменение контура на enter-qa2.sigma.land"
    assert app.process_change_server()

    # "Ввод кода устройства"
    assert app.process_enter_device_code(device_code=device_code)

    # "Ввод пин кода"
    assert app.input_pin_code(config.SIGMA_KASSA_PIN_CODE)

    # "Ожидание загрузки данных из ЛК"
    assert app.process_loading_wait()

    # "Открытие смены"
    assert app.open_shift(cash='50', timeout=3)

    # "Товары в виде списка"
    assert app.process_list_items()

    # "Закрыть смену"
    assert app.close_shift()

