"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
"""

class Warehouse:

    """
    Description of warehouse working
    """


    def __init__(self, item):
        self.at_warehouse = {}
        self.item = item

    def receiving_to_warehouse(self, item):
        self.at_warehouse.update(item)

    def give_to_department(self, item):
        self.at_warehouse.popitem(self, item)


class OfficeEquipment:

    def __init__(self):

class Printer(OfficeEquipment):
    def __init__(self, brand, model, type_of_printer, color_printer, speed_printer, paper_format_printer, quantity):
        self.brand = brand
        self.model = model
        self.type_of_printer = type_of_printer
        self.color_printer = color_printer
        self.speed_printer = speed_printer
        self.paper_format_printer = paper_format_printer
        self.quantity = quantity

    def printer_spec(self):
        return {(self.brand, self.model, self.color_printer, self.paper_format_printer): self.quantity}


class Scaner(OfficeEquipment):
    def __init__(self,brand, model, type_of_scaner, quantity):
        self.brand = brand
        self.model = model
        self.type_of_scaner = type_of_scaner
        self.quantity = quantity

    def scaner_spec(self):
        return {(self.brand, self.model, self.type_of_scaner): self.quantity}


class Xepox(OfficeEquipment):
    def __init__(self, brand, model, type_of_xerox, color_xerox, xerox_speed, xerox_paper_format, quantity):
        self.brand = brand
        self.model = model
        self.type_of_xerox = type_of_xerox
        self.color_xerox = color_xerox
        self.xerox_speed = xerox_speed
        self.xerox_paper_format = xerox_paper_format
        self.quantity = quantity

    def xerox_spec(self):
        return {(self.brand, self.model, self.color_xerox, self.xerox_paper_format): self.quantity}
