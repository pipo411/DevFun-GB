from src.com.jalasoft.shopping_car.model.item import Item


class Store:
    store_stock = {}

    def __init__(self):
        pass

    def add_item(self, item):
        if item.get_name() in self.store_stock.keys():
            item.set_quantity()
        else:
            self.store_stock[item.get_name()] = item


jabon = Item("jabon", 12.0)
jabon2 = Item("jabon", 12.0)
oreo = Item("Oreo", 5.0)
store = Store()
store.add_item(jabon)
store.add_item(jabon2)
store.add_item(oreo)
print(store.store_stock)
for i in store.store_stock.values():
    print(i.get_quantity())
