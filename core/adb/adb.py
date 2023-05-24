import logging
import os
import re
import subprocess
import time
from datetime import datetime
from typing import List
import config

logger = logging.getLogger(config.LOGGER_NAME)


def run_cmd(command: List[str]) -> str:
    result = subprocess.run(command, stdout=subprocess.PIPE, check=True).stdout.decode("utf-8").strip()
    return result


def get_device_uuid() -> str:
    """
    Get the UUID of the connected Android device using the adb command.
    :return: The UUID as a string.
    """
    output = subprocess.check_output(['adb', 'devices']).decode('utf-8')
    device_list = re.findall(r'(\d+\.\d+\.\d+\.\d+:\d+|\d+)', output)

    return device_list[0]


def get_device_model() -> str:
    """
    Get the model of the connected Android device using the adb command.
    :return: The model as a string.
    """
    command = ["adb", "shell", "getprop", "ro.product.model"]
    model = run_cmd(command)
    return model


def get_package_name(path_to_apk: str) -> str:
    aapt = config.AAPT_PATH
    output = subprocess.run([aapt, "dump", "badging", path_to_apk], capture_output=True, text=True, check=True)
    package_line = [line for line in output.stdout.splitlines() if line.startswith("package: name")][0]
    package_name = package_line.split("'")[1]

    return package_name


def get_launchable_activity_from_apk(path_to_apk: str) -> str:
    aapt = config.AAPT_PATH

    output = subprocess.run([aapt, "dump", "badging", path_to_apk], capture_output=True, text=True, check=True)
    package_line = [line for line in output.stdout.splitlines() if line.startswith("launchable-activity")][0]
    launchable_activity = package_line.split("'")[1]

    return launchable_activity


def push(source: str, destination: str) -> bool:
    """
    Push a file or directory to the connected device.

    Args:
        source (str): The path to the file or directory to push.
        destination (str): The destination path on the device.

    Returns:
        bool: True if the file or directory was pushed successfully, False otherwise.
    """
    try:
        subprocess.run(["adb", "push", source, destination], check=True, capture_output=True, text=True)
        logging.info(f"{source} was successfully pushed to {destination}.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to push {source} to {destination}: {e.stderr}")
        return False


def pull(source: str, destination: str) -> bool:
    try:
        subprocess.run(["adb", "pull", source, destination], check=True, capture_output=True, text=True)
        logging.info(f"from {source} was successfully pulled to {destination}.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to push {source} to {destination}: {e.stderr}")
        return False


def install(source: str) -> bool:
    """
    Install an APK file on the connected device.

    Args:
        source (str): The path to the APK file to install.

    Returns:
        bool: True if the APK file was installed successfully, False otherwise.
    """
    try:
        subprocess.run(["adb", "install", "-r", source], check=True, capture_output=True, text=True)
        logging.info(f"{source} was successfully installed.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while trying to install {source}: {e.stderr}")
        return False


def start_activity(package, activity):
    try:
        os.system(f'adb shell am start -n {package}/{activity}')
        return True
    except Exception as e:
        logging.error('Unexpected error: {}'.format(e))


def close_app(package):
    time.sleep(3)
    """Force stops the specified package using ADB.

    Args:
        package (str): The package name of the app to close.

    Returns:
        bool: True if the app was closed successfully, False otherwise.
    """
    cmd = ['adb', 'shell', 'am', 'force-stop', package]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        logging.error(f"{package} was successfully closed.")
        time.sleep(3)
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while trying to force stop {package}: {e.stderr}")
        time.sleep(3)
        return False
    except FileNotFoundError:
        logging.error("ADB not found. Please make sure it's installed and added to your PATH environment variable.")
        time.sleep(3)
        return False


def reboot_app(package, activity):
    assert close_app(package=package)
    assert start_activity(package=package, activity=activity)
    return True


def uninstall_app(package):
    """Uninstalls the specified package using ADB.

    Args:
        package (str): The package name of the app to uninstall.

    Returns:
        bool: True if the app was uninstalled successfully, False otherwise.
    """
    cmd = ['adb', 'uninstall', package]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        logging.info(f"{package} was successfully uninstalled.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while trying to uninstall {package}: {e.stderr}")
        return False
    except FileNotFoundError:
        logging.error("ADB not found. Please make sure it's installed and added to your PATH environment variable.")
        return False


