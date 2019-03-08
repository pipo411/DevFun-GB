class Store:

    def __init__(self):
        self.store_stock = []

    def add_item(self, item):
        self.store_stock.append(item)

    def remove_item(self, item):
        self.store_stock.remove(item)

    def update_item(self, actual_item, new_item):
        self.store_stock[actual_item] = new_item

    def get_items(self):
        return self.store_stock

    def get_item(self, item):
        return self.store_stock[item]
