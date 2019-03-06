from src.com.jalasoft.shopping_car.model.store import Store


class ShoppingCar(Store):

    def __init__(self, list_of_selling_items):
        super().__init__()
        self.list_of_selling_items = list_of_selling_items

    def get_total_price(self):
        total = 0.0
        for item_price in self.list_of_selling_items:
            if item_price in self.store_stock.values():
                total += item_price.get_price()
        return total


