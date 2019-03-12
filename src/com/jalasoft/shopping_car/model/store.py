from src.com.jalasoft.shopping_car.db.database_manager import DatabaseManager


class Store:
    db_manager = DatabaseManager()

    def __init__(self):
        self.store_stock = self.db_manager.get_items_as_dictionary()

    def add_item(self, item_name, item, quantity):
        if not item_name in self.store_stock.keys():
            self.store_stock[item_name] = item
            self.db_manager.insert_element(item.get_name(), item.get_price(), quantity)
        else:
            item.update_quantity(quantity)
            self.db_manager.update_quantity_field(item.get_quantity(), self.store_stock[item_name]["id"])

    def update_item_stock(self, item_name, quantity):
        if self.store_stock[item_name].get_quantity() <= 1:
            self.store_stock.pop(item_name)
        else:
            self.store_stock[item_name].decrease_quantity(quantity)

    def edit_item(self, item_name, name, price):
        self.store_stock[item_name].set_name(name)
        self.store_stock[item_name].set_price(price)

    def get_items(self):
        self.store_stock = self.db_manager.get_items_as_dictionary()
        return self.store_stock

    def get_item(self, item_name):
        return self.store_stock[item_name].get_item_detail()