def press_home():
    """Sends a Home button press event to the device using ADB.

    Returns:
        bool: True if the command was executed successfully, False otherwise.
    """
    cmd = ['adb', 'shell', 'input', 'keyevent', 'KEYCODE_HOME']
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        logging.info("Home button press event sent.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while trying to send a Home button press event: {e.stderr}")
        return False
    except FileNotFoundError:
        logging.error("ADB not found. Please make sure it's installed and added to your PATH environment variable.")
        return False


def press_back():
    """Sends a Back button press event to the device using ADB.

    Returns:
        bool: True if the command was executed successfully, False otherwise.
    """
    cmd = ['adb', 'shell', 'input', 'keyevent', 'KEYCODE_BACK']
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        logging.info("Back button press event sent.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while trying to send a Back button press event: {e.stderr}")
        return False
    except FileNotFoundError:
        logging.error("ADB not found. Please make sure it's installed and added to your PATH environment variable.")
        return False


def press_menu():
    """Sends a Menu button press event to the device using ADB.

    Returns:
        bool: True if the command was executed successfully, False otherwise.
    """
    cmd = ['adb', 'shell', 'input', 'keyevent', 'KEYCODE_MENU']
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        logging.info("Menu button press event sent.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while trying to send a Menu button press event: {e.stderr}")
        return False
    except FileNotFoundError:
        logging.error("ADB not found. Please make sure it's installed and added to your PATH environment variable.")
        return False


def input_keycode_num_(num: int) -> bool:
    print("def input_keycode_num_(num:int) -> bool:")
    """Sends a Back button press event to the device using ADB.
    required: 0-9, ADD, COMMA, DIVIDE, DOT, ENTER, EQUALS
    Returns:
        bool: True if the command was executed successfully, False otherwise.
    """
    cmd = ['adb', 'shell', 'input', 'keyevent', f'KEYCODE_NUMPAD_{num}']
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        logging.info("Event sent.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while trying to send a Back button press event: {e.stderr}")
        return False
    except FileNotFoundError:
        logging.error("ADB not found. Please make sure it's installed and added to your PATH environment variable.")
        return False

def input_keycode(keycode:str) -> bool:
    """
    Вводит указанный кейкод
    """
    cmd = ['adb', 'shell', 'input', 'keyevent', f'{keycode}']
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        logging.info("Event sent.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while trying to send a Back button press event: {e.stderr}")
        return False
    except FileNotFoundError:
        logging.error("ADB not found. Please make sure it's installed and added to your PATH environment variable.")
        return False

def input_by_virtual_keyboard(key: str, keyboard: dict):
    try:
        for char in key:
            tap(*keyboard[char])
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while input_by_virtual_keyboard: {e.stderr}")
        return False

def input_text(text: str):
    try:
        adb_command = f"adb shell input text {text}"
        response = subprocess.run(adb_command, shell=True, check=True)
        if 'Error' in response:
            logging.error(f"input_text(): {response.stderr}")
            return False
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"input_text(): {e.stderr}")
        return False

