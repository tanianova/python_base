# 3.Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, «stop».При этом скрипт завершается, сформированный список с числами выводится на экран.
# *для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода пользователем
# очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.


class MyError(Exception):
    pass


def user_input():
    list_numbers = []
    while True:
        try:
            val = input('Для выхода введите stop. Введите данные: ')
            if val == 'stop':
                return list_numbers
            else:
                list_numbers.append(int(val))
        except Exception as e:
            print(MyError(f"Недопустимое значение: {e}. "))


try:
    print(user_input())
except MyError as e:
    print(MyError(f"Недопустимое значение: {e}"))
except Exception as e:
    print(MyError(f"error: {e}"))
