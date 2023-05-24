# coding: utf-8
import json
import logging

from core.allure.allure_op import attach_compare_results
from core.decorators.decorators import my_step_info

import config
from core.ofd import ofd_taxcom
from core.dto import dto
from core.utils import utils
from consts.tags import tags

logger = logging.getLogger(config.LOGGER_NAME)


class ComparerTaxcom:

    def __init__(self):
        # Конечный результат обработки
        self.result = {}
        # Белый лист, проверка отключена
        self.__white_list = ["1162", "1077", "fiscalDocumentType", "qr", "short"]

        self.__cast_methods = {
            'BYTE': self.__cast_byte,
            'INT16': self.__cast_int16,
            'INT32': self.__cast_int32,
            'VLN': self.__cast_vln,
            'FPD': self.__cast_fpd,
            'STRING': self.__cast_string,
            'COINS': self.__cast_coins,
            'UNIXTIME': self.__cast_unixtime,
            'FVLN': self.__cast_fvln,
            'STLV': self.__cast_stlv,
            'ENUM': self.__cast_enum,
            'SET': self.__cast_set,
            'BITS': self.__cast_bits,
            'BYTES': self.__cast_bytes,
        }

        self.etalon_value = None
        self.comparable_value = None

    def compare(self, comparable: dict, etalon: dict, cast: bool = True):
        """
        Сравнение по тегам ФД из ФН и ОФД
        """
        for key in etalon:
            if key in comparable:
                if key in self.__white_list:
                    continue
                self.etalon_value = etalon[key]
                self.comparable_value = comparable[key]
                if cast:
                    try:
                        self.__cast_to_one_type(key=str(key), comparable=self.comparable_value,
                                                etalon=self.etalon_value)
                    except Exception as e:
                        logger.error("Exception: {}".format(e))
                        logger.error("params: tag = %s, etalon = %s, comparable = %s", key, etalon[key],
                                     comparable[key])
                if tags[key]['Type'] == 'STLV':
                    self.__cast_stlv(key=str(key), comparable=self.comparable_value, etalon=self.etalon_value)
                if str(self.comparable_value) == str(self.etalon_value):
                    self.__message_pass(key, self.comparable_value, self.etalon_value)
                else:
                    self.__message_fail(key, self.comparable_value, self.etalon_value)
            else:
                self.__message_not_found(key, self.etalon_value)
        return True

    @my_step_info("Сравнение ФД")
    def compare_etalon_fn_ofd(self, etalon: dict, changes: dict = None):
        """
        Метод сравнивает эталон с последним ФД в ФН, затем последний ФД в ФН с ФД в ОФД.
        """
        logger.debug("compare_etalon_fn_ofd()")
        logger.info("Сравнение ФД, ЭТАЛОН : ФН")
        if bool(changes):
            utils.change_values_in_dict(dict_needs_to_change=etalon, changes=changes)
        comparable = dto.get_fd_from_fn(dto.get_last_fd_number())
        self.compare(etalon=etalon,
                     comparable=comparable,
                     cast=False)

        logger.debug("etalon: %s", etalon)
        logger.debug("comparable: %s", comparable)
        logger.debug("compare_result: %s", self.result)
        self.output_result_to_log()
        attach_compare_results(result=self.result, name="Результат сравнения ФД. ЭТАЛОН - ФН")
        assert not self.is_have_failed()
        dto.wait_for_sent_all_fd()
        logger.info("Сравнение ФД, ФН : ОФД")
        self.compare_last_fd_in_fn_and_ofd()
        logger.debug("etalon: %s", etalon)
        logger.debug("comparable: %s", comparable)
        logger.debug("compare_result: %s", self.result)
        self.output_result_to_log()
        attach_compare_results(result=self.result, name="Результат сравнения ФД. ФН - ОФД")
        assert not self.is_have_failed()
        return True

    def compare_last_fd_in_fn_and_ofd(self, modif_fd_number: int = 0):
        logger.debug("compare_last_fd_in_fn_and_ofd()")
        try:
            fd_number = dto.get_last_fd_number() + modif_fd_number
            fd_fn = dto.get_fd_from_fn(
                fd=fd_number)
            fn = dto.get_fn_number_from_fd_json(fd_fn)
            fd_ofd = ofd_taxcom.get_fd_from_taxcom(fn_number=fn, fd=fd_number)
            self.compare(etalon=fd_fn, comparable=fd_ofd)
            return True
        except Exception as e:
            logger.error("compare() error: {}".format(e))
            return False

    def output_result_to_log(self):
        if not self.result:
            logger.error("Результат сравнения пуст")
        else:
            for tag in self.result:
                if not self.result[tag][1] == '___WHITE_LIST___':
                    logger.info(
                        f"{self.result[tag][1]} | {self.result[tag][2]} | etalon {self.result[tag][4]} | "
                        f"compared {self.result[tag][3]} | {self.result[tag][5]}")

    def calc_result(self):
        logger.debug("calc_result()")
        test_result = {tag: 0 for tag in ['passed', 'skipped', 'not_founded', 'failed']}
        if not self.result:
            logger.error("Результат сравнения пуст")
            return None
        for tag in self.result:
            if self.result[tag][1] == "+++PASS+++":
                test_result['passed'] += 1
            if self.result[tag][1] == "__SKIP__":
                test_result['skipped'] += 1
            if self.result[tag][1] == "===NOT_FOUND===":
                test_result['not_founded'] += 1
            if self.result[tag][1] == "---FAIL---":
                test_result['failed'] += 1
        logger.debug("calc_result(): %s", test_result)
        return test_result

    def is_have_failed(self):
        logger.debug("is_have_failed()")
        if not self.result:
            logger.error("Результат сравнения пуст")
            return True
        test_result = self.calc_result()
        if test_result['failed'] != 0 or test_result['not_founded'] != 0:
            logger.debug("is_have_failed(): True")
            self.clear()
            return True
        logger.debug("is_have_failed(): False")
        logger.info("ФД совпали")
        self.clear()
        return False

    def clear(self):
        """
        Очистка результата сравнения
        """
        self.result = {}
        return True

    def __cast_to_one_type(self, key, etalon, comparable):
        if tags[key]['Type'] in self.__cast_methods:
            key_method = tags[key]['Type']
            if not self.__cast_methods[key_method](key, etalon, comparable):
                return False

    def __cast_byte(self, key, etalon, comparable):
        if comparable == 0 or "0":
            self.comparable_value = False
        if comparable == 1 or "1":
            self.comparable_value = True
        if etalon == 0 or "0":
            self.etalon_value = False
        if etalon == 1 or "1":
            self.etalon_value = True
        return True

    def __cast_int16(self, key, etalon, comparable):
        return True

    def __cast_int32(self, key, etalon, comparable):
        return True

    def __cast_vln(self, key, etalon, comparable):
        return True

    def __cast_fpd(self, key, etalon, comparable):
        return True

    def __cast_string(self, key, etalon, comparable):
        if type(etalon) != type(comparable):
            self.etalon_value = etalon[0].strip()
        else:
            self.etalon_value = etalon.strip()
        self.comparable_value = comparable.strip()
        return True

    def __cast_coins(self, key, etalon, comparable):
        etalon = float(etalon)
        comparable = float(comparable)
        if etalon > comparable:
            self.etalon_value = etalon / 100
            self.comparable_value = float(comparable)
        if comparable > etalon:
            self.comparable_value = comparable / 100
            self.etalon_value = float(etalon)
        return True

    def __cast_unixtime(self, key, etalon, comparable):
        self.etalon_value = self.__remove_timezone(data=etalon)
        self.comparable_value = self.__remove_timezone(data=comparable)
        return True

    def __cast_fvln(self, key, etalon, comparable):
        etalon = str(etalon).strip()
        comparable = str(comparable).strip()
        try:
            self.etalon_value = float(etalon)
            self.comparable_value = float(comparable)
        except ValueError:
            try:
                self.etalon_value = int(etalon)
                self.comparable_value = int(comparable)
                return True
            except ValueError:
                return False
        return True

    def __cast_stlv(self, key, etalon, comparable):
        if not self.__expand_stlv(etalon=etalon, comparable=comparable):
            return False
        return True

    def __cast_enum(self, key, etalon, comparable):
        return True

    def __cast_set(self, key, etalon, comparable):
        return True

    def __cast_bits(self, key, etalon, comparable):
        return True

    def __cast_bytes(self, key, etalon, comparable):
        return True

    def __expand_stlv(self, comparable, etalon):
        if self.__is_list(comparable, etalon):
            if not isinstance(comparable, list) and isinstance(etalon, list):
                self.compare(comparable=comparable, etalon=etalon[0])
                return True
            elif isinstance(comparable, list) and not isinstance(etalon, list):
                self.compare(comparable=comparable[0], etalon=etalon)
                return True
            elif isinstance(comparable, list) and isinstance(etalon, list):
                for i in etalon:
                    self.compare(comparable=comparable[etalon.index(i)], etalon=i)
                return True
        return False

    def __is_list(self, comparable, etalon):
        if isinstance(comparable, list) or isinstance(etalon, list):
            return True
        else:
            return False

    def __remove_timezone(self, data):
        if "+" in data:
            return data.split("+")[0]
        return data

    def __append_to_result(self, status, message, key, comparable, etalon):
        """
        Добавление в итоговый результат
        """
        try:
            if not key in self.__white_list:
                self.result[len(self.result) + 1] = status, message, key, comparable, etalon, tags[str(key)]['Name']
                return True
            self.result[len(self.result) + 1] = True, "___WHITE_LIST___", key, comparable, etalon
            return True
        except Exception as e:
            logger.error("[ERROR] ", status, message, key, comparable, etalon)
            logger.error("Exception: {}".format(e))
            return False

    def __message_pass(self, key, comparable, etalon):
        """
        Добавление в итоговый лист положительный результат сравнения
        """
        if not self.__append_to_result(True, "+++PASS+++", key, comparable, etalon):
            return False
        return True

    def __message_fail(self, key, comparable, etalon):
        """
        Добавление в итоговый лист отрицательный результат сравнения
        """
        if not self.__append_to_result(False, "---FAIL---", key, comparable, etalon):
            return False
        return True

    def __message_not_found(self, key, etalon):
        """
        Добавление в итоговый лист неудавшееся сравнение
        """
        if not self.__append_to_result(False, "===NOT_FOUND===", key, "None", etalon):
            return False
        return True

    def __message_error(self, key, comparable, etalon):
        """
        Добавление в итоговый лист сообщение об ошибке в обработке тега
        """
        if not self.__append_to_result(False, "[ERROR]", key, comparable, etalon):
            return False
        return True

    def __message_skip(self, key, comparable, etalon):
        """
        Добавление в итоговый лист сообщения о пропуске обработки тега
        """
        if not self.__append_to_result(True, "__SKIP__", key, comparable, etalon):
            return False
        return True
