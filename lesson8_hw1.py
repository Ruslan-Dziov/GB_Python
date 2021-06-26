"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
class Date:

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod

    def get_number(cls, date_str):
        data_list = list(map(int, date_str.split('-')))
        return data_list



    @staticmethod
    def validation_date(date_str):
        data_list = list(map(int, date_str.split('-')))
        day = data_list[0]
        month = data_list[1]
        year = data_list[2]
        print(day, month, year)
        days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if month > 12:
            return 'this month is not existing'
        if day > days.get(month):
            return 'this day is not existing'
        else:
            return 'date is validated'

