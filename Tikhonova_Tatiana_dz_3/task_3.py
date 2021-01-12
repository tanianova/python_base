# 3.Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
# аргументов.


def my_func(arg_1, arg_2, arg_3):
    if arg_1 < arg_2 and arg_1 < arg_3:
        return arg_2 + arg_3
    elif arg_2 < arg_1 and arg_2 < arg_3:
        return arg_3 + arg_1
    else:
        return arg_1 + arg_2


print(my_func(10, 6, 8))
print(my_func(1, 6, 8))
print(my_func(10, 6, 1))
