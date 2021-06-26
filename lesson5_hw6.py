"""
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}.
"""

with open('hw_6.txt', 'r', encoding='utf-8') as f:
    result_total = {}
    for line in f:
        key = ''
        value = []
        number = ''
        result = {}
        for l in line:
            if l == ':':
                break
            key += l
        for l in line:
            if l.isdigit():
                number += l
            elif number == '':
                continue
            else:
                value.append(number)
                number = ''
        value = sum(list(map(int, value)))
        result.update({key: value})
        result_total.update(result)
    print(result_total)
