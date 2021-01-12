# 6.Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
# быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл. Вторым пунктом
# необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
from itertools import count, cycle


def list_numbers(num):
    for el in count(num):
        if el <= 10:
            print(el)
        else:
            break


list_numbers(3)


def list_cycle(*argv):
    i = 0
    for el in cycle(argv):
        print(el)
        i += 1
        if i > 10:
            break


list_cycle(True, 2, 'hello')


