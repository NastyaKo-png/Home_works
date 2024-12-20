# lesson_3_task_1.py

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        print(self.first_name)

    def print_last_name(self):
        print(self.last_name)

    def print_full_name(self):
        print(f"{self.first_name} {self.last_name}")

# Создание экземпляра класса
my_user = User("Иван", "Иванов")

# Вызов методов
my_user.print_first_name()
my_user.print_last_name()
my_user.print_full_name()
