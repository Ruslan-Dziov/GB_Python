"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def __init__(self):
        self.asphalt_weight = 25
        self.nb_of_layers = 5

    def weight_of_asphalt(self, length, width):
        self.__length = length
        self.__width = width
        weight = self.__width * self.__length * self.asphalt_weight * self.nb_of_layers
        return weight


road = Road()
print(road.weight_of_asphalt(4000, 20))


