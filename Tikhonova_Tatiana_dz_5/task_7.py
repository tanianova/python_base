# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о
# фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

with open('text_7.txt', 'w', encoding='utf-8') as f:
    firms = ['firm_1 ООО 10000 5000\n', 'firm_2 ООО 30000 35000\n', 'firm_3 ИП 40000 7000\n',
             'firm_4 ОАО 300000 200000\n', 'firm_5 АО 500000 550000\n']
    f.writelines(firms)

with open('text_7.txt', 'r', encoding='utf-8') as f:
    file_content = list(map(str.strip, f.readlines()))

summary_profit = 0
i = 0
firms_keys = []
firms_values = []
full_list = []

for line in file_content:
    words = line.split()
    profit = float(words[2]) - float(words[3])
    firms_keys.append(words[0])
    firms_values.append(profit)
    if profit >= 0:
        i += 1
        print(f'прибыль {words[0]} : {profit}')
        summary_profit += profit
    else:
        print(f'убытки {words[0]} составили: {abs(profit)}')
average_profit = summary_profit / i
print(f'средняя прибыль составляет: {average_profit}')

firms_dict = dict(zip(firms_keys, firms_values))
average_dict = {'average profit': average_profit}
full_list.append(firms_dict)
full_list.append(average_dict)
print(full_list)

with open('text_7.json', 'w') as write_f:
    json.dump(full_list, write_f)

