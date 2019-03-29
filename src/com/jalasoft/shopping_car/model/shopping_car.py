"""
This class management the logic of shopping cart..
"""
from src.com.jalasoft.shopping_car.logger import LOG
from src.com.jalasoft.shopping_car.model.store import Store


class Shoppingcar(Store):
    """
    This class management the logic of shopping cart as, buy, save records.
    """

    def __init__(self):
        """
        Init constructor.
        """
        LOG.info('Enter on Shopping Cart constructor')
        super().__init__()

    def buy(self, products):
        """
        Function that buy a dict of items.
        :param products:   dict  products.
        """
        LOG.info("Start to buy %s", products)
        for _, item in products.items():
            if item.get_name() in self.db_manager.get_items_as_dictionary():
                super().decrease_item_stock(item)
        LOG.info("Complete the buy")

    def save_records(self, products):
        """
        Function that can save the item records from a dict of items.
        :param products:    dict items.
        """
        LOG.info("Start to save %s", products)
        for _, item in products.items():
            self.db_manager.insert_element_records(item)
        LOG.info("Complete to save item records")
