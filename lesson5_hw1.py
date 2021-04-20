"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

list_w = []
with open('hw_1.txt', 'w', encoding="utf-8") as f:
    while True:
        line = input('Введите строку или нажмите Enter для завершения ')
        list_w.append(line+'\n')
        if line == '':
            break

    f.writelines(list_w)
