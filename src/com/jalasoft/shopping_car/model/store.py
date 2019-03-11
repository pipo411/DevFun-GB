from com.jalasoft.shopping_car.model.item_2 import Item2


class Store:

    def __init__(self):
        self.store_stock = {}

    def add_item(self, id, item, quantity=1):
        if not id in self.store_stock.keys():
            self.store_stock[id] = item
        else:
            item.update_quantity(quantity)

    def update_item_stock(self, id, quantity=1):
        if self.store_stock[id].get_quantity() <= 1:
            self.store_stock.pop(id)
        else:
            self.store_stock[id].decrease_quantity(quantity)

    def edit_item(self, id, name, price):
        self.store_stock[id].set_name(name)
        self.store_stock[id].set_price(price)

    def get_items(self):
        items_stock = {}
        for id, item in self.store_stock.items():
            items_stock[id] = item.get_item_detail()
        return items_stock

    def get_item(self, id):
        return self.store_stock[id].get_item_detail()
