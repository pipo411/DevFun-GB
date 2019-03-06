class Item:
    #
    # def __init__(self, name, price):
    #     self.name = name
    #     self.price = price
    #     self.quantity = 1
    #
    # def get_name(self):
    #     return self.name
    #
    # def get_price(self):
    #     return self.price
    #
    # def get_quantity(self):
    #     return self.quantity
    #
    # def set_name(self, name):
    #     self.name = name
    #
    # def set_price(self, price):
    #     self.price = price
    def __init__(self, name, price):
        self.item = {"name": name, "price": price, "quantity": 1}

    def get_name(self):
        return self.item["name"]

    def get_price(self):
        return self.item["price"]

    def get_quantity(self):
        return self.item["quantity"]

    def set_name(self, name):
        self.item["name"] = name

    def set_price(self, price):
        self.item["price"] = price

    def set_quantity(self):
        self.item["quantity"] += 1
