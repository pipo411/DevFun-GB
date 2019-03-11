from com.jalasoft.shopping_car.model.item_2 import Item2
from com.jalasoft.shopping_car.model.store import Store


class Shoppingcar(Store):

    def __init__(self, items):
        super().__init__()
        self.sell_items = items

    def add_quantity(self, id, quantity):
        self.sell_items[id]["quantity"] = quantity

    def remove_item(self, item_id):
        self.sell_items.pop(item_id)

    def get_total_price(self):
        price = 0
        for item_key in self.sell_items.keys():
            print("ENTRO",self.store_stock.keys())
            print(item_key)
            if item_key in self.store_stock.keys():

                print(self.store_stock[item_key])
                price += self.store_stock[item_key].get_price()
        return price

    def buy_items(self):
        print("ENTRO")
        for item_sell in self.sell_items:
            print(item_sell)
            if item_sell in self.store_stock:
                print("ENTRO")
                self.update_stock(item_sell)