def tap(x, y):
    try:
        adb_command = f"adb shell input tap {x} {y}"
        subprocess.run(adb_command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while trying to send a Menu button press event: {e.stderr}")
        return False


def swipe(start_x, start_y, end_x, end_y, duration: int = 300):
    cmd = ['adb', 'shell', 'input', 'swipe', str(start_x), str(start_y), str(end_x), str(end_y), str(duration)]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        logging.info(f"Swipe by direction start_x: {start_x}, start_y: {start_y}, end_x: {end_x}, end_y: {end_y}, "
                     f"duration: {duration}, event sent.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while trying to send a Menu button press event: {e.stderr}")
        return False
    except FileNotFoundError:
        logging.error("ADB not found. Please make sure it's installed and added to your PATH environment variable.")
        return False


def get_current_app_package():
    time.sleep(3)
    try:
        # Define the command as a list of strings
        command = ["adb", "shell", "dumpsys", "window", "windows", "|", "grep", "-E", "'mCurrentFocus|mFocusedApp'",
                   "|", "grep", "-e", "'mFo'"]

        # Run the command and get the output as a byte string
        output = subprocess.check_output(command)

        # Convert the byte string to a regular string
        output_str = output.decode("utf-8")

        print("get_current_app_package() output: ", output_str)

        # Find the position of the last occurrence of the "/." substring in the string
        end_index = output_str.rfind("/")

        # Extract the app name from the preceding characters
        start_index = output_str.rfind(" ", 0, end_index) + 1
        app_name = output_str[start_index:end_index]

        return app_name

    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        logging.error(f"Error occurred: {e}")
        return False


def check_VPN():
    logger.debug("check_VPN()")
    command = "adb shell \"netstat | grep -w -e '213.232.199.14'\""
    try:
        output = subprocess.check_output(command, shell=True, timeout=10).decode()
        logger.debug("check_VPN() output: %s", output)
        if "ESTABLISHED" in output:
            logger.debug("check_VPN() True")
            return True
        else:
            logger.debug("check_VPN() False")
            return False
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        logger.debug("check_VPN() False")
        return False


def stop_logcat():
    try:
        # get a list of running logcat processes
        process_list = subprocess.check_output(['adb', 'shell', 'ps', '|', 'grep', 'logcat'], shell=True).decode()
        # loop through the list of processes and send SIGINT signal to each one
        for process in process_list.splitlines():
            pid = process.split()[1]
            subprocess.call(['adb', 'shell', 'kill', '-s', 'SIGINT', pid])
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None


def reload_adb():
    try:
        cmd = ['adb', 'kill-server']
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    time.sleep(3)
    try:
        cmd = ['adb', 'start-server']
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    # TODO RECONNECT TO DEVICE
    return True


def kill_by_pid(pid: str):
    try:
        subprocess.call(['adb', 'shell', 'kill', '-s', 'SIGINT', str(pid)])
    except subprocess.CalledProcessError as e:
        logger.error(f"Error: {e}")


def kill_all(name: str):
    try:
        subprocess.call(['adb', 'shell', 'pkill', '-f', str(name)])
    except subprocess.CalledProcessError as e:
        logger.error(f"Error: {e}")


def kill_by_name(name: str):
    try:
        subprocess.call(['adb', 'shell', 'pkill', '-l', 'SIGINT', str(name)])
    except subprocess.CalledProcessError as e:
        logger.error(f"Error: {e}")


def delete_files_from_internal_storage(path):
    try:
        cmd = ['adb', 'shell', 'rm', '-rf', f'{path}*']
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False


def pull_video(path):
    try:
        cmd = ['adb', 'pull', '/sdcard/Movies/', f'{path}']
        # Execute the init subprocess using subprocess.Popen()
        p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(5)
        # Wait for the init subprocess to finish using its wait() method
        p1.wait()
        cmd = ['adb', 'shell', 'rm', '-rf', '/sdcard/Movies/*']
        # Execute the second subprocess using subprocess.Popen()
        p2 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Wait for the second subprocess to finish using its wait() method
        p2.wait()
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False


def stop_video():
    try:
        subprocess.call(['adb', 'shell', 'pkill', '-l', 'SIGINT', 'screenrecord'])
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None


def record_video(filename):
    try:
        command = f"adb shell screenrecord /sdcard/Movies/{filename}"
        record_process = subprocess.Popen(command, shell=True)
        return record_process
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

def reboot():
    command = f"adb shell reboot"
    subprocess.call(command)
    return True


# def record_video(folder_path: str = '/sdcard/Movies/'):
#     try:
#         filepath = os.path.join(folder_path, f'screenrecord_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.mp4')
#         command = f"adb shell screenrecord {filepath}"
#         screenrecord_process = subprocess.Popen(command, shell=True)
#         return screenrecord_process
#
#     except subprocess.CalledProcessError as e:
#         logger.error(f"[Error]: {e}")

# def record_video():
#     try:
#         timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#         filename = 'screenrecord_{}.mp4'.format(timestamp)
#         command = f"adb shell screenrecord /sdcard/Movies/{filename}"
#         record_process = subprocess.Popen(command, shell=True)
#         return record_process
#     except subprocess.CalledProcessError as e:
#         print(f"Error: {e}")
#         return None
