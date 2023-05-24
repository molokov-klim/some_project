import time
import threading
import allure
import pytest

import libfptr10

from core.dto.libfptr10 import IFptr
import config
import json
import logging

logger = logging.getLogger(config.LOGGER_NAME)

fptr = IFptr(
    '/\\atol.ru\\FSRoot\\Develop\\ДРО\\Builds\\Drivers_v10\\Core\\tags\\10.9.4.30\\nt-x86-msvc2015')  # Создание объекта ДТО
# action = fptr.showProperties(fptr.LIBFPTR_GUI_PARENT_NATIVE, 0)


if config.MODEL == "ATOL_AUTO":
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(IFptr.LIBFPTR_MODEL_ATOL_AUTO))  # Модель: Автоматически АТОЛ
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_COM))  # Канал связи COM порт
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_COM_FILE, f"COM{config.COM_PORT}")  # Номер COM порта

if config.MODEL == "SIGMA":
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_MODEL, str(99999))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_TCPIP))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_IPADDRESS, str(config.IP_ADRESS))
    fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_IPPORT, str(config.IP_PORT))

fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_AUTO_RECONNECT, str(True))
fptr.applySingleSettings()  # Запись настроек


def is_connected(timeout=5):
    logger.debug("ККТ is_connected() timeout %s", timeout)
    connected = False

    def check_connection():
        nonlocal connected
        fptr.open()
        if fptr.isOpened():
            fptr.close()
            logger.debug("ККТ is_connected() True")
            connected = True
        fptr.close()

    timer = threading.Timer(timeout, check_connection)
    timer.start()

    while not connected and timer.is_alive():
        time.sleep(0.1)

    timer.cancel()

    logger.debug("ККТ is_connected() %s", connected)
    return connected


def get_fd_from_fn(fd: int):
    """
    Извлечение ФД из ФН
    """
    logger.debug(f"get_fd_from_fn() < {fd}")
    if fd is None:
        logger.debug(f"get_fd_from_fn() > None")
        return None
    # JSON задание для чтения документа из ФН
    json_task = {
        "type": "getFnDocument",
        "fiscalDocumentNumber": int(fd),
        "withRawData": False
    }
    fd_fn = execute_json(json_task)
    if fd_fn is None:
        return None
    if isinstance(fd_fn, dict):
        fd_fn = fd_fn['documentTLV']
        return fd_fn
    return None


def wait_to_connect(timeout=300):
    logger.debug(f"wait_to_connect() timeout={timeout}")
    start_time = time.time()
    while not is_connected() and not time.time() - start_time > timeout:
        logger.debug(f"Не получен ответ от ККТ, time {time.time() - start_time} timeout {timeout}")
    if is_connected():
        logger.debug("ККТ доступна")
        return True
    logger.debug("ККТ не отвечает")
    return False


def execute_json(json_task, timeout=30):
    logger.debug(f"execute_json() < json_task {json_task}, timeout {timeout}")
    try:
        if not is_connected():
            if not wait_to_connect(timeout=timeout):
                return False
        fptr.open()
        fptr.setParam(IFptr.LIBFPTR_PARAM_JSON_DATA, json.dumps(json_task))
        fptr.processJson()
        response_raw = fptr.getParamString(IFptr.LIBFPTR_PARAM_JSON_DATA)
        if response_raw is not None:
            try:
                response = json.loads(response_raw)
                logger.debug(f"execute_json() > {response}")
                return response
            except json.decoder.JSONDecodeError as e:
                logger.error('[ERROR] error with json.loads from response: {}'.format(e))
    except libfptr10.error as e:
        logger.error('Exception in execute_json(): {}'.format(e))
    finally:
        fptr.close()  # Закрытие ДТО
    logger.debug(f"execute_json() > None")
    return None


def get_last_fd_number():
    logger.debug("get_last_fd_number()")
    try:
        json_task = {
            "type": "getFnStatus"
        }
        fn_status = execute_json(json_task)
        logger.debug("СТАТУС ФН: %s", fn_status)
        last_fd_number = fn_status['fnStatus']['fiscalDocumentNumber']
        logger.debug(f"get_last_fd_number() > {last_fd_number}")
        logger.info("ФД: %s", last_fd_number)
        return last_fd_number
    except Exception as e:
        logger.error("get_last_fd_number error: {}".format(e))
        logger.debug("get_last_fd_number() > None")
        return None


def get_fn_number_from_fd_json(fd_json: dict):
    """
    Получение номера ФД из JSON_ФД
    """
    logger.debug(f"get_fn_number_from_fd_json() < {fd_json}")
    fn = None
    if fd_json is None:
        logger.debug(f"get_fn_number_from_fd_json() > {fn}")
        return None
    for key in fd_json:
        if key == "1041":
            fn = fd_json[key]
    logger.debug(f"get_fn_number_from_fd_json() > {fn}")
    return fn


