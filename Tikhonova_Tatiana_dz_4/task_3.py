# 3.Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.

numbers = [num for num in range(20, 241) if num % 20 == 0 or num % 21 == 0]
print(numbers)
