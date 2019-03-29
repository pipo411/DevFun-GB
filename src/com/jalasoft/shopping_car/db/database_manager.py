import logging
import time

from src.com.jalasoft.shopping_car.db.database_connection import DatabaseConnection
from src.com.jalasoft.shopping_car.logger import LOG
from src.com.jalasoft.shopping_car.model.item import Item


time = (time.strftime("%d/%m/%y"))


class DatabaseManager:
    db = DatabaseConnection().get_database()

    def __init__(self):
        self.db_connection = self.db

    def insert_element(self, item):
        LOG.debug("Insert Item")
        LOG.debug(item.get_name())
        self.db_connection.execute("INSERT into items (NAME,PRICE,QUANTITY) values (?,?,?)",
                                   (item.get_name(), item.get_price(), item.get_quantity()))
        self.db_connection.commit()
        LOG.debug("Complete insert item")

    def delete_element(self, id):
        self.db_connection.execute("""DELETE FROM items WHERE  ID = ?""", (id,))
        self.db_connection.commit()

    def update_quantity_field(self, quantity, id):
        self.db_connection.execute("""UPDATE items SET QUANTITY = ? WHERE  ID = ?""",
                                   (quantity, id))
        self.db_connection.commit()

    def update_item_description(self, id, name=None, price=None):
        if name is not None:
            self.db_connection.execute("""UPDATE items SET NAME = ? WHERE  ID = ?""",
                                       (name, id))
        if price is not None:
            self.db_connection.execute("""UPDATE items SET PRICE = ? WHERE  ID = ?""",
                                       (price, id))
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

    def insert_element_records(self, product):
        print("Insert ", product.get_name())
        self.db_connection.execute("INSERT into records (NAME,PRICE,QUANTITY,PURCHASE_DATE) values (?,?,?,?)",
                                   (product.get_name(), product.get_price(), product.get_quantity(), time))
        self.db_connection.commit()

    def get_records_as_list(self):
        cursor = self.db_connection.cursor()
        records = cursor.execute("select ID,NAME,PRICE,QUANTITY,PURCHASE_DATE from records  WHERE QUANTITY  > 0")
        list_of_records = []
        for row in records:
            list_of_records.append({"name": row[1], "price": row[2], "quantity": row[3], "date": time})
        return list_of_records

# db = DatabaseManager()
# print(db.get_records_as_list())
# oreo = Item("oreo", 17.5, 9)
# db.insert_element_records(oreo)
# print(db.get_records_as_list())
# db.delete_element(id)
# db.insert_element_records(oreo)
# print(db.get_records_as_list())
