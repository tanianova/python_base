# 5.Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

with open('text_5.txt', 'w', encoding='utf-8') as f:
    my_list = [randint(1, 100) for i in range(10)]
    f.write(str(my_list))

with open('text_5.txt', 'r', encoding='utf-8') as f:
    file_content = f.readline()
    content = file_content[1:-1]
    summary = 0
    list_numbers = content.split(', ')
    print(list_numbers)
    for i, el in enumerate(list_numbers):
        el = int(el)
        summary += el
    print(summary)
