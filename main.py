import argparse
import os
import external_sort

from typing import Union


def parse_args() -> Union[bool, str]:
    """Обработка параметров командной строки"""
    # Осуществляем разбор аргументов командной строки
    parser = argparse.ArgumentParser(description="Внешняя сортировка")

    parser.add_argument("-f", "--files", nargs="+", dest="files", type=str,
                        help="Исходные файлы")

    parser.add_argument("-o", "--output", dest="output", type=str,
                        help="Выходной файл", required=False, default="")

    parser.add_argument("-r", "--reverse", dest="reverse", action="store_true",
                        help="Порядок сортировки")

    parser.add_argument("-t", "--type_data", dest="type_data", type=str,
                        help="Тип данных (i (int), f (float), s (string)",
                        default="s")

    # В эту переменную попадает результат разбора аргументов командной строки.
    args = parser.parse_args()

    if_args = bool(args.files)

    if not if_args:
        # Если параметры командной строки не переданы
        return "no_args"

    # Проверяем аргументы командной строки

    external_sort.my_sort(args.files, args.output)


def menu() -> None:
    """Меню программы"""
    print("    Меню программы")
    print("1 - Ввод параметров;")
    print("2 - Сортировка;")
    print("3 - Выход из программы.")


def get_file(file_path: str = "") -> Union[str, bool]:
    """
    Получение пути к файлу и проверка его корректности
    :param file_path: Путь к файлу
    :return: путь к файлу или логическую переменную, означающую отсутствие файла.
    """

    if not file_path:
        file_name = input(
            "Введите имя файла (с расширением): ")

    if not os.path.exists(file_path):
        print("Такого файла не существует.")
        return False

    return file_path


def get_files() -> list:
    """
    Получение файлов для внешней сортировки
    :return: Список путей до файлов
    """
    lst_files = []
    file_path_entered = input(
        "Введите путь до файла (нажмите Enter для остановки): ")
    while file_path_entered != "" or not lst_files:
        if file_path_entered != "":
            file = get_file(file_path_entered)
            if file:
                lst_files.append(file)
        file_path_entered = input(
            "Введите путь до файла (нажмите Enter для остановки): ")

    return lst_files


def get_output_file() -> str:
    """
    Получение пути выходного файла
    :return: путь до выходного файла.
    """
    result_path = ""
    output_file_path = input(
        "Введите путь до выходного файла (нажмите Enter для остановки): ")

    while output_file_path != "":
        if output_file_path[len(output_file_path) - 3::] in ["txt", "csv"]:
            result_path = output_file_path
            return result_path
        else:
            print("Недопустимое название файла!")
            output_file_path = input(
                "Введите путь до выходного файла (нажмите "
                "Enter для остановки): ")


def get_key(lst_files) -> str:
    """
    Получение ключа для csv файла
    :param lst_files: пути до файлов
    :return: ключ для csv файла (например, номер/наименование столбца)
    """
    if lst_files[0][len(lst_files[0]) - 3::] == "csv":
        key = input("Введите ключ (наименование столбца): ")
        while not key:
            print("Ключ пустой")
            key = input("Введите ключ (наименование столбца): ")
        return key

    else:
        return ""


def get_reverse() -> bool:
    """
    Получение параметра порядка сортировки
    :return: вариант сортировки
    """

    choice = input("Сортировка должна быть по неубыванию (False) или по "
                   "невозрастанию (True): ")
    while choice not in ["True", "False"]:
        print("Введено неверное значение. Попробуйте снова.")
        choice = input("Сортировка должна быть по неубыванию (False) или по "
                       "невозрастанию (True): ")

    if choice == "True":
        reverse = True
    else:
        reverse = False

    return reverse


def get_type_data() -> str:
    type_data = "s"

    type_list = input("Введите тип данных элементов списка: s (string), "
                      "i (int), f (float) или Enter, чтобы выйти: ")

    while type_list not in ("s", "i", "f", ""):
        print("Введено неверное значение. Попробуйте снова.")
        type_list = input("Введите тип данных элементов списка: s (string), "
                          "i (int), f (float) или Enter, чтобы выйти: ")

    if type_list != "exit":
        type_data = type_list

    return type_data


def main():
    """Точка входа"""

    message = "Введите желаемый номер команды: "
    command_numb = 0

    files = []
    key = ''
    output_file = ''
    type_data = 's'
    reverse = False

    if_parse = parse_args()

    while command_numb != "3" and if_parse == "no_args":
        menu()  # Вызов меню
        command_numb = input(message)

        if command_numb == "1":
            files = get_files()
            output_file = get_output_file()
            key = get_key(files)
            reverse = get_reverse()
            type_data = get_type_data()

        elif command_numb == "2":
            print("Внешняя сортировка начата...")
            external_sort.my_sort(files, output_file, reverse, key, type_data)

            print("Внешняя сортировка закончена")

        elif command_numb == "3":
            print("Завершение программы...")

        else:
            print("Введено неверное значение, попробуйте снова.")


if __name__ == "__main__":
    main()
