import logging
from datetime import datetime
import os
import subprocess
import time

import coloredlogs

import config
from core.adb import adb
from core.operations import operations

logger = logging.getLogger(config.LOGGER_NAME)

def logging_autotest(folder_path):

    os.makedirs(folder_path, exist_ok=True)
    filepath = os.path.join(folder_path, 'autotest.log')

    logger = logging.getLogger(config.LOGGER_NAME)
    logger.setLevel(config.LOGGER_LEVEL)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(filepath, encoding='utf-8')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    coloredlogs.install(level=config.LOGGER_LEVEL, logger=logger)

    return logger

def logging_adb_full(folder_path):
    try:
        filepath = os.path.join(folder_path, 'adb_full.log')
        command = f"adb logcat > {filepath} HWComposer:s"
        logcat_process_adb_full = subprocess.Popen(command, shell=True)

        return logcat_process_adb_full


    except subprocess.CalledProcessError as e:
        logger.error(f"AdbFullLogger [Error]: {e}")


def logging_adb_appium(folder_path):
    try:
        filepath = os.path.join(folder_path, 'adb_appium.log')
        command = f"adb logcat > {filepath} appium:i *:s"
        logcat_process_adb_full = subprocess.Popen(command, shell=True)

        return logcat_process_adb_full


    except subprocess.CalledProcessError as e:
        logger.error(f"AdbFullLogger [Error]: {e}")

def logging_adb_dto(folder_path):
    try:
        filepath = os.path.join(folder_path, 'adb_dto.log')
        command = f"adb logcat > {filepath} Drivers10:i *:s"
        logcat_process_adb_full = subprocess.Popen(command, shell=True)

        return logcat_process_adb_full


    except subprocess.CalledProcessError as e:
        logger.error(f"AdbFullLogger [Error]: {e}")





# def start_video():
#     try:
#         record_video_process = adb.record_video()
#         return record_video_process
#
#     except subprocess.CalledProcessError as e:
#         logger.error(f"AdbFullLogger [Error]: {e}")
#
# def stop_video(folder_path):
#     try:
#         adb.kill_by_name('screenrecord')
#         print(subprocess.check_output(["adb", "shell", "ps", "|", "grep", "'screenrecord'"]).decode("utf-8"))
#         time.sleep(5)
#         print(subprocess.check_output(["adb", "shell", "ps", "|", "grep", "'screenrecord'"]).decode("utf-8"))
#         #adb.pull(source='/sdcard/Movies/', destination=folder_path)
#
#         print("folder_path: ", folder_path)
#         command = f'adb pull /sdcard/Movies/ {folder_path}'
#         #subprocess.run(command)
#         subprocess.run(command, shell=True)
#         time.sleep(5)
#         #adb.delete_files_from_internal_storage(path='/sdcard/Movies/')
#
#     except subprocess.CalledProcessError as e:
#         logger.error(f"AdbFullLogger [Error]: {e}")






