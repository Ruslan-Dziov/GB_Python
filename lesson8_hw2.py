"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class ZDiv(Exception):

    def __init__(self, txt):
        self.txt = txt

class Devision:
    def __init__(self, divisible, divider):
        self.divisible = divisible
        self.divider = divider

    def func_devision(self):

        try:
            self.divisible / self.divider
            if self.divider == 0:
                raise ZDiv('Your entered zero!')
        except ZeroDivisionError:
            print('You cannot devide by zero!')
        else:
            print(self.divisible / self.divider)

a = Devision(10, 0)
a.func_devision()