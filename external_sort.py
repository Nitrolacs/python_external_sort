"""Модуль внешней естественной сортировки"""

import pathlib
import os

from typing import Union, Optional

from data_file import DataFile

PathTypeList = Union[list, pathlib.Path]
PathType = Union[DataFile, pathlib.Path]


def end_of_range(value):
    """
    Проверка конца серии
    :param value: символ
    :return: конец ли это серии
    """
    if value == "`\n" or value == '':
        return True
    else:
        return False


def valid_item(item: str, type_data: str) -> bool:
    """
    Функция проверки считанного значения
    :param item: значение
    :param type_data: тип значения
    :return: результат проверки
    """
    value = None
    if type_data == 'i':
        value = (
            item.replace('-', '').replace('.', '').replace('\n', '').isdigit()
        )
    elif type_data == 's':
        value = False if item in ("", "'\n", "\'", "\'\n") else True
    elif type_data == 'f':
        value = (
            item.replace('-', '').replace('.', '').replace('\n', '').isdigit()
        )
    return value


def compare(first: str, second: str, type_data: str) -> int:
    """
    Функция сравнения двух считанных значений
    :param first: первое значение
    :param second: второе значение
    :param type_data: тип значения
    :return: результат сравнения
    """
    value = 0
    if type_data == 'i':
        if int(first) < int(second):
            value = -1
        elif int(first) > int(second):
            value = 1
        else:
            value = 0
    elif type_data == 's':
        if str(first) < str(second):
            value = -1
        elif str(first) > str(second):
            value = 1
        else:
            value = 0
    elif type_data == 'f':
        if float(first) < float(second):
            value = -1
        elif float(first) > float(second):
            value = 1
        else:
            value = 0

    return value


def splitting_file(output_file: DataFile, file1: DataFile,
                   file2: DataFile, reverse: bool) -> None:
    """
    Разбиение файла
    :param output_file: Исходный файл
    :param file1: файл 1
    :param file2: файл 2
    :param reverse: флаг сортировки
    :return: None
    """

    output_file.open_file('r')
    file1.clean()
    file1.open_file('a')
    file2.clean()
    file2.open_file('a')

    active_file = file1
    str1 = output_file.read_file()

    str1 = str1 + "\n" if "\n" not in str1 else str1

    number_of_sequences = 1

    file1.write_file(str1)

    str2 = str1
    while str1 is not None:

        str1 = output_file.read_file()

        if len(str1) == 0:
            break

        compare_result = compare(str2, str1, output_file.type_data)

        str1 = str1 + "\n" if "\n" not in str1 else str1

        if reverse:
            if compare_result in [1, 0]:
                active_file.write_file(str1)
            elif compare_result == -1:
                number_of_sequences += 1
                active_file = file2 if active_file == file1 else file1
                if number_of_sequences > 2:
                    active_file.write_file("`\n")
                active_file.write_file(str1)

        else:
            if compare_result in [-1, 0]:
                active_file.write_file(str1)
            elif compare_result == 1:
                number_of_sequences += 1
                active_file = file2 if active_file == file1 else file1
                if number_of_sequences > 2:
                    active_file.write_file("`\n")
                active_file.write_file(str1)

        str2 = str1

    file1.close_file()
    file2.close_file()
    output_file.close_file()


def combine_files(src: PathTypeList, output: Optional[str] = None,
                  type_data: str = "s") -> str:
    """
    Соединение файлов
    :param src: исходные файлы
    :param output: файл для вывода
    :param type_data: тип значения в исходном файле
    :return: путь к файлу для вывода
    """

    common_file = DataFile(output, "", type_data)

    common_file.open_file('w')

    for index in range(len(src)):
        tmp_file = DataFile(src[index], "", type_data)
        tmp_file.open_file("r")
        for _ in range(tmp_file.lines):
            str1 = tmp_file.read_file()
            str1 = str1 + "\n" if "\n" not in str1 else str1
            common_file.write_file(str1)
        tmp_file.close_file()

    common_file.close_file()

    return common_file.path_to_file


def merging_files(output_file: DataFile, file1: DataFile,
                  file2: DataFile, reverse: bool, is_output: bool) -> None:
    """
    Слияние файлов
    :param output_file: исходный файл
    :param file1: файл1
    :param file2: файл2
    :param reverse: флаг сортировки
    :param is_output: есть ли выходной файл
    :return: None
    """

    if output_file.type_of_file == "csv" and not is_output:
        backup_file = DataFile(output_file.path_to_file[:-4] + "_backup." +
                               output_file.type_of_file,
                               "w", output_file.type_data)

        output_file.open_file("r")

        keys = dict(list(output_file.reader)[0])

        backup_file.open_file("w", list(keys))

        output_file.close_file()
        output_file.open_file("r")

        for row in output_file.reader:
            row[output_file.key] = ''
            backup_file.writer.writerow(row)

        output_file.close_file()
        backup_file.close_file()

        backup_file.open_file("r")
        output_file.open_file('w', list(keys))

        for row in backup_file.reader:
            output_file.writer.writerow(row)

        backup_file.delete()

    else:
        output_file.open_file('w')

    file1.open_file('r')
    file2.open_file('r')

    # merging

    str1 = file1.read_file()
    str2 = file2.read_file()

    if reverse:
        values_list = [1, 0]
    else:
        values_list = [-1, 0]

    while str1 != '' and str2 != '':

        run_f1 = False
        run_f2 = False

        while run_f1 is False and run_f2 is False:

            compare_result = compare(str1, str2, output_file.type_data)

            if compare_result in values_list:
                output_file.write_file(str1)
                str1 = file1.read_file()
                run_f1 = end_of_range(str1)

            else:
                output_file.write_file(str2)
                str2 = file2.read_file()
                run_f2 = end_of_range(str2)

        while run_f1 is False:
            output_file.write_file(str1)
            str1 = file1.read_file()
            run_f1 = end_of_range(str1)

        while run_f2 is False:
            output_file.write_file(str2)
            str2 = file2.read_file()
            run_f2 = end_of_range(str2)

        str1 = file1.read_file()
        str2 = file2.read_file()

    while str1 != "":
        output_file.write_file(str1)
        str1 = file1.read_file()

    while str2 != "":
        output_file.write_file(str2)
        str2 = file2.read_file()

    file1.close_file()
    file2.close_file()
    output_file.close_file()


def my_sort(src: PathTypeList, output: Optional[str] = None,
            reverse: bool = False,
            key: str = "", type_data: str = 's') -> None:
    """
    Основная функция
    :param src: Пути к исходным файлам
    :param output: Путь для выходного файла
    :param reverse: Флаг сортировки
    :param key: ключ (для csv файлов)
    :param type_data: тип значений
    :return: None
    """
    output_file = None

    if output:
        output_file = DataFile(output, key, type_data)

    if output and len(src) != 1:
        src = [combine_files(src, output, type_data)]
        output = ""

    for index in range(len(src)):
        original_file = DataFile(src[index], key, type_data)
        file1 = DataFile("file1.txt", key, type_data)
        file2 = DataFile("file2.txt", key, type_data)

        if not output:
            output_file = original_file

        index = 0

        if original_file.lines > 1:
            while True:
                index += 1

                if index == 1:
                    splitting_file(original_file, file1, file2, reverse)
                else:
                    splitting_file(output_file, file1, file2, reverse)

                if os.stat(file2.path_to_file).st_size == 0:
                    break

                merging_files(output_file, file1, file2, reverse, bool(output))

        file1.delete()
        file2.delete()
