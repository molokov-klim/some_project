import json
import logging
import math
import os

from core.dto import dto
from core.ofd import ofd_taxcom

START_DIR = os.getcwd()
PROJECT_ROOT_DIR = os.path.dirname(__file__)
logger = logging.getLogger('autotest')


def save_to_files_all_fd_from_taxcom():
    last_fd = dto.get_last_fd_number()
    fd_fn = dto.get_fd_from_fn(
        fd=last_fd)
    fn_number = dto.get_fn_number_from_fd_json(fd_fn)
    folder_path = os.path.join(PROJECT_ROOT_DIR, 'test_data', 'raw')
    count = 0
    while count < last_fd:
        try:
            fd_ofd = ofd_taxcom.get_fd_from_taxcom(fn_number=fn_number, fd=last_fd)
            print(fd_ofd)
            count += 1
            print("COUNT: ", count)
            os.makedirs(folder_path, exist_ok=True)
            filepath = os.path.join(folder_path, f'{count}.json')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(fd_ofd))
            print("OK")
        except Exception as e:
            print("ERROR: {}".format(e))


def save_to_files_all_fd_from_fn():
    last_fd = dto.get_last_fd_number()
    fd_fn = dto.get_fd_from_fn(
        fd=last_fd)
    folder_path = os.path.join(PROJECT_ROOT_DIR, 'test_data', 'raw')
    count = 0
    while count < last_fd:
        try:
            count += 1
            fd_fn = dto.get_fd_from_fn(count)
            print(fd_fn)
            print("COUNT: ", count)
            os.makedirs(folder_path, exist_ok=True)
            filepath = os.path.join(folder_path, f'{count}.json')
            print(filepath)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(fd_fn))
            print("OK")
        except Exception as e:
            print("ERROR: {}".format(e))


def write_to_json(path, filename, data):
    try:
        filepath = os.path.join(START_DIR, path, filename)
        with open(filepath, 'x', encoding='utf-8') as f:
            json.dump(data, f)
        return True
    except:
        return False


def remove_keys_from_json_files_recursively(keys: list, path: str):
    """
    Метод рекурсивно проходит по всем вложенным папкам в поисках .json файлов.
    В каждом файле удаляет ключи и значения заданные в параметрах.
    Например:
    keys_to_remove = ["1038",
                      "1040",
                      "1042",
                      "qr",
                      "1021",
                      "1012",
                      "1042",
                      "1077",
                      ]
    path = os.path.join('test_data', 'FFD_1_05', 'cash')
    operations.change_values_in_json_files_recursively(keys=keys_to_remove, path=path)
    """
    # Define the directory to traverse
    root_dir = os.path.join(START_DIR, path)

    # Traverse the directory tree and modify JSON files
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            # Check if the file is a JSON file
            if file.endswith('.json'):
                # Load the JSON data from the file
                file_path = os.path.join(subdir, file)
                print("file_path: ", file_path)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Delete the text-value pair from the JSON data
                for key in keys:
                    if key in data:
                        del data[key]

                # Write the modified JSON data back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f)


def change_values_in_json_files_recursively(keys: dict, path: str):
    """
    Метод рекурсивно проходит по всем вложенным папкам в поисках .json файлов.
    В каждом файле меняет значения у ключей заданных в параметрах.
    Например:
    keys = {
    "1031": 0,
    "1081": 1,
    }
    path = os.path.join('test_data', 'FFD_1_05', 'card')
    operations.change_values_in_json_files_recursively(keys=keys, path=path)
    """
    print("change_values_in_json_files_recursively()")
    print("keys: ", keys)
    print("path: ", path)
    # Define the directory to traverse
    root_dir = os.path.join(START_DIR, path)

    # Traverse the directory tree and modify JSON files
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            # Check if the file is a JSON file
            if file.endswith('.json'):
                # Load the JSON data from the file
                file_path = os.path.join(subdir, file)
                print("file_path: ", file_path)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Delete the text-value pair from the JSON data
                for key in keys:
                    if key in data:
                        print("data[text]: ", data[key])
                        print("keys[text]: ", keys[key])
                        data[key] = keys[key]

                # Write the modified JSON data back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f)


def change_values_in_dict(dict_needs_to_change: dict, changes: dict) -> dict:
    """
    Метод изменяет поданный словарь, согласно поданным параметрам (поиск с заменой).
    Если значение None, то удаляет ключ.
    Возвращает измененный словарь.
    """
    logger.debug("change_values_in_dict()")
    # Delete the text-value pair from the JSON data
    count = 0
    for key in changes:
        if key in dict_needs_to_change:
            if changes[key] is None:
                dict_needs_to_change.pop(key)
            else:
                dict_needs_to_change[key] = changes[key]
            count += 1
    if count > 0:
        logger.debug("change_values_in_dict(): Словарь подготовлен")
        return dict_needs_to_change
    else:
        logger.debug("change_values_in_dict(): В словаре нечего менять")


def find_coordinates_by_vector(width, height,  direction: int, distance: int, start_x: int, start_y: int):
    """
    fill me
    """

    # Расчет конечной точки на основе направления и расстояния
    angle_radians = direction * (math.pi / 180)  # Преобразование направления в радианы
    dy = abs(distance * math.cos(angle_radians))
    dx = abs(distance * math.sin(angle_radians))

    if 0 <= direction <= 180:
        x = start_x + dx
    else:
        x = start_x - dx

    if 0 <= direction <= 90 or 270 <= direction <= 360:
        y = start_y - dy
    else:
        y = start_y + dy

    # Обрезка конечной точки до границ экрана
    x2 = (max(0, min(x, width)))
    y2 = (max(0, min(y, height)))

    return x2, y2
