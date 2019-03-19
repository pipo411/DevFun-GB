from src.com.jalasoft.shopping_car.db.database_manager import DatabaseManager


class Store:
    db_manager = DatabaseManager()

    def __init__(self):
        self.store_stock = self.db_manager.get_items_as_dictionary()

    def add_item(self, item):
        if not item.get_name() in self.store_stock:
            self.db_manager.insert_element(item)
        else:
            current_item_quantity = self.store_stock[item.get_name()].get_quantity()
            item.update_quantity(current_item_quantity)
            self.db_manager.update_quantity_field(quantity=item.get_quantity(),
                                                  id=self.store_stock[item.get_name()].get_id())

    def decrease_item_stock(self, items):
        current_items = self.get_items()
        # o = self.store_stock[item.get_name()]["quantity"]
        # self.db_manager.update_quantity_field(quantity=item.get_quantity(),
        #                                       id=self.store_stock[item.get_name()]["id"])

    def edit_item(self, item_name, name, price):
        self.store_stock[item_name].set_name(name)
        self.store_stock[item_name].set_price(price)

    def get_items(self):
        self.store_stock = self.db_manager.get_items_as_dictionary()
        # for item_key,item in self.store_stock.values():
        #     print(item.get_quantity)
        #     print(item.get_name)
        return self.store_stock

    def get_item(self, item_key):
        self.store_stock = self.db_manager.get_items_as_dictionary()
        return self.store_stock[item_key]
