"""
This class contents the unit tests for DatabaseConnection class
"""
import unittest
from src.com.jalasoft.shopping_car.db.database_manager import DatabaseManager


class database_connection_test(unittest.TestCase):

    def test_db_is_an_object_ofDatabaseManager(self):
        """
        This method validates if object is sent
        """
        connection = DatabaseManager

        self.assertIsInstance(connection, DatabaseManager)

    def test_get_db_connection(self):
        """
        This method validates the db connection
        """
        connection = DatabaseManager.db_connection()

        self.assertTrue(connection)
