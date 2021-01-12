# 2.Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.


class MyZeroDivision(Exception):
    pass


class Division:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    @staticmethod
    def div_func(numb_1, numb_2):
        try:
            numb_1 / numb_2
        except Exception as e:
            raise MyZeroDivision(f'на ноль делить нельзя!: {e}')


try:
    print(Division.div_func(3, 0))
except MyZeroDivision as e:
    print(f'MyZeroDivision: {e}')




