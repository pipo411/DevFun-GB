"""
This class create item objects.
"""
from src.com.jalasoft.shopping_car.logger import LOG


class Item:
    """
    Create item objects.
    """

    def __init__(self, name="", price=0, quantity=0):
        """
        Item constructor.
        :param name:        str     item_name
        :param price:       str     item_price
        :param quantity:    str     item_quantity
        """
        LOG.info('Enter on Item constructor')
        self.__id = 0
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_name(self):
        """
        Function return item_name
        :return:    str item_name
        """
        LOG.info('GET item_name')
        return self.__name

    def get_price(self):
        """
        Function return item_price
        :return: float  item_price
        """
        LOG.info('GET item_price')
        return self.__price

    def get_quantity(self):
        """
        Function return item_quantity
        :return:    int item_quantity
        """
        LOG.info('GET item_quantity')
        return self.__quantity

    def get_id(self):
        """
        Function return item_id
        :return:    str item_id
        """
        LOG.info('GET item_id')
        return self.__id

    def set_id(self, item_id):
        """
        Function set the item_id
        :param item_id:      str item_id
        """
        LOG.info('SET item_id')
        self.__id = item_id

    def set_name(self, name):
        """
        Function set the item_name
        :param id:      str item_name
        """
        LOG.info('SET item_name')
        self.__name = name

    def set_price(self, price):
        """
        Function set the item_price
        :param id: float item_price
        """
        LOG.info('SET item_price')
        self.__price = price

    def set_quantity(self, quantity):
        """
        Function set the item_quantity
        :param id: float item_quantity
        """
        LOG.info('SET item_quantity')
        self.__quantity = quantity