#
#
#
# class DataStructureLogger:
#     def __init__(self):
#         self.logger_name = None
#         self.save_to_file = None
#         self.logger = None
#         self.level = None
#         self.filepath = None
#         self.logcat_process = None
#         self.adb_full_pid = None
#         self.filepath = None
#         self.logcat_process_adb_full = None
#         self.pid_adb_full = None
#         self.filepath = None
#         self.logcat_process_adb_appium = None
#         self.pid_adb_appium = None
#         self.filepath = None
#
#
# class AutotestLogger(DataStructureLogger):
#     def __init__(self, logger_name: str = 'UNKNOWN', save_to_file: bool = True, level: str = 'DEBUG',
#                  filepath: str = None):
#         super().__init__()
#         self.logger_name = logger_name
#         self.save_to_file = save_to_file
#         self.logger = None
#         self.level = level
#         self.filepath = os.path.join(filepath, 'autotest.log')
#
#     def __enter__(self):
#         self.logger = logging.getLogger(self.logger_name)
#         self.logger.setLevel(logging.DEBUG)
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         if self.save_to_file:
#             handler = logging.FileHandler(self.filepath, encoding='utf-8')
#             handler.setFormatter(formatter)
#             self.logger.addHandler(handler)
#         coloredlogs.install(level=self.level, logger=self.logger)
#         #return self.logger
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type:
#             self.logger.error(f"An error occurred: {exc_type} {exc_val}", exc_info=True)
#         if self.logger:
#             for handler in self.logger.handlers:
#                 self.logger.removeHandler(handler)
#
#
# class AdbFullLogger(DataStructureLogger):
#     def __init__(self, filepath: str = None):
#         super().__init__()
#         self.logcat_process_adb_full = None
#         self.pid_adb_full = None
#         self.filepath = os.path.join(filepath, 'adb_full.log')
#
#     def __enter__(self):
#         try:
#             command = f"adb logcat > {self.filepath} HWComposer:s"
#             # with subprocess.Popen(command, shell=True) as process:
#             #     self.logcat_process_adb_full = process
#             #     self.pid_adb_full = self.logcat_process_adb_full.pid
#             #     return self.logcat_process_adb_full
#             self.logcat_process_adb_full = subprocess.Popen(command, shell=True)
#             self.pid_adb_full = self.logcat_process_adb_full.pid
#             #return self.logcat_process_adb_full
#
#
#         except subprocess.CalledProcessError as e:
#             self.logger.error(f"AdbFullLogger [Error]: {e}")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type:
#             self.logger.error(f"An error occurred: {exc_type} {exc_val}", exc_info=True)
#         if self.logcat_process_adb_full:
#             try:
#                 subprocess.call(['adb', 'shell', 'kill', '-s', 'SIGINT', self.pid_adb_full])
#                 self.logcat_process_adb_appium.terminate()
#                 self.logcat_process_adb_appium.wait()
#                 if self.logcat_process_adb_appium:
#                     self.logcat_process_adb_appium.kill_by_pid()
#                     self.logcat_process_adb_appium.wait()
#             except subprocess.CalledProcessError as e:
#                 self.logger.error(f"Error: {e}")
#             self.logcat_process_adb_full = None
#
#
# class AdbAppiumLogger(DataStructureLogger):
#     def __init__(self, filepath: str = None):
#         super().__init__()
#         self.logcat_process_adb_appium = None
#         self.pid_adb_appium = None
#         self.filepath = os.path.join(filepath, 'adb_appium.log')
#
#     def __enter__(self):
#         try:
#             command = f"adb logcat > {self.filepath} appium:i *:s"
#             # with subprocess.Popen(command, shell=True) as process:
#             #     self.logcat_process_adb_appium = process
#             self.logcat_process_adb_appium = subprocess.Popen(command, shell=True)
#             self.pid_adb_appium = self.logcat_process_adb_appium.pid
#             #return self.logcat_process_adb_appium
#         except subprocess.CalledProcessError as e:
#             self.logger.error(f"AdbAppiumLogger [Error]: {e}")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.logcat_process_adb_appium:
#             try:
#                 subprocess.call(['adb', 'shell', 'kill', '-s', 'SIGINT', self.pid_adb_appium])
#                 self.logcat_process_adb_appium.terminate()
#                 self.logcat_process_adb_appium.wait()
#                 if self.logcat_process_adb_appium:
#                     self.logcat_process_adb_appium.kill_by_pid()
#                     self.logcat_process_adb_appium.wait()
#             except subprocess.CalledProcessError as e:
#                 self.logger.error(f"AdbAppiumLogger [Error]: {e}")
#             self.logcat_process_adb_appium = None
#
#
# class ComplexLogger(DataStructureLogger):
#     def __init__(self, logger_name: str = 'UNKNOWN', save_to_file: bool = True, level: str = 'DEBUG'):
#         super().__init__()
#         timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#         folder_path = os.path.join('logs', f'launch_{timestamp}')
#         os.makedirs(folder_path, exist_ok=True)
#         self.filepath = folder_path
#         self.save_to_file = save_to_file
#         self.level = level
#         self.logger_name = logger_name
#         self.autotest = None
#         self.adb_full = None
#         self.adb_appium = None
#         self.loggers_dict = None
#
#     def __enter__(self):
#         self.autotest = AutotestLogger(logger_name=self.logger_name,
#                             save_to_file=self.save_to_file,
#                             level=self.level,
#                             filepath=self.filepath)
#         self.adb_full = AdbFullLogger(filepath=self.filepath)
#         self.adb_appium = AdbAppiumLogger(filepath=self.filepath)
#
#             #return self.loggers_dict
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.autotest = None
#         self.adb_full = None
#         self.adb_appium = None
#
#
# class VideoRecorder:
#     def __enter__(self):
#         timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#         self.filename = f'screenrecord_{timestamp}.mp4'
#         self.command = f"adb shell screenrecord /sdcard/Movies/{self.filename}"
#         self.process = subprocess.Popen(self.command, shell=True)
#         #return self.process
#
#     @staticmethod
#     def delete_video():
#         try:
#             cmd = ['adb', 'shell', 'rm', '-rf', '/sdcard/Movies/*']
#             subprocess.run(cmd, check=True, capture_output=True, text=True)
#             return True
#         except subprocess.CalledProcessError as e:
#             print(f"Error: {e}")
#             return False
#
#     @staticmethod
#     def stop_video():
#         try:
#             subprocess.call(['adb', 'shell', 'pkill', '-l', 'SIGINT', 'screenrecord'])
#             return True
#         except subprocess.CalledProcessError as e:
#             print(f"Error: {e}")
#             return None
#
#     @staticmethod
#     def pull_video():
#         try:
#             path = 'logs'
#             cmd = ['adb', 'pull', '/sdcard/Movies/', f'{path}']
#             # Execute the init subprocess using subprocess.Popen()
#             p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             time.sleep(5)
#             # Wait for the init subprocess to finish using its wait() method
#             p1.wait()
#             cmd = ['adb', 'shell', 'rm', '-rf', '/sdcard/Movies/*']
#             # Execute the second subprocess using subprocess.Popen()
#             p2 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             # Wait for the second subprocess to finish using its wait() method
#             p2.wait()
#             return True
#         except subprocess.CalledProcessError as e:
#             print(f"Error: {e}")
#             return False
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.stop_video()
#         time.sleep(5)
#         self.pull_video()
#         self.process.terminate()
#
#
# class AllureReport:
#     def __init__(self):
#         self.timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#         self.report_dir = os.path.join("allure-results", self.timestamp)
#
#     def __enter__(self):
#         os.makedirs(self.report_dir, exist_ok=True)
#         subprocess.run(["pytest", f"--alluredir={self.report_dir}"])
#         subprocess.run(["allure", "generate", self.report_dir, "-o", f"{self.report_dir}/html"])
#         #return self.report_dir
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         subprocess.run(["alluredir", "serve", {self.report_dir}])
#



