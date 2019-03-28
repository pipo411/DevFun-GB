import unittest
from src.com.jalasoft.shopping_car.db.database_manager import DatabaseManager
from src.com.jalasoft.shopping_car.model.item import Item


class database_manager_test(unittest.TestCase):

    def test_insert_element(self):
        test_db_manager = DatabaseManager()
        test_item = Item("fanta", 10.5, 5)
        test_db_manager.insert_element(test_item)

        dictionary = test_db_manager.get_items_as_dictionary()

        self.assertEqual(dictionary["fanta"].get_name(), test_item.get_name())

    def test_update_element(self):
        test_db_manager = DatabaseManager()
        test_item = Item("sprite", 10.5, 5)
        test_db_manager.insert_element(test_item)
        dictionary = test_db_manager.get_items_as_dictionary()
        dic = dictionary["sprite"].get_id()
        test_db_manager.update_item_description(dic, name="sprite2")

        self.assertEqual("sprite2", dictionary["sprite2"].get_name())