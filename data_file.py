"""Реализация класса файла"""
import csv
import os.path


class DataFile:
    """
    Класс для работы с csv и txt файлами
    """

    def __init__(self, path_to_file: str, key: str, type_data: str) -> None:
        self.path_to_file = path_to_file

        self.check_or_create_file()

        self.type_data = type_data
        self.lines = 0
        self.type_of_file = path_to_file[len(path_to_file) - 3::]
        self.key = ""

        self.file = None
        self.dict_reader = None

        self.dict_writer = None

        if self.type_of_file == "csv":
            self.key = key

        self.calculate_count_lines()

    def calculate_count_lines(self) -> None:
        if not self.file:
            self.open_file('r')

        if self.type_of_file == "txt":
            for _ in self.file:
                self.lines += 1

        elif self.type_of_file == "csv":
            for _ in self.dict_reader:
                self.lines += 1

        self.close_file()

    def check_or_create_file(self) -> None:
        if not os.path.exists(self.path_to_file):
            with open(self.path_to_file, "x", encoding='utf-8') as _:
                pass

    def open_file(self, mode: str = 'r') -> None:
        if not self.file:
            self.close_file()

        self.file = open(self.path_to_file, mode, encoding='utf-8')

        if self.type_of_file == "csv":
            if mode == "r":
                self.dict_reader = csv.DictReader(self.file)

            elif mode == "a":
                self.file = open(self.path_to_file, mode, newline="",
                                 encoding='utf-8')
                self.dict_writer = csv.DictWriter(self.path_to_file,
                                                  fieldnames=[self.key],
                                                  )
                self.dict_writer.writeheader()

            elif mode == 'w':
                self.file = open(self.path_to_file, mode, newline='',
                                 encoding='utf-8')

                self.dict_writer = csv.DictWriter(self.path_to_file,
                                                  fieldnames=[self.key])

    def read_file(self) -> str:
        if self.file is None:
            self.open_file('r')

        if self.type_of_file == "txt":
            try:
                return self.file.readline()
            except StopIteration:
                return ''

        if self.type_of_file == "csv":
            try:
                return next(self.dict_reader)[self.key]
            except StopIteration:
                return ''

    def close_file(self) -> None:
        if self.file is not None:
            self.file.close()
            self.file = None
            self.dict_reader = None
            self.dict_writer = None

    def write_file(self, data: str) -> None:
        if self.type_of_file == 'txt':
            self.file.write(str(data))
        elif self.type_of_file == 'csv':
            self.dict_writer.writerow()

    def clean(self) -> None:
        self.open_file('w')
        self.write_file('')
        self.close_file()

        self.lines = 0

    def delete(self) -> None:
        self.close_file()
        os.remove(self.path_to_file)
        self.path_to_file = None
