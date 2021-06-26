"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_str = ''
        for line in range(len(self.matrix)):
            matrix_str += str(self.matrix[line]) + '\n'
        return matrix_str

    def __add__(self, other):
        sum_matrix = []
        matrix_str = ''
        for x in range(0, len(self.matrix)):
            list_ = []
            for y in range(len(self.matrix[x])):
                el = self.matrix[x][y] + other.matrix[x][y]
                list_.append(el)
            sum_matrix.append(list_)
        for line in range(len(sum_matrix)):
            matrix_str += str(sum_matrix[line]) + '\n'
        return matrix_str


matrix1 = [[31, 22, 58, 66], [37, 43, 47, 89], [31, 22, 87, 56], [37, 43, 12, 54]]
matrix2 = [[78, 52, 74, 89], [55, 63, 78, 25], [75, 15, 95, 58], [52, 54, 89, 69]]

a = Matrix(matrix1)
print(a)
b = Matrix(matrix2)
print(b)
print(a + b)
