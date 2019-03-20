from src.com.jalasoft.shopping_car.db.database_manager import DatabaseManager
from src.com.jalasoft.shopping_car.model.item import Item
from src.com.jalasoft.shopping_car.model.store import Store


class Shoppingcar(Store):

    def __init__(self):
        super().__init__()

    def buy(self, items):
        print("ENTRO A LA VENTA")
        for _,item in items.items():
            if item.get_name() in self.db_manager.get_items_as_dictionary():
                super().decrease_item_stock(item)


# pipoca = Item("pipoca", 2, 10)
# oreo = Item("oreo", 0, 15)
# list = {"pipoca": pipoca, "oreo": oreo}
# db = DatabaseManager()
# store = Store()
# # store.add_item(pipoca)
# for _,item in db.get_items_as_dictionary().items():
#     print(item.get_name())
#     print(item.get_price())
#     print(item.get_quantity())
# cart = Shoppingcar()
# cart.buy(list)
# print("*****************************************")
# for _,item in db.get_items_as_dictionary().items():
#     print(item.get_name())
#     print(item.get_price())
#     print(item.get_quantity())
