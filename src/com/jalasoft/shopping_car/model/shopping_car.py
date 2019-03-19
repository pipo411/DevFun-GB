from pprint import pprint

from src.com.jalasoft.shopping_car.db.database_manager import DatabaseManager
from src.com.jalasoft.shopping_car.model.item import Item
from src.com.jalasoft.shopping_car.model.store import Store


class Shoppingcar(Store):

    def __init__(self):
        super().__init__()

    def buy(self, items):
        for item in items:
            if item.get_name() in self.db_manager.get_items_as_dictionary():
                super().decrease_item_stock(item)

