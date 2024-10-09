import unittest
from model import CallBook, Contact
import os
import json

class TestCallBook(unittest.TestCase):
    def setUp(self):
        # Создаем временный файл для тестов
        self.test_filename = 'test_callbook.json'
        self.callbook = CallBook(self.test_filename)

    def tearDown(self):
        # Удаляем временный файл после тестов
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_add_contact(self):
        contact = Contact("Иван Иванов", "123456789", "Компания А")
        self.callbook.add_contact(contact)
        self.assertEqual(len(self.callbook.contacts), 1)
        self.assertEqual(self.callbook.contacts[0]['name'], "Иван Иванов")

    def test_find_contact_by_name(self):
        contact1 = Contact("Иван Иванов", "123456789", "Компания А")
        contact2 = Contact("Петр Петров", "987654321", "Компания Б")
        self.callbook.add_contact(contact1)
        self.callbook.add_contact(contact2)

        found_contacts = self.callbook.find_contact('n', "Иван")
        self.assertEqual(len(found_contacts), 1)
        self.assertEqual(found_contacts[0]['name'], "Иван Иванов")

    def test_find_contact_by_phone_number(self):
        contact = Contact("Иван Иванов", "123456789", "Компания А")
        self.callbook.add_contact(contact)

        found_contacts = self.callbook.find_contact('pn', "123456789")
        self.assertEqual(len(found_contacts), 1)
        self.assertEqual(found_contacts[0]['phone_number'], "123456789")

    def test_clear_contacts(self):
        contact = Contact("Иван Иванов", "123456789", "Компания А")
        self.callbook.add_contact(contact)
        self.callbook.clear()
        self.assertEqual(len(self.callbook.contacts), 0)

    def test_show_all_contacts(self):
        contact1 = Contact("Иван Иванов", "123456789", "Компания А")
        contact2 = Contact("Петр Петров", "987654321", "Компания Б")
        self.callbook.add_contact(contact1)
        self.callbook.add_contact(contact2)

        all_contacts = self.callbook.show_all()
        self.assertEqual(len(all_contacts), 2)

if __name__ == '__main__':
    unittest.main()
