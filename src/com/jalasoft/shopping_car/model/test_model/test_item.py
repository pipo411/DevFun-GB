import unittest

from src.com.jalasoft.shopping_car.model.item import Item


class item_test(unittest.TestCase):

    def test_create_item(self):
        item = Item("oil", 15.6, 25)
        expected = ("oil", 15.6, 25)
        assert expected[0] == item.get_name()
        assert expected[1] == item.get_price()
        assert expected[2] == item.get_quantity()

    def test_set_item_name_quantity_price(self):
        expected_item = ("carrot", 2.3, 69)
        item = Item("oil", 15.6, 25)
        item.set_name(expected_item[0])
        item.set_price(expected_item[1])
        item.set_quantity(expected_item[2])
        assert expected_item[0] == item.get_name()
        assert expected_item[1] == item.get_price()
        assert expected_item[2] == item.get_quantity()
