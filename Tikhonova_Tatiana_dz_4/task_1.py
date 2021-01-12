# 1.Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте
# в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений
# необходимо запускать скрипт с параметрами.
from sys import argv

file_name, hour, rate, bonus = argv
numbers = [float(el) for i, el in enumerate(argv[1:])]
calc_salary = numbers[0] * numbers[1] + numbers[2]
print(f'зарплата сотрудника с учетом премии в этом месяце составила {calc_salary} $')


# def salary():
#     hour = float(input('введите колво отработанных часов: '))
#     rate = float(input('введите размер ставки: '))
#     bonus = float(input('введите размер премии: '))
#     payment = hour * rate + bonus
#     return f'зарплата сотрудника с учетом премии в этом месяце составила {payment} $'
#

# print(salary())
