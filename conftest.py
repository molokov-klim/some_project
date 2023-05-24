# coding: utf-8
from datetime import datetime
import os
import re
import time
from typing import Union
import allure
import pytest
import config

from core.adb import adb
from core.dto import dto
from core.operations import operations
from core.telegram import telegram_bot
from consts.locators import sigma_kassa_locators as sk_locator
from core.logger.logger import logging_autotest, logging_adb_full, logging_adb_appium, logging_adb_dto

from applications.SigmaCashRegister.sk_main import SigmaCashRegister
from core.fd_compare.compare import ComparerTaxcom
from core.selenium.pages.sigma_cloud.sc_auth_page import AuthPage
from applications.OpenVPN.openVPN import OpenVPN
from core.selenium.pages.sigma_cloud.sc_subscription_page import SubscriptionPage

from core.test_manager.test_manager import TestManagerHelper

START_DIR = os.getcwd()
PROJECT_ROOT_DIR = os.path.dirname(__file__)
os.chdir(PROJECT_ROOT_DIR)

TEST_MANAGER = TestManagerHelper(start_dir=START_DIR, project_root_dir=PROJECT_ROOT_DIR)

folder_path = os.path.join(TEST_MANAGER.results_directory, 'logs')
logger = logging_autotest(folder_path)
sk_app = SigmaCashRegister()


def pytest_cmdline_preparse(config, args):
    logger.debug("pytest_cmdline_preparse()")
    arguments = []
    allure_report_dir = os.path.join(TEST_MANAGER.results_directory, "Allure")
    arguments.append(f'--alluredir={allure_report_dir}')
    # arguments.append(f'--driver Chrome')
    # arguments.append(f'--driver-path "core/selenium/chromedriver/chromedriver.exe"')
    args.extend(arguments)


def pytest_report_teststatus(report, config):
    report_result = "test report: {}".format(report)
    if "teardown" not in report_result and "setup" not in report_result:
        test_name = re.search("::(.+?)'", report_result).group(1)
        outcome = re.search("outcome='(.+?)'", report_result).group(1)
        report = test_name + ": " + outcome
        telegram_bot.send_message_text(report)


@pytest.fixture(scope='session', autouse=True)
def logging(request):
    folder_path = os.path.join(TEST_MANAGER.results_directory, 'logs')
    logger = None
    logger = logging_autotest(folder_path)
    logger.debug("fixture logging()")
    logcat_process_adb_full = logging_adb_full(folder_path)
    logger.debug("logcat_process_adb_full: %s", type(logcat_process_adb_full))
    logcat_process_adb_appium = logging_adb_appium(folder_path)
    logger.debug("logcat_process_adb_appium: %s", type(logcat_process_adb_full))
    logcat_process_adb_dto = logging_adb_dto(folder_path)
    logger.debug("logcat_process_adb_appium: %s", type(logcat_process_adb_dto))

    def logging_finalizer(logger):
        if logger.handlers:
            for handler in logger.handlers:
                logger.removeHandler(handler)

        logcat_process_adb_full.terminate()
        logcat_process_adb_appium.terminate()
        logcat_process_adb_dto.terminate()
        operations.copy_file(source=config.dto_logs_path, destination=folder_path)

        adb.kill_all('logcat')
        # прикрепление логов к отчету
        log_path = os.path.join(TEST_MANAGER.results_directory, "logs")
        for log_file_name in os.listdir(log_path):
            if os.path.splitext(log_file_name)[1] == '.log':
                file_path = os.path.join(log_path, log_file_name)
                allure.attach.file(file_path, name=log_file_name, attachment_type=allure.attachment_type.TEXT)

        logger.debug("td logcat_process_adb_full: %s", type(logcat_process_adb_full))

    yield logger
    request.addfinalizer(lambda: logging_finalizer(logger))


@pytest.fixture(scope='function', autouse=True)
def logger_video_record(request):
    logger.debug("fixture logger_video_record()")
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = 'screenrecord_{}.mp4'.format(timestamp)
    record_process = adb.record_video(filename)

    def video_finalizer():
        adb.stop_video()
        folder_path = os.path.join(TEST_MANAGER.results_directory)
        if record_process is not None:
            record_process.terminate()
        time.sleep(5)  # ждем пока видео сформируется на устройстве
        adb.pull_video(path=folder_path)
        # прикрепление видео к отчету
        video_path = os.path.join(TEST_MANAGER.results_directory, "Movies")
        # for video_file_name in os.listdir(video_path):
        #     if os.path.splitext(video_file_name)[1] == '.mp4':
        #         file_path = os.path.join(video_path, video_file_name)
        #         allure.attach.file(file_path, name=video_file_name, attachment_type=allure.attachment_type.MP4)
        file_path = os.path.join(video_path, filename)
        allure.attach.file(file_path, name=filename, attachment_type=allure.attachment_type.MP4)

    request.addfinalizer(video_finalizer)


@allure.title('Фикстура установки headers браузеру')
@pytest.fixture()
def chrome_options(chrome_options):
    logger.debug("fixture chrome_options()")
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')
    return chrome_options


