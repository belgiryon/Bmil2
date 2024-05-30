class User:
    def __init__(self, username, password, delay=[]):
        # Инициализируем объект класса User
        # username: Имя пользователя
        # password: Пароль пользователя
        # delay: Список временных интервалов нажатий клавиш (по умолчанию пустой список)
        self.username = username  # Устанавливаем имя пользователя
        self.password = password  # Устанавливаем пароль пользователя
        self.delay = delay  # Устанавливаем список временных интервалов нажатий клавиш
