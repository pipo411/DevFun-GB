from src.com.jalasoft.shopping_car.model.store import Store


class Shoppingcar(Store):

    def __init__(self):
        super().__init__()

    def buy(self, items):
        print("ENTRO A LA VENTA")
        for _,item in items.items():
            if item.get_name() in self.db_manager.get_items_as_dictionary():
                super().decrease_item_stock(item)
