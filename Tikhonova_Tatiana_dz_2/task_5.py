# 5.Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
new_el = int('8')

if new_el < my_list[-1]:
    my_list.append(new_el)
elif new_el > my_list[0]:
    my_list.insert(0, new_el)
else:
    for idx, el in enumerate(my_list):
        if new_el == el:
            my_list.insert(idx+1, new_el)
            break

print(my_list)
