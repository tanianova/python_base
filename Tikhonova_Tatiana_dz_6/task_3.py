# 3.Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
# (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров.


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'полное имя сотрудника {self.name} {self.surname}'

    def get_total_income(self):
        total_income = sum(self._income.values())
        return f'доход с учетом премии составляет {total_income} $'


user_1 = Position('Иван', 'Иванов', 'слесарь', 750, 90)
print(user_1.name)
print(user_1.surname)
print(user_1.get_full_name())
print(user_1.get_total_income())