@allure.title('Фикстура инициализации браузера и финализации браузера')
@pytest.fixture()
def web_browser(request, selenium):
    logger.debug("fixture web_browser()")
    browser = selenium
    browser.set_window_size(1400, 1000)

    def web_browser_finalizer(browser):
        browser.quit()

    yield browser
    request.addfinalizer(lambda: web_browser_finalizer(browser))


@allure.title('Фикстура инициализации и удаления ComparerTaxcom()')
@pytest.fixture(scope='function', autouse=True)
def dto_comparer(request):
    comparer = ComparerTaxcom()

    def dto_comparer_finalizer(comparer):
        del comparer

    yield comparer
    request.addfinalizer(lambda: dto_comparer_finalizer(comparer))


@allure.title('Фикстура для получения кода активации Sigma Касса с cloud-qa2.sigma.land')
@pytest.fixture()
def device_code(web_browser) -> Union[None, str]:
    logger.debug("fixture device_code()")
    auth_page = AuthPage(web_browser)
    assert auth_page.sign_in(config.SIGMA_CLOUD_EMAIL, config.SIGMA_CLOUD_PASSWORD)
    subscription_page = SubscriptionPage(web_browser)
    assert subscription_page.open_current_cash_register()
    assert subscription_page.generate_new_device_code()
    secret_code = subscription_page.get_secret_code()
    assert secret_code.isnumeric()
    return secret_code


@allure.title('Фикстура установки и активации OpenVPN')
@pytest.fixture(scope='session', autouse=False)
def openVPN(skip: bool = False):
    if skip:
        logger.debug("fixture openVPN() SKIP")
        return True

    logger.debug("fixture openVPN()")
    if not adb.check_VPN():
        logger.debug("VPN is disabled, try to enable")
        app = OpenVPN()
        assert app.push_keys()
        assert app.connect_without_install()
        if not app.check_vpn_for_readiness():
            # app.push_keys()
            assert app.agree_permissions()
            assert app.add_keys()
            assert app.turn_on()
            assert app.check_request()
            time.sleep(1)
        assert adb.press_home()
    return True


def sk_force_reconnect():
    adb.close_app(sk_locator.PACKAGE)
    sk_app.disconnect()
    sk_app.start(install=False)
    sk_app.foreground_app_by_adb(sk_locator.ACTIVITY_LAUNCHABLE)
    sk_app.input_pin_code(config.SIGMA_KASSA_PIN_CODE)
    sk_app.open_shift()
    sk_app.clear_cart()

@allure.title('Открытие и закрытие смены')
@pytest.fixture(scope='function', autouse=False)
def shift_manager(request):
    sk_app.input_pin_code(number=config.SIGMA_KASSA_PIN_CODE, timeout=3)
    sk_app.open_shift(cash='0', timeout=30)
    sk_app.clear_cart()

    def shift_manager_finalizer():
        #logging()
        if not SigmaCashRegister.is_running:
            sk_force_reconnect()
        sk_app.close_shift()

    yield sk_app
    request.addfinalizer(shift_manager_finalizer)


@allure.title('Основная фикстура подготовки и финализации приложения Сигма Касса, без установки приложения')
@pytest.fixture(scope='session', autouse=True)
def sk_without_install_fixture(request):
    logger.debug("fixture sk_without_install_fixture")
    assert dto.is_connected()
    adb.close_app(sk_locator.PACKAGE)
    sk_app.start(install=False)
    sk_app.foreground_app_by_adb(sk_locator.ACTIVITY_LAUNCHABLE)

    def sk_without_install_fixture_finalizer():
        #logging()
        sk_app.disconnect()
        adb.close_app(sk_locator.PACKAGE)

    yield sk_app
    request.addfinalizer(sk_without_install_fixture_finalizer)


# @allure.title('Фикстура подготовки и финализации приложения Сигма Касса, без установки приложения, без открытия смены')
# @pytest.fixture(scope='function')
# def sk_without_install_and_without_open_shift_fixture(request):
#     adb.close_app(sk_locator.PACKAGE)
#     sk_app.start(install=False)
#     sk_app.foreground_app_by_adb(sk_locator.ACTIVITY_LAUNCHABLE)
#     if sk_app.wait_for_window(locator=sk_locator.PIN_CODE_TV_TITLE,
#                            text=sk_locator.PIN_CODE_TV_TITLE_TEXT,
#                            timeout=10):
#         sk_app.input_pin_code(config.SIGMA_KASSA_PIN_CODE)
#
#     def sk_without_install_and_without_open_shift_fixture_finalizer():
#         sk_app.disconnect()
#         adb.close_app(sk_locator.PACKAGE)
#
#     yield sk_app
#     request.addfinalizer(lambda: sk_without_install_and_without_open_shift_fixture_finalizer())


@pytest.fixture(scope="function", autouse=True)
def check_session():
    if not SigmaCashRegister.is_running:
        logger.warning("\nAppium Client is not responding, reconnect")
        sk_force_reconnect()
    logger.info("\nAppium Client is running, continue")

