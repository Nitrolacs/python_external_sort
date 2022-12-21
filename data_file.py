"""Реализация класса файла"""
import csv
import os.path
from typing import Union


class DataFile:
    """
    Класс для работы с csv и txt файлами
    """

    def __init__(self, path_to_file: str, key: str, type_data: str) -> None:
        """
        Инициализация
        :param path_to_file: Путь к файлу
        :param key: ключ (для csv)
        :param type_data: тип значений
        """
        self.path_to_file = path_to_file

        self.check_or_create_file()

        self.type_data = type_data
        self.lines = 0
        self.type_of_file = path_to_file[len(path_to_file) - 3::]
        self.key = ""

        self.file = None
        self.reader = None
        self.writer = None

        if self.type_of_file == "csv":
            self.key = key

        self.calculate_count_lines()

    def calculate_count_lines(self) -> None:
        """
        Подсчет количества строк
        :return: None
        """
        if not self.file:
            self.open_file('r')

        if self.type_of_file == "txt":
            for _ in self.file:
                self.lines += 1

        elif self.type_of_file == "csv":
            for _ in self.reader:
                self.lines += 1

        self.close_file()

    def check_or_create_file(self) -> None:
        """
        Проверка существования файла
        :return: None
        """
        if not os.path.exists(self.path_to_file):
            with open(self.path_to_file, "x", encoding='utf-8') as _:
                pass

    def open_file(self, mode: str = 'r') -> None:
        """
        Открытие файла
        :param mode: режим открытия
        :return: None
        """
        if not self.file:
            self.close_file()

        self.file = open(self.path_to_file, mode, encoding='utf-8')

        if self.type_of_file == "csv":
            if mode == "r":
                self.reader = csv.DictReader(self.file)

            elif mode == "a":
                self.file = open(self.path_to_file, mode, newline="",
                                 encoding='utf-8')
                self.writer = csv.DictWriter(self.file,
                                             fieldnames=[self.key],
                                             )
                self.writer.writeheader()

            elif mode == 'w':
                self.file = open(self.path_to_file, mode, newline='',
                                 encoding='utf-8')

                self.writer = csv.DictWriter(self.file,
                                             fieldnames=[self.key],
                                             )
                self.writer.writeheader()

    def read_file(self) -> str:
        """
        Чтение файла
        :return: считанное значение
        """
        if self.file is None:
            self.open_file('r')

        if self.type_of_file == "txt":
            try:
                return self.file.readline()
            except StopIteration:
                return ''

        if self.type_of_file == "csv":
            try:
                return next(self.reader)[self.key]
            except StopIteration:
                return ''

    def close_file(self) -> None:
        """
        Метод закрытия файла
        :return: None
        """
        if self.file is not None:
            self.file.close()
            self.file = None
            self.reader = None
            self.writer = None

    def transform_item(self, item: str) -> Union[str, int, float]:
        """Метод для преобразования элемента при записи в csv файл"""
        if self.type_data == 'i':
            item = int(item)
        elif self.type_data == 's':
            item = str(item).replace('\n', '')
        elif self.type_data == 'f':
            item = float(item)

        return item

    def write_file(self, data: str) -> None:
        """
        Запись в файл
        :param data: записываемое значение
        :return: None
        """
        if self.type_of_file == 'txt':
            self.file.write(str(data))
        elif self.type_of_file == 'csv':
            if data:
                self.writer.writerow(
                    {self.key: self.transform_item(data)},
                )

    def clean(self) -> None:
        """
        Очистка файла
        :return: None
        """

        self.open_file('w')
        self.write_file('')
        self.close_file()

        self.lines = 0

    def delete(self) -> None:
        """
        Удаление файла
        :return: None
        """
        self.close_file()
        os.remove(self.path_to_file)
        self.path_to_file = None
