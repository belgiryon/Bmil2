import json  # Импортируем модуль json для работы с JSON-файлами

from user import User  # Импортируем класс User из модуля user


class Tool:
    @staticmethod
    def write_to_json(users, file_name):
        # Статический метод для записи списка объектов User в JSON-файл
        with open(file_name, "w", encoding='utf-8') as file:
            # Открываем файл для записи (режим "w")
            json.dump(
                [u.__dict__ for u in users],  # Преобразуем каждый объект User в словарь
                file  # Записываем данные в файл
            )

    @staticmethod
    def read_from_json(file_name):
        # Статический метод для чтения списка объектов User из JSON-файла
        users = []  # Инициализируем пустой список для пользователей
        with open(file_name, 'r', encoding='utf-8') as file:
            # Открываем файл для чтения (режим "r")
            data = json.load(file)  # Загружаем данные из файла
            for user_data in data:
                # Для каждого словаря в загруженных данных создаем объект User
                users.append(
                    User(**user_data)  # Используем распаковку словаря для передачи данных в конструктор User
                )
        return users  # Возвращаем список объектов User