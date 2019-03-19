class Item:

    def __init__(self, name="", price=0, quantity=0):
        self.__id = 0
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def update_quantity(self, quantity):
        self.__quantity += quantity

    def decrease_quantity(self, quantity):
        self.__quantity -= quantity if self.get_quantity() >= quantity else self.get_quantity()
