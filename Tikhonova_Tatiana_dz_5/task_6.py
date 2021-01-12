# 6.Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие
# лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно,
# чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('text_6.txt', 'r', encoding='utf-8') as f:
    file_content = f.read().splitlines()

keys = [el.split()[0][:-1] for el in file_content]
values = []

for el in file_content:
    subject, lecture, practice, lab = el.split()
    hours = lecture, practice, lab
    lectures = [float(lecture[:-3]) if lecture[:-3].isdigit() else 0]
    practices = [float(practice[:-4]) if practice[:-4].isdigit() else 0]
    labs = [float(lab[:-5]) if lab[:-5].isdigit() else 0]
    hour_sum = sum(lectures + practices + labs)
    values.append(hour_sum)
my_dict = dict(zip(keys, values))
print(my_dict)


"""решение через тернарный оператор"""
# keys = [el.split()[0][:-1] for el in file_content]  #генератор предметов, удалила ':'
# lectures = []
# practices = []
# labs = []
# values = []
#
# for el in file_content:
#     subject, lecture, practice, lab = el.split()
#     hours = lecture, practice, lab
#     if lecture[:-3].isdigit():         #беру срез, чтобы было только число, проверяю на '-'
#         lectures.append(float(lecture[:-3]))
#     else:
#         lectures.append(0)
#     if practice[:-4].isdigit():
#         practices.append(float(practice[:-4]))
#     else:
#         practices.append(0)
#     if lab[:-5].isdigit():
#         labs.append(float(lab[:-5]))
#     else:
#         labs.append(0)
# for i in range(len(file_content)):
#     h = lectures[i] + practices[i] + labs[i]
#     values.append(h)
#
# my_dict = dict(zip(keys, values))
# print(my_dict)
