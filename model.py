import json
import os
from faker import Faker

# Класс для работы с файлами
class FileManager:
    @staticmethod
    def read_file_json(filename: str) -> list:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as json_file:
                return json.load(json_file)
        return []

    @staticmethod
    def write_file_json(filename: str, write_text: list):
        with open(filename, 'w', encoding='UTF-8') as json_file:
            write_text = sorted(write_text, key=lambda x: x["name"])
            json.dump(write_text, json_file, ensure_ascii=False, indent=4)

    @staticmethod
    def clear_file_json(filename: str):
        with open(filename, 'w', encoding='UTF-8') as json_file:
            json.dump([], json_file, ensure_ascii=False, indent=4)

# Класс для представления контакта
class Contact:
    def __init__(self, name, phone_number, company):
        if not name or not phone_number:
            raise ValueError("Имя и номер телефона не могут быть пустыми")
        self.name = name
        self.phone_number = phone_number
        self.company = company

    def to_dict(self):
        return {
            'name': self.name,
            'phone_number': self.phone_number,
            'company': self.company,
        }

# Класс для управления телефонной книгой
class CallBook:
    def __init__(self, filename):  # Убедитесь, что здесь есть параметр filename
        self.filename = filename
        self.contacts = FileManager.read_file_json(filename)  # Загружаем контакты из файла

    def add_contact(self, contact: Contact):
        self.contacts.append(contact.to_dict())
        FileManager.write_file_json(self.filename, self.contacts)

    def find_contact(self, search_area: str, find_name: str):
        if search_area == 'n':
            return [c for c in self.contacts if find_name in c["name"]]
        elif search_area == 'pn':
            return [c for c in self.contacts if find_name in c["phone_number"]]
        elif search_area == 'c':
            return [c for c in self.contacts if find_name in c["company"]]
        return []

    def clear(self):
        FileManager.clear_file_json(self.filename)
        self.contacts = []

    def show_all(self):
        return self.contacts
