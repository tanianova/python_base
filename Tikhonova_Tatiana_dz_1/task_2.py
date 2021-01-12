# 2.Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_time = int(input('введите время в секундах '))
minute = user_time // 60
hour = minute // 60
second = user_time % minute

print(f'{hour:02d}:{minute:02d}:{second:02d}')
