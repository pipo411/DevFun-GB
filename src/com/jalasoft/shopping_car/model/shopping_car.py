from src.com.jalasoft.shopping_car.model.store import Store


class Shoppingcar(Store):

    def __init__(self, items):
        super().__init__()
        self.sell_items = items

    def add_quantity(self, id, quantity):
        self.sell_items[id]["quantity"] = quantity

    def remove_item(self, item_id):
        self.sell_items.pop(item_id)
