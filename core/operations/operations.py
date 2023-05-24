import re
import os
import logging
import serial.tools.list_ports
import shutil
import json

logger = logging.getLogger('autotest')
START_DIR = os.getcwd()


def extract_numeric(variable):
    number = None
    regex = r'-?\d+(?:,\d+)?'
    match = re.search(regex, variable)
    if match:
        number = float(match.group().replace(',', '.'))
    return number


def find_latest_folder(path: str):
    pattern = re.compile(r"launch_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}")
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    dirs = [d for d in dirs if pattern.match(d)]
    dirs.sort(reverse=True)
    latest_dir = dirs[0]

    return str(latest_dir)


def get_com():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if int(port.device[3:]) > 10:
            try:
                ser = serial.Serial(port.device)
                ser.close()
                return port.device[3:]
            except serial.SerialException:
                pass
    return None


def copy_file(source, destination):
    logger.debug("copy_file() source %s, destination %s", source, destination)
    try:
        shutil.copy(source, destination)
        logger.debug("File copied successfully!")
    except IOError as e:
        logger.error("Unable to copy file: %s" % e)


def count_currency_numbers(number: int) -> tuple:
    """
    Метод вычисляет количество вхождений купюр достоинством 5000, 1000, 500, 100 в сумму.
    Вычисления производятся с наибольшего достоинства, остальные последовательно от остатка.
    Остаток менее 100 игнорируется (важно для вычисления сдачи!)
    """
    if number < 100:
        number = 100
    count_5000 = number // 5000
    remainder = number % 5000
    count_1000 = remainder // 1000
    remainder = remainder % 1000
    count_500 = remainder // 500
    remainder = remainder % 500
    count_100 = remainder // 100
    return (count_5000, count_1000, count_500, count_100)


def read_json(path, filename):
    filepath = os.path.join(START_DIR, path, filename)
    data = None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        logger.error("Файл не найден")
        return None
    return data


def str_to_float(number: str) -> float:
    """
    Метод приводит строковое представление сумм в float
    """
    number = str(number)
    number = float(number.replace(',', '.').replace('₽', '').replace(' ', ''))
    return number
