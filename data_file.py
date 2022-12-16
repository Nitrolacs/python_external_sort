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

        self.data_type = type_data
        self.lines = 0
        self.type_of_file = path_to_file[len(path_to_file) - 3::]
        self.key = ""

        self.open_file = None
        self.dict_reader = None

        self.dict_writer = None

        if self.type_of_file == "csv":
            self.key = key

    def check_or_create_file(self) -> None:
        if not os.path.exists(self.path_to_file):
            with open(self.path_to_file, "x", encoding='utf-8') as _:
                pass

    def open_file(self, mode: str = 'r') -> None:
        if not self.open_file:
            self.close_file()

        self.open_file = open(self.path_to_file, mode, encoding='utf-8')

        if self.type_of_file == "csv":
            if mode == "r":
                self.dict_reader = csv.DictReader(self.open_file)

            elif mode == "a":
                self.open_file = open(self.path_to_file, mode, newline="",
                                      encoding='utf-8')
                self.dict_writer = csv.DictWriter(self.path_to_file,
                                                  fieldnames=[self.key],
                                                  )
                self.dict_writer.writeheader()

            elif mode == 'w':
                self.open_file = open(self.path_to_file, mode, newline='',
                                      encoding='utf-8')

                self.dict_writer = csv.DictWriter(self.path_to_file,
                                                  fieldnames=[self.key])

    def close_file(self) -> None:
        self.open_file.close()
        self.open_file = None
        self.dict_reader = None
        self.dict_writer = None

    def write_file(self, data: str) -> None:
        if self.type_of_file == 'txt':
            self.open_file.write(str(data))
        elif self.type_of_file == 'csv':
            self.dict_writer.writerow()

    def clean(self) -> None:
        self.open_file('w')
        self.write_file('')
        self.close_file()

        self.lines = 0