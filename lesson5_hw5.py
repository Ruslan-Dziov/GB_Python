"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
"""
with open('hw_5.txt', 'w') as f:
    f.write(input('введите числа через пробел для сохранения в созданном файле hw_5.txt: '))

with open('hw_5.txt', 'r') as f:
     list_sum = (f.readline()).split()
     print('Сумма чисел = ', sum(list(map(int, list_sum))))
