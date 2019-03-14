from src.com.jalasoft.shopping_car.db.database_connection import DatabaseConnection


class DatabaseManager:
    db = DatabaseConnection().get_database()

    def __init__(self):
        self.db_connection = self.db

    def insert_element(self, name, price, quantity):
        self.db_connection.execute("INSERT into items (NAME,PRICE,QUANTITY) values (?,?,?)", (name, price, quantity))
        self.db_connection.commit()

    def update_quantity_field(self, quantity, id):
        self.db_connection.execute("""UPDATE items SET QUANTITY = ? WHERE  ID = ?""", (quantity, id))

    def get_items_as_dictionary(self):
        items = self.db_connection.execute("select ID,NAME,PRICE,QUANTITY from items")
        dict_of_items = {}
        for row in items:
            dict_of_items[row[1]] = {"id": row[0], "name": row[1], "price": row[2], "quantity": row[3]}
        return dict_of_items

