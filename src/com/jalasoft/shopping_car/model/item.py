class Item:

    def __init__(self, name, price):
        self.item = {"name": name,
                     "price": price,
                     "quantity": 0}

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

    def update_quantity(self, quantity):
        self.item["quantity"] += quantity

    def decrease_quantity(self, quantity):
        self.item["quantity"] -= quantity

    def get_item_detail(self):
        return self.item
