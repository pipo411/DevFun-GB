from src.com.jalasoft.shopping_car.db.database_manager import DatabaseManager
import logging

LOG = logging.getLogger(__name__)


class Store:
    db_manager = DatabaseManager()

    def __init__(self):
        LOG.info('Enter on Store constructor')
        self.store_stock = self.db_manager.get_items_as_dictionary()

    def add_item(self, item):
        LOG.info('Add Product')
        LOG.info(item.get_name(), item.get_price(), item.get_quantity())
        if not item.get_name() in self.store_stock:
            self.db_manager.insert_element(item)
        else:
            current_item_quantity = self.store_stock[item.get_name()].get_quantity() + item.get_quantity()
            self.db_manager.update_quantity_field(quantity=current_item_quantity,
                                                  id=self.store_stock[item.get_name()].get_id())

    def decrease_item_stock(self, item):
        current_item_quantity = self.get_items()[item.get_name()].get_quantity() - item.get_quantity()
        self.db_manager.update_quantity_field(quantity=current_item_quantity,
                                              id=self.store_stock[item.get_name()].get_id())

    def delete_product(self, item_name):
        self.db_manager.delete_element(id=self.store_stock[item_name].get_id())

    def edit_item(self, item_name, new_name, price):
        # self.store_stock[item_name].set_name(new_name)
        # self.store_stock[item_name].set_price(price)
        self.db_manager.update_item_description(id=self.store_stock[item_name].get_id(), name=new_name, price=price)

    def get_items(self):
        self.store_stock = self.db_manager.get_items_as_dictionary()
        return self.store_stock

    def get_records_items(self):
        return self.db_manager.get_records_as_list()

# store = Store()
# print(store.get_items())
# stock = store.get_items()
# print(stock["nucita"].get_id())
# store.delete_product("nucita")
# print(store.get_items())
# store.edit_item("oi", "nucita", 17.7)
# print(store.get_items())
