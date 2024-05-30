import time  # Импортируем модуль time для работы с временными интервалами
import keyboard  # Импортируем модуль keyboard для работы с клавиатурными событиями

from tools import Tool  # Импортируем класс Tool из модуля tools
from user import User  # Импортируем класс User из модуля user

class Console_processor:
    def __init__(self):
        # Инициализируем класс Console_processor
        self.users = Tool.read_from_json('users.json')  # Загружаем пользователей из JSON-файла
        self.commands = {
            1: 'register',  # Команда регистрации пользователя
            2: 'list_users',  # Команда вывода всех пользователей
            3: 'stop'  # Команда остановки программы
        }

    def read(self):
        # Метод для чтения и выполнения команд
        print(self.commands)  # Печатаем доступные команды
        while True:
            print()
            command = int(input('command: '))  # Ввод команды пользователем
            if command == 3:
                return  # Останавливаем выполнение программы при команде 'stop'
            command = self.commands.get(command)  # Получаем команду по ее номеру
            if command is None:
                print('invalid command')  # Печатаем сообщение при недопустимой команде
            else:
                self.read_next(command)  # Выполняем следующую команду

    def read_next(self, command):
        # Метод для выполнения конкретной команды
        if command == 'list_users':
            print('result: ')
            for user in self.task():
                print(user.__dict__)  # Печатаем результат выполнения задачи
        elif command == 'register':
            self.users.append(self.read_user())  # Регистрируем нового пользователя
            Tool.write_to_json(self.users, 'users.json')  # Сохраняем пользователей в JSON-файл

    def task(self):
        # Метод для выполнения задачи: вывод перечня всех зарегистрированных пользователей
        return self.users  # Возвращаем список пользователей

    def read_user(self):
        # Метод для чтения данных нового пользователя
        username = input('username: ')  # Ввод имени пользователя

        password, times = self.read_password()  # Ввод пароля и временных интервалов нажатий клавиш
        print()
        return User(username, password, times)  # Возвращаем объект User

    def read_password(self):
        # Метод для чтения пароля и записи времени нажатий клавиш
        password = ''
        times = []
        last = None
        while True:
            K = keyboard.read_key()  # Чтение клавиши
            if K == 'enter' and len(password) > 0:
                input()  # Дополнительный ввод для подтверждения окончания пароля
                break
            if K == 'backspace':
                password = password[:-1]  # Удаление последнего символа из пароля
            elif keyboard.is_pressed(K):
                password += K  # Добавление символа к паролю
                if last is not None:
                    times.append(time.time() - last)  # Запись времени между нажатиями
                last = time.time()
        return password, times  # Возвращаем пароль и временные интервалы
