import pathlib

from typing import Union, Optional, Callable

from data_file import DataFile

PathTypeList = Union[list, pathlib.Path]
PathType = Union[DataFile, pathlib.Path]


def write_output_file(src: PathTypeList, output: DataFile, key: str,
                      type_data: str) -> PathType:
    output.clean()


def my_sort(src: PathTypeList, output: Optional[str] = None,
            reverse: bool = False,
            key: str = "", type_data: str = 's') -> None:
    if output:
        output = DataFile(output, key, type_data)
        src = write_output_file(src, output, key, type_data)

    original_file = DataFile(src, key, type_data)
    file1 = DataFile("file1.txt", key, type_data),
    file2 = DataFile("file2.txt", key, type_data)
