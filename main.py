import argparse
import os

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

    """
    sorted_array = sort_visualization(array, args.reverse, args.gif,
                                      args.visualize)
    """


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
            "Введите имя файла (с расширением), откуда нужно считать строку: ")

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


def main():
    """Точка входа"""

    message = "Введите желаемый номер команды: "
    command_numb = 0

    files = []
    key = ''
    output_file = ''
    reverse = False

    if_parse = parse_args()

    while command_numb != "3" and if_parse == "no_args":
        menu()  # Вызов меню
        command_numb = input(message)

        if command_numb == "1":
            files = get_files()

        elif command_numb == "2":
            pass

        elif command_numb == "3":
            print("Завершение программы...")

        else:
            print("Введено неверное значение, попробуйте снова.")


if __name__ == "__main__":
    main()
