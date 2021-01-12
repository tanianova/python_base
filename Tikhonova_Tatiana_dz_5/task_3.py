# 3.Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('text_3.txt', 'r', encoding='utf-8') as f:
    file_content = f.read().splitlines()

surname = []
salary = []
summary_salary = 0
for i in file_content:        #взяла список, из него каждую строку разделила
    words = i.split()         #преобразовала список в строки. поделила строку на пробел
    nums = float(words[1])     #(cтроки из чисел) в числа
    salary.append(nums)
    if nums < 20000:
        surname.append(words[0])
for i, el in enumerate(salary):
    summary_salary += el
average_salary = summary_salary / len(salary)

print(f'средний доход сотрудников составляет: {average_salary}')
print(f'зарплата менее 20000 у следующих сотрудников: {surname}')
