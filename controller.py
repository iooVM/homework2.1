from model import CallBook, Contact
from view import menu, menu_show_all, menu_callbook_add, menu_callbook_find
from faker import Faker

# Класс для управления логикой приложения
class CallBookManager:
    def __init__(self, filename):
        self.callbook = CallBook(filename)  # Создаем экземпляр телефонной книги

    def start_programm(self):
        # Основной цикл программы
        choice = ''
        while choice != 'e':
            choice = menu()  # Отображаем меню и получаем выбор пользователя
            if choice == 'p':
                data = self.callbook.show_all()  # Получаем все контакты
                menu_show_all(data)  # Отображаем контакты
            elif choice == 'a':
                self.add_contact()  # Добавляем новый контакт
            elif choice == 'c':
                self.callbook.clear()  # Очищаем телефонную книгу
            elif choice == 'f':
                self.find_contact()  # Ищем контакт

    def add_contact(self):
        # Метод для добавления контакта
        choice = menu_callbook_add()  # Получаем выбор пользователя
        if choice == 'g':
            # Генерация случайного контакта
            fake = Faker('ru_RU')
            contact = Contact(fake.name(), fake.phone_number(), fake.company())
            self.callbook.add_contact(contact)  # Добавляем сгенерированный контакт
        elif choice == 'a':
            # Ввод данных для нового контакта вручную
            name = input("Введите имя: ")
            phone_number = input("Введите номер телефона: ")
            company = input("Введите компанию: ")
            contact = Contact(name, phone_number, company)  # Создаем новый контакт
            self.callbook.add_contact(contact)  # Добавляем контакт в телефонную книгу

    def find_contact(self):
        # Метод для поиска контакта
        search_area, find_name = menu_callbook_find()  # Получаем критерий поиска и имя
        found_contacts = self.callbook.find_contact(search_area, find_name)  # Ищем контакт
        menu_show_all(found_contacts)  # Отображаем найденные контакты
