# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).

# month = int(input('введите месяц в виде целого числа от 1 до 12: '))
month = int('11')

season_list = ['зима', 'весна', 'лето', 'осень', 'зима']
season_dict = {
    (1, 2, 12): 'зима',
    (3, 4, 5): 'весна',
    (6, 7, 8): 'лето',
    (9, 10, 11): 'осень'
}

for key, val in season_dict.items():
    if month in key:
        print(val)

season = month // 3
print(season_list[season])
