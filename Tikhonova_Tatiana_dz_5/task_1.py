# 1.Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных будет свидетельствовать пустая строка.
with open('text_1.txt', 'w', encoding='utf-8') as f:
    i = None
    while i != '':
        i = (input('введите данные: '))
        f.write(i + '\n')
