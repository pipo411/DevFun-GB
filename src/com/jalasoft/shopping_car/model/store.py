from src.com.jalasoft.shopping_car.db.database_manager import DatabaseManager
from src.com.jalasoft.shopping_car.model.item import Item


class Store:
    db_manager = DatabaseManager()

    def __init__(self):
        self.store_stock = self.db_manager.get_items_as_dictionary()

    def add_item(self, item):
        if not item.get_name() in self.store_stock:
            self.db_manager.insert_element(name=item.get_name(), price=item.get_price(), quantity=item.get_quantity())
        else:
            item.update_quantity(item.get_quantity())
            self.db_manager.update_quantity_field(quantity=item.get_quantity(),
                                                  id=self.store_stock[item.get_name()]["id"])

    def decrease_item_stock(self, item, quantity):
        o = self.store_stock[item.get_name()]["quantity"]
        self.db_manager.update_quantity_field(quantity=item.get_quantity(),
                                              id=self.store_stock[item.get_name()]["id"])


    def edit_item(self, item_name, name, price):
        self.store_stock[item_name].set_name(name)
        self.store_stock[item_name].set_price(price)

    def get_items(self):
        self.store_stock = self.db_manager.get_items_as_dictionary()
        return self.store_stock

    def get_item(self, item_name):
        return self.store_stock[item_name].get_item_detail()