# def autotest_logger(logger_name: str = 'UNKNOWN', save_to_file: bool = True):
#     logger = logging.getLogger(logger_name)
#     logger.setLevel(logging.DEBUG)
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     if save_to_file:
#         # timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#         # filename = './logs/autotest_log_{}.log'.format(timestamp)
#         filename = './logs/autotest.log'
#         handler = logging.FileHandler(filename, encoding='utf-8')
#         handler.setFormatter(formatter)
#         logger.addHandler(handler)
#     coloredlogs.install(level='DEBUG', logger=logger)
#     return logger
#
# def remove_handlers(logger):
#     for handler in logger.handlers:
#         logger.removeHandler(handler)


# def adb_appium_logger():
#     # timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#     path = 'logs'
#     # filename = 'adb_appium_log_{}.log'.format(timestamp)
#     if not os.path.exists(os.path.join(path)):
#         os.makedirs(os.path.join(path))
#     filename = 'adb_appium.log'
#     filepath = os.path.join(path, filename)
#     try:
#         command = f"adb logcat > {filepath} appium:i *:s"
#         # logcat_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
#         logcat_process = subprocess.Popen(command, shell=True)
#         return logcat_process
#     except subprocess.CalledProcessError as e:
#         print(f"Error: {e}")
#         return None


# def adb_full_logger():
#     try:
#         timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#         path = 'logs'
#         path2 = 'adb_full'
#         filename = 'adb_full_log_{}.log'.format(timestamp)
#         filepath = os.path.join(path, path2, filename)
#         if not os.path.exists(os.path.join(path, path2)):
#             os.makedirs(os.path.join(path, path2))
#         command = f"adb logcat > {filepath} HWComposer:s"
#         logcat_process = subprocess.Popen(command, shell=True)
#         return logcat_process
#     except subprocess.CalledProcessError as e:
#         print(f"Error: {e}")
#         return None
