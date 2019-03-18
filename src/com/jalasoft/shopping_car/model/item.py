class Item:

    def __init__(self, name, price, quantity=0):
        self.__item = {"name": name,
                       "price": price,
                       "quantity": quantity}

    def get_name(self):
        return self.__item["name"]

    def get_price(self):
        return self.__item["price"]

    def get_quantity(self):
        return self.__item["quantity"]

    def set_name(self, name):
        self.__item["name"] = name

    def set_price(self, price):
        self.__item["price"] = price

    def update_quantity(self, quantity):
        self.__item["quantity"] += quantity

    def decrease_quantity(self, quantity):
        self.__item["quantity"] -= quantity if self.get_quantity() >= quantity else self.get_quantity()

    def get_item_detail(self):
        return self.__item
