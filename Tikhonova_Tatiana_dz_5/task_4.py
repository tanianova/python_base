# 4.Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

with open('text_4.txt', 'r', encoding='utf-8') as f:
    file_content = f.read().splitlines()

new_list = []
eng_keys = []
rus_keys = ['один', 'два', 'три', 'четыре', 'пять', 'шесть',
            'семь', 'восемь', 'девять', 'десять']

for i in file_content:
    words = i.split()
    eng_keys.append(words[0])
for i in range(len(file_content)):
    new_row = file_content[i].replace(eng_keys[i], rus_keys[i])
    new_list.append(new_row)

new_file = '\n'.join(new_list)

with open('text_4_new.txt', 'w', encoding='utf-8') as new_f:
    new_f.writelines(new_file)
