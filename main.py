
from controller import CallBookManager

# Точка входа в программу
if __name__ == '__main__':
    print('Добро пожаловать!!!')
    manager = CallBookManager('callbook.json')  # Создаем менеджер телефонной книги
    manager.start_programm()  # Запускаем программу
