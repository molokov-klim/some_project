import logging

import requests

import config
from config import INTEGRATOR_ID, USER_DATA
import time

logger = logging.getLogger(config.LOGGER_NAME)


def get_token():
    """
    Получение токена от Такском ОФД
    """
    # print("get_token()")
    headers = {"Content-Type": "application/json", "Integrator-ID": INTEGRATOR_ID}
    url = 'http://api-tlk-ofd.taxcom.ru/API/v2/Login'
    sessionToken = None
    try:
        response = requests.post(url, allow_redirects=False)
    except requests.exceptions.RequestException as e:
        raise Exception(
            f'[ERROR] with get token from ofd: {e}')
    try:
        if response.status_code == 301:
            response = requests.post(response.headers['Location'], headers=headers, json=USER_DATA)
            sessionToken = response.json()['sessionToken']
    except requests.exceptions.RequestException as e:
        raise Exception(
            f'[ERROR] with get token from ofd: {e}')
    # time.sleep(2)
    return sessionToken


def get_fd_from_taxcom(fn_number: int, fd: int, timeout: int = 300):
    """
    Получение ФД от Такском ОФД
    """
    logger.debug(f"get_fd_from_taxcom() < fn_number {fn_number}, fd {fd}")
    if fn_number is None:
        logger.debug(f"get_fd_from_ofd() > None")
        return None
    headers = {"Session-Token": get_token()}
    data = {"fn": str(fn_number), "fd": str(fd)}
    url = 'https://api-tlk-ofd.taxcom.ru/API/v2/DocumentInfo'
    response = requests.get(url, headers=headers, params=data, allow_redirects=True)
    fd_taxcom = None
    logger.debug(f"headers: {headers} \ndata: {data}")
    try:
        start_time = time.time()
        while not time.time() - start_time > timeout:
            response = requests.get(url, headers=headers, params=data, allow_redirects=True)
            logger.info("response: %s", response)
            time.sleep(1)
            if response.status_code == 200:
                fd_taxcom = response.json()['document']
                return fd_taxcom
    except requests.exceptions.RequestException as e:
        raise Exception(f'[ERROR] with get fd from ofd: {e}')



def get_fd_from_cri(fn: str, fd: str):
    """
    Получение ФД от ЦРИ ОФД - не реализовано
    """
    # print("not implemented, please use taxcom ofd")
    logger.error("method not implemented")
    return False
