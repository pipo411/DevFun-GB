"""
This class management the logic store.
"""

from src.com.jalasoft.shopping_car.db.database_manager import DatabaseManager

from src.com.jalasoft.shopping_car.logger import LOG


class Store:
    """
    This class management the logic store as, create, edit , obtain, delete items.
    """
    db_manager = DatabaseManager()

    def __init__(self):
        LOG.info('Enter on Store constructor')
        self.store_stock = self.db_manager.get_items_as_dictionary()

    def add_item(self, item):
        """
        Function that add aitem into data base if the item exists, it will update the quantity.
        :param item:    object item.
        """
        LOG.info('Add Product')
        LOG.info(
            "Add the item: %s , price: %s, quantity: %s"
            , item.get_name(), item.get_price(), item.get_quantity())
        if not item.get_name() in self.store_stock:
            self.db_manager.insert_element(item)
        else:
            current_item_quantity = \
                self.store_stock[item.get_name()].get_quantity() \
                + item.get_quantity()
            self.db_manager.update_quantity_field(quantity=current_item_quantity,
                                                  id=self.store_stock[item.get_name()].get_id())
        LOG.info("Complete to add a item successful")

    def decrease_item_stock(self, item):
        """
        Function that decrease the a item quantity
        :param item:    object item.
        """
        LOG.info("decrease the item %s", item.get_quantity())
        current_item_quantity = \
            self.get_items()[item.get_name()].get_quantity() \
            - item.get_quantity()
        LOG.info("current quantity: %s ", current_item_quantity)
        self.db_manager.update_quantity_field(quantity=current_item_quantity,
                                              id=self.store_stock[item.get_name()].get_id())
        LOG.info("Complete to decrease item quantity")

    def delete_product(self, item_name):
        """
        Function that delete the a item from name.
        :param item_name:    str item.
        """
        LOG.info("Start to delete item: %s on database", item_name)
        self.db_manager.delete_element(id=self.store_stock[item_name].get_id())
        LOG.info("Complete to delete item: %s on database", item_name)

    def edit_item(self, item_name, new_name, price):
        """
        Function that edit an item from item_name.
        :param item_name:   str item_name.
        :param new_name:    str new_name.
        :param price:       str price.
        """
        LOG.info("Start to edit item: %s on database", item_name)
        item_key = self.store_stock[item_name].get_id()
        self.db_manager.update_item_description(id=item_key, name=new_name, price=price)
        LOG.info("Complete to edit item: %s on database", item_name)

    def get_items(self):
        """
        Function that return the items as a dictionary.
        :return:        dict    items.
        """
        LOG.info("Get all items on stock from data base")
        self.store_stock = self.db_manager.get_items_as_dictionary()
        return self.store_stock

    def get_records_items(self):
        """
         Function that return the items records as a list of dictionaries.
        :return:
        """
        LOG.info("Get all records items from data base")
        return self.db_manager.get_records_as_list()

# store = Store()
# print(store.get_items())
# stock = store.get_items()
# print(stock["nucita"].get_id())
# store.delete_product("nucita")
# print(store.get_items())
# store.edit_item("oi", "nucita", 17.7)
# print(store.get_items())
