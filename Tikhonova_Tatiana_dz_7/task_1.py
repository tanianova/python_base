# 1.Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __len__(self):
        return len(self.matrix)

    def size_matrix(self):
        return len(self.matrix), len(self.matrix[0])

    def __getitem__(self, idx):
        return self.matrix[idx]

    def __add__(self, other):
        if self.size_matrix() == other.size_matrix():
            new_matrix = []
            for row in range(len(self.matrix)):
                tmp = []
                for col in range(len(self.matrix)):
                    tmp.append(self[row][col] + other[row][col])
                new_matrix.append(tmp)
            return Matrix(new_matrix)
        else:
            return 'different sizes'


matrix_1 = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]
matrix_2 = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

matrix_3 = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3]
]

a = Matrix(matrix_1)
b = Matrix(matrix_2)
c = Matrix(matrix_3)
summary_1 = a + b + b
summary_2 = a + c
print(summary_1)
print(summary_2)
