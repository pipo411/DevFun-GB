import unittest

from src.com.jalasoft.shopping_car.model.item import Item
from src.com.jalasoft.shopping_car.model.store import Store


class store_test(unittest.TestCase):

    def test_add_item(self):
        item = Item("item3", 15.6, 25)
        store = Store()
        store.add_item(item)
        assert store.get_items()[item.get_name()].get_name() == item.get_name()
        assert store.get_items()[item.get_name()].get_price() == item.get_price()
        assert store.get_items()[item.get_name()].get_quantity() == item.get_quantity()
        store.delete_product(item.get_name())

    def test_decrease_item_stock(self):
        item = Item("chocolate", 15.6, 25)
        store = Store()
        store.add_item(item)
        actual_item = (item.get_name(), item.get_price(), item.get_quantity())
        item = Item("chocolate", 15.6, 5)
        store.decrease_item_stock(item)
        assert not actual_item[2] == store.get_items()[item.get_name()].get_quantity()
        store.delete_product(item.get_name())

    def test_delete_item(self):
        item1 = Item("oil1", 15.6, 25)
        item2 = Item("chocolate1", 15.6, 25)
        item_name = ("oil1", "chocolate1")
        store = Store()
        store.add_item(item1)
        store.add_item(item2)
        store.delete_product(item_name[0])
        assert not item_name[0] in store.get_items().keys()
        store.delete_product(item_name[1])
        assert not item_name[1] in store.get_items().keys()

    def test_edit_item(self):
        item = Item("product_edit", 25.6, 100)
        store = Store()
        store.add_item(item)
        actual_item_info = (item.get_name(), item.get_price())
        store.edit_item(item.get_name(), "product_edited", 63.6)
        assert not actual_item_info[0] == store.get_items()["product_edited"].get_name()
        assert not actual_item_info[1] == store.get_items()["product_edited"].get_price()
        store.delete_product("product_edited")
