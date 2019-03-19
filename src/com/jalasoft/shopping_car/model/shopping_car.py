from pprint import pprint

from src.com.jalasoft.shopping_car.db.database_manager import DatabaseManager
from src.com.jalasoft.shopping_car.model.item import Item
from src.com.jalasoft.shopping_car.model.store import Store


class Shoppingcar():
    db_manager = DatabaseManager()

    def __init__(self, items):
        self.selling_items = items
        self.store_stock = self.db_manager.get_items_as_dictionary()

    def add_quantity(self, id, quantity):
        self.selling_items[id]["quantity"] = quantity

    def remove_item(self, item_id):
        del self.selling_items[item_id]

    def buy(self):
        print(self.selling_items)
        print(self.store_stock)
        for item_key in self.store_stock:
            if 



# oreo = Item("oreo", 2.5, 15)
# orange = Item("orange",5)
cookie = Item("nucita", 10, 1)
db = DatabaseManager()
store = Store()
# store.add_item(cookie)
# pprint(store.get_items())
# print(db.get_items_as_dictionary())
# compras = {"cocacola": {"name": "cocacola", "quantity": 5}}
# cart = Shoppingcar(compras)
# cart.add_quantity("cocacola",7)
# cart.buy()


d = {"a":{"no":12},"b":{"si":10}}
for i in d:
    print(i)