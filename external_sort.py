import pathlib

from typing import Union, Optional

from data_file import DataFile

PathTypeList = Union[list, pathlib.Path]
PathType = Union[DataFile, pathlib.Path]


def copy_in_file(file: DataFile, output_file: DataFile, last: str):
    output_file.open_file("r")
    count_lines = 0


def sort_check(main_file: DataFile, reverse: bool) -> bool:
    """Функция проверки отсортированности файла"""
    sort = True
    main_file.open_file('r')
    count_str1, count_str2 = 0, 0
    str1, str2 = '', ''
    while not valid_item(str(str1), main_file.type_data):
        str1 = main_file.read_file()
    count_str1 += 1

    while not valid_item(str(str2), main_file.type_data):
        str2 = main_file.read_file()

    while (count_str1 + count_str2) < main_file.lines:
        if (
                compare(str1, str2, main_file.type_data) not in
                ((1 if reverse else -1), 0)
        ):
            sort = False
            break

        count_str2 += 1
        str1 = str2
        str2 = main_file.read_file()
        while not valid_item(str(str2), main_file.type_data):
            str2 = main_file.read_file()
            if (count_str1 + count_str2) == main_file.lines:
                break
    main_file.close_file()
    return sort


def write_output_file(src: PathTypeList, output: DataFile, key: str,
                      type_data: str) -> PathType:
    output.clean()

    output.open_file('a')

    last = ''

    for file in src:
        output_file = DataFile(file, key, type_data)
        # output, last = copy_in_file(output, output_file, last)

    output.close_file()
    return output


def file_len(fname):
    i = -1
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def copy_to_another_and_split(from_this, to_this):
    """
    delete all comas and rewrite it to a new file
    """
    copy_from = open(from_this, "r")
    copy_to = open(to_this, "w")
    copy_to.truncate()
    data = copy_from.read().split(',')
    for i in range(len(data)):
        copy_to.write(data[i] + '\n')
    copy_from.close()
    copy_to.close()


def read_int(file):
    """
    reads an str from file and convert it to number
    """
    num_str = file.readline()
    if num_str != "`\n" and num_str != '':
        num = int(num_str.replace("\n", ""))
        return num
    return None


def swap_active_files(active_file):
    """
    function to swap file with to write
    """
    if active_file == "f1":
        active_file = "f2"
    else:
        active_file = "f1"
    return active_file


def write_to_active_file(active_file, num, f1, f2):
    """
    Writes to active file
    """
    if active_file == "f1":
        f1.write(str(num) + "\n")
    else:
        f2.write(str(num) + "\n")


def write_to_main_file(f, num):
    """
    writing to main exit file
    """
    f.write(str(num) + "\n")


def end_of_range(num):
    if num is None:
        return True
    else:
        return False


def valid_item(item: str, type_data: str) -> bool:
    """Функция проверки считанного значения"""
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
    """Функция сравнения"""
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


def split_original_file(original_file: DataFile, file1: DataFile,
                        file2: DataFile, reverse: bool):
    counter_splits = 0
    counter_merges = 0
    counter_more_or_less_split = 0

    str1, str2 = '', ''

    original_file.open_file('r')
    file1.clean()
    file1.open_file('a')
    file2.clean()
    file2.open_file('a')

    while True:
        active_file = file1

        str1 = original_file.read_file()

        file1.write_file(str1)
        # write_to_active_file(active_file, num, file1, file2)
        str2 = str1
        while str1 is not None:

            str1 = original_file.read_file()

            if len(str1) == 0:
                break

            counter_more_or_less_split += 1

            compare_result = compare(str2, str1, original_file.type_data)

            str1 = str1 + "\n" if "\n" not in str1 else str1

            if reverse:
                if compare_result in [1, 0]:
                    file1.write_file(str1)
                elif compare_result == -1:
                    file2.write_file(str1)
            else:
                if compare_result in [-1, 0]:
                    active_file.write_file(str1)
                elif compare_result == 1:
                    active_file = file2 if active_file == file1 else file1
                    active_file.write_file(str1)

            str2 = str1

        if file2.lines == 0:
            break

        counter_splits += 1


        f1.close()
        f2.close()
        original_file.close()
        
        
        #merging
        with open(f_name, "w") as original_file, open(f1_name, "r") as f1, open(f2_name,
                                                                    "r") as f2:
            num_f1 = read_int(f1)
            num_f2 = read_int(f2)

            while num_f1 is not None and num_f2 is not None:
                run_f1 = False
                run_f2 = False
                while run_f1 is False and run_f2 is False:
                    if num_f1 <= num_f2:
                        write_to_main_file(original_file, num_f1)
                        num_f1 = read_int(f1)
                        run_f1 = end_of_range(num_f1)

                    else:
                        write_to_main_file(original_file, num_f2)
                        num_f2 = read_int(f2)
                        run_f2 = end_of_range(num_f2)
                    counter_more_or_less_split += 1
                while run_f1 is False:
                    write_to_main_file(original_file, num_f1)
                    num_f1 = read_int(f1)
                    run_f1 = end_of_range(num_f1)

                while run_f2 is False:
                    write_to_main_file(original_file, num_f2)
                    num_f2 = read_int(f2)
                    run_f2 = end_of_range(num_f2)

            run_f1 = False
            run_f2 = False
            while num_f1 is not None and run_f1 is False:
                write_to_main_file(original_file, num_f1)
                num_f1 = read_int(f1)

            while num_f2 is not None and run_f2 is False:
                write_to_main_file(original_file, num_f2)
                num_f2 = read_int(f2)

        counter_merges += 1
        original_file.close()
        f1.close()
        f2.close()
        """


def my_sort(src: PathTypeList, output: Optional[str] = None,
            reverse: bool = False,
            key: str = "", type_data: str = 's') -> None:
    """
    if output:
        output = DataFile(output, key, type_data)
        src = write_output_file(src, output, key, type_data)
    """

    original_file = DataFile(src[0], key, type_data)
    file1 = DataFile("file1.txt", key, type_data)
    file2 = DataFile("file2.txt", key, type_data)
    split_original_file(original_file, file1, file2, reverse)
    """
    if original_file.lines > 1:
        while not sort_check(original_file, reverse):
            split_original_file(original_file, file1, file2, reverse)

    file1.delete()
    file2.delete()
    """