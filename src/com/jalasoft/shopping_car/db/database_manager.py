import logging

from src.com.jalasoft.shopping_car.db.database_connection import DatabaseConnection
from src.com.jalasoft.shopping_car.model.item import Item

LOG = logging.getLogger()


class DatabaseManager:
    db = DatabaseConnection().get_database()

    def __init__(self):
        self.db_connection = self.db

    def insert_element(self, item):
        LOG.info("Insert Item")
        LOG.info(item.get_name())
        self.db_connection.execute("INSERT into items (NAME,PRICE,QUANTITY) values (?,?,?)",
                                   (item.get_name(), item.get_price(), item.get_quantity()))
        self.db_connection.commit()
        LOG.info("Complete insert item")

    def update_quantity_field(self, quantity, id):
        self.db_connection.execute("""UPDATE items SET QUANTITY = ? WHERE  ID = ?""",
                                   (quantity, id))
        self.db_connection.commit()

    def get_items_as_dictionary(self):
        cursor = self.db_connection.cursor()
        items = cursor.execute("select ID,NAME,PRICE,QUANTITY from items WHERE QUANTITY  > 0")
        dict_of_items = {}

        for row in items:
            item = Item()
            item.set_id(row[0])
            item.set_name(row[1])
            item.set_price(row[2])
            item.set_quantity(row[3])
            dict_of_items[row[1]] = item
        return dict_of_items
