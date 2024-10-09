# Телефонный справочник

Это приложение представляет собой телефонный справочник, который позволяет пользователям добавлять, удалять, редактировать и искать контакты. Приложение использует JSON для хранения данных и предоставляет удобный консольный интерфейс.

## Установка

1. Убедитесь, что у вас установлен Python 3.6 или выше.
2. Склонируйте репозиторий или скачайте файлы проекта на свой компьютер.
3. Установите необходимые зависимости, если они есть. Для этого выполните команду:

   ```bash
   pip install -r requirements.txt




Использование
Запустите приложение, выполнив команду:


python main.py

В главном меню вы можете выбрать следующие действия:
e - выход из приложения
p - показать все контакты
a - добавить новую запись
c - очистить справочник
f - поиск по справочнику
При добавлении записи вы можете выбрать:
g - сгенерировать случайный контакт
a - ввести контакт вручную
w - сохранить изменения
e - выйти без сохранения
Тестирование


Для запуска автотестов выполните следующую команду:

python -m unittest test_model.py