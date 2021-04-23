"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
import random
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car started to move')

    def stop(self):
        print('Car stopped')

    def turn(self, direction):
        print(f'Car turns {direction}')

    def show_speed(self):
        speed = random.randint(1, 150)
        print(f'current speed is {speed}')

class TownCar(Car):
    def show_speed(self):
        speed = random.randint(1, 100)
        if speed > 60:
            print(f'current speed is {speed}, please slow down')

class SportCar(Car):
    print('sport car')

class WorkCar(Car):
    def show_speed(self):
        speed = random.randint(1, 100)
        if speed > 40:
            print(f'current speed is {speed}, please slow down')

class PoliceCar(Car):
    print('police car')