def get_not_sent_fd_qty():
    logger.debug(f"get_not_sent_fd_qty()")
    task = {
        "type": "ofdExchangeStatus"
    }
    ofdExchangeStatus = execute_json(task)
    if ofdExchangeStatus is not None:
        not_sent_fd_qty = ofdExchangeStatus['status']['notSentCount']
        logger.debug(f"get_not_sent_fd_qty() %s", not_sent_fd_qty)
        return not_sent_fd_qty
    logger.debug(f"get_not_sent_fd_qty() None")
    return None


def wait_for_sent_all_fd(timeout: int = 600):
    logger.debug(f"wait_for_sent_all_fd() timeout %s", timeout)
    start_time = time.time()
    while get_not_sent_fd_qty() != 0:
        if time.time() - start_time > timeout:
            logger.debug(f"get_not_sent_fd_qty() False")
            return False
        time.sleep(3)
    logger.debug(f"get_not_sent_fd_qty() True")
    return True


def execute_mass_json(json_task, quantity, timeout=30):
    logger.debug(f"execute_json() < json_task {json_task}, timeout {timeout}")
    print(f"execute_json() < json_task {json_task}, timeout {timeout}")
    try:
        if not is_connected():
            if not wait_to_connect(timeout=timeout):
                return False
        fptr.open()
        count = 0
        while count < quantity:
            fptr.setParam(IFptr.LIBFPTR_PARAM_JSON_DATA, json.dumps(json_task))
            fptr.processJson()
            print(count)
            count += 1
    except libfptr10.error as e:
        logger.error('Exception in execute_json(): {}'.format(e))
    finally:
        fptr.close()  # Закрытие ДТО
    logger.debug(f"execute_json() > None")
    return None


def get_TPG_count():
    """
    Получить ресурс ТПГ (постоянный)
    """
    if not is_connected():
        if not wait_to_connect(timeout=60):
            return False
    fptr.open()
    fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_TERMAL_RESOURCE)
    fptr.setParam(IFptr.LIBFPTR_PARAM_COUNTER_TYPE, IFptr.LIBFPTR_CT_ROLLUP)
    fptr.queryData()
    count = fptr.getParamInt(IFptr.LIBFPTR_PARAM_COUNT)

    if count == 0:
        print_info_report()

    return count

def get_TPG_temperature():
    """
    Получить температуру ТПГ
    """
    if not is_connected():
        if not wait_to_connect(timeout=60):
            return False
    fptr.open()

    fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_PRINTER_TEMPERATURE)
    fptr.queryData()

    temperature = fptr.getParamString(IFptr.LIBFPTR_PARAM_PRINTER_TEMPERATURE)
    return temperature


def get_TPG_motor_count():
    """
    Получить ресурс шагового двигателя
    """
    if not is_connected():
        if not wait_to_connect(timeout=60):
            return False
    fptr.open()

    fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_STEP_RESOURCE)
    fptr.setParam(IFptr.LIBFPTR_PARAM_COUNTER_TYPE, IFptr.LIBFPTR_CT_ROLLUP)
    fptr.setParam(IFptr.LIBFPTR_PARAM_STEP_COUNTER_TYPE, IFptr.LIBFPTR_SCT_OVERALL)
    fptr.queryData()

    count = fptr.getParamInt(IFptr.LIBFPTR_PARAM_COUNT)

    return count

def print_info_report():
    if not is_connected():
        if not wait_to_connect(timeout=60):
            return False
    fptr.open()

    fptr.setParam(IFptr.LIBFPTR_PARAM_REPORT_TYPE, 5)
    fptr.setParam(IFptr.LIBFPTR_PARAM_REPORT_ELECTRONICALLY, 0)
    fptr.report()


def print_custom_text(text_tuple: tuple):
    """
    Метод печати нефискального текста на ЧЛ
    """
    if not is_connected():
        if not wait_to_connect(timeout=60):
            return False
    fptr.open()
    fptr.beginNonfiscalDocument()

    for text in text_tuple:
        fptr.setParam(IFptr.LIBFPTR_PARAM_TEXT, text)
        fptr.setParam(IFptr.LIBFPTR_PARAM_ALIGNMENT, 0)
        fptr.setParam(IFptr.LIBFPTR_PARAM_TEXT_WRAP, 0)
        fptr.setParam(IFptr.LIBFPTR_PARAM_FONT, 0)
        fptr.setParam(IFptr.LIBFPTR_PARAM_FONT_DOUBLE_HEIGHT, False)
        fptr.setParam(IFptr.LIBFPTR_PARAM_FONT_DOUBLE_WIDTH, False)
        fptr.setParam(IFptr.LIBFPTR_PARAM_FORMAT_TEXT, False)
        fptr.setParam(IFptr.LIBFPTR_PARAM_LINESPACING, 0)
        fptr.setParam(IFptr.LIBFPTR_PARAM_BRIGHTNESS, 0)
        fptr.setParam(IFptr.LIBFPTR_PARAM_STORE_IN_JOURNAL, True)
        fptr.printText()
    fptr.setParam(IFptr.LIBFPTR_PARAM_PRINT_FOOTER, False)
    fptr.endNonfiscalDocument()



