# 2.Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3
# и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно
# использовать функцию input().

# count = int(input('введите колво элементов: '))
# user_list = []
idx = 0

# for element in range(count):
#     element = input('введите элемент: ')
#     user_list.append(element)
#
# print(user_list)

user_list = [True, 'go', 56, 900, 'sunny']
print(user_list)

while idx < len(user_list) - 1:
    user_list[idx], user_list[idx + 1] = user_list[idx + 1], user_list[idx]
    idx += 2

print(user_list)
