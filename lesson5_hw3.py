"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

# with open('salary.txt', 'w', encoding="utf-8") as f:
#     f.write('Хадарцев 25000\nФазаев 20000\nАндиев 15000\nКачмазов 12000')
with open('hw_3.txt', 'r', encoding="utf-8") as f:
    dict_ = {}
    for lines in f:
        lines = lines.split()
        dict_.update({lines[0]: lines[1]})
    sal_less_15 = ''
    sal_all = []
    for p in dict_:
        if int(dict_[p]) < 20000:
            sal_less_15 += (p + ', ')
        sal_all.append(int(dict_[p]))
    print('Сотрудник(и) ', sal_less_15, 'имеет(ют) зарплату меньше 20 тыс.')
    aver = sum(sal_all) / len(sal_all)
    print(f'Cредняя зарплата составляет {aver}')




