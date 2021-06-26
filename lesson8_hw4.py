"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""

class Warehouse:

    """
    Description of warehouse working
    """

class OfficeEquipment:
    def __init__(self, quantity):
        self.quantity = quantity

class Printer(OfficeEquipment):
    def __init__(self, brand, model, type_of_printer, color_printer, speed_printer, paper_format_printer, quantity):
        self.brand = brand
        self.model = model
        self.type_of_printer = type_of_printer
        self.color_printer = color_printer
        self.speed_printer = speed_printer
        self.paper_format_printer = paper_format_printer
        self.quantity = quantity


class Scaner(OfficeEquipment):
    def __init__(self,brand, model, type_of_scaner, quantity):
        self.brand = brand
        self.model = model
        self.type_of_scaner = type_of_scaner
        self.quantity = quantity


class Xepox(OfficeEquipment):
    def __init__(self, brand, model, type_of_xerox, color_xerox, xerox_speed, xerox_paper_format, quantity):
        self.brand = brand
        self.model = model
        self.type_of_xerox = type_of_xerox
        self.color_xerox = color_xerox
        self.xerox_speed = xerox_speed
        self.xerox_paper_format = xerox_paper_format
        self.quantity = quantity