# 7.Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}+{self.b}j'

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)


f = ComplexNumber(2, 4)
e = ComplexNumber(3, 5)
g = ComplexNumber(4, 6)
print(f)
print(e)
print(g)
print(f + e + g)
print(f * e)
