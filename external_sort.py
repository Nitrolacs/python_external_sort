import pathlib

from typing import Union, Optional

from data_file import DataFile

PathTypeList = Union[list, pathlib.Path]
PathType = Union[DataFile, pathlib.Path]


def copy_in_file(file: DataFile, output_file: DataFile, last: str):
    output_file.open_file("r")
    count_lines = 0


def write_output_file(src: PathTypeList, output: DataFile, key: str,
                      type_data: str) -> PathType:
    output.clean()

    output.open_file('a')

    last = ''

    for file in src:
        output_file = DataFile(file, key, type_data)
        output, last = copy_in_file(output, output_file, last)

    output.close_file()
    return output


def split_original_file(original_file: DataFile, file1: DataFile,
                        file2: DataFile, reverse: bool):
    pass


def my_sort(src: PathTypeList, output: Optional[str] = None,
            reverse: bool = False,
            key: str = "", type_data: str = 's') -> None:
    if output:
        output = DataFile(output, key, type_data)
        src = write_output_file(src, output, key, type_data)

    original_file = DataFile(src[0], key, type_data)
    file1 = DataFile("file1.txt", key, type_data),
    file2 = DataFile("file2.txt", key, type_data)

    if original_file.lines > 1:
        while not sort_check(original_file, reverse):
            split_original_file(original_file, file1, file2, reverse)


    file1.delete()
    file2.delete()