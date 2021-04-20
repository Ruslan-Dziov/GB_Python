"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}]
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json
with open('hw_7.txt', 'r', encoding='utf-8') as f:
    av_profit = []
    loss = []
    dict_profit = {}
    dict_loss = {}
    result = []
    for line in f:
        list_ = list(line.split())
        profit = (int(list_[2]) - int(list_[3]))
        if profit > 0:
            av_profit.append(profit)
            dict_profit.update({list_[0]: profit})
        else:
            dict_loss.update({list_[0]: profit})
    print(f'Фирмы с прибылью: {dict_profit}')
    print(f'Фирмы с убытками: {dict_loss}')
    av_profit = sum(av_profit) / len(av_profit)
    dict_av_profit = {"average_profit": av_profit}
    print(f'Средняя прибыль: {dict_av_profit}')
    result.append(dict_profit)
    result.append(dict_av_profit)
    result.append(dict_loss)
print(f'итоговый словарь для json: {result}')
with open('hw_7.json', 'w') as new_f:
    json.dump(result, new_f)
