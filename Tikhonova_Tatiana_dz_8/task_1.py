# 1.Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, *args):
        self.str_date = str(args)

    def __str__(self):
        return str(self.str_date)

    @classmethod
    def get_date_from_str(cls, str_date):
        list_number = [int(number) for number in str_date.split('-')]
        day = list_number[0]
        month = list_number[1]
        year = list_number[2]
        return cls(day, month, year)

    @staticmethod
    def check_date(str_date):
        list_number = [int(number) for number in str_date.split('-')]
        if 1 <= list_number[0] <= 31 and 1 <= list_number[1] <= 12 and 2020 >= list_number[2] >= 0:
            return 'проверка ввода даты пройдена'
        else:
            return 'ошибка валидации '


try:
    print(Date.get_date_from_str('9-11-1992'))
    print(Date.check_date('9-11-1992'))
except ValueError as e:
    print(f'ошибка ввода данных: {e}')
except Exception as e:
    print(f'ошибка: {e}')

