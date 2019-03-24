from src.com.jalasoft.shopping_car.db.database_connection import DatabaseConnection
from src.com.jalasoft.shopping_car.model.item import Record


class DatabaseManager:
    db = DatabaseConnection().get_database()

    def __init__(self):
        self.db_connection = self.db

    def insert_element(self, record):
        print("Insert ",record.get_name())
        self.db_connection.execute("INSERT into records (NAME,PRICE,QUANTITY) values (?,?,?)",
                                   (record.get_name(),record.get_price(), record.get_quantity()))
        self.db_connection.commit()

    def update_quantity_field(self, quantity, id):
        self.db_connection.execute("""UPDATE items SET QUANTITY = ? WHERE  ID = ?""",
                                   (quantity, id))
        self.db_connection.commit()

    def get_records_as_dictionary(self):
        cursor = self.db_connection.cursor()
        records = cursor.execute("select ID,NAME,PRICE,QUANTITY,PURCHASE_DATE from records")
        dict_of_records = {}

        for row in records:
            record = Record()
            record.set_id(row[0])
            record.set_name(row[1])
            record.set_price(row[2])
            record.set_quantity(row[3])
            dict_of_records[row[1]] = record
        return dict_of_records
