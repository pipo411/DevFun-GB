from src.com.jalasoft.shopping_car.model.store import Store


class Shoppingcar(Store):

    def __init__(self):
        super().__init__()

    def buy(self, products):
        print("Start Buy")
        for _, item in products.items():
            if item.get_name() in self.db_manager.get_items_as_dictionary():
                super().decrease_item_stock(item)

    def save_sell(self, products):
        print("Start records")
        for _, item in products.items():
            self.db_manager.insert_element_records(item)
