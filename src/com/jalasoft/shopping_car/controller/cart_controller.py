from PyQt5.QtWidgets import QTableWidgetItem, QComboBox

from src.com.jalasoft.shopping_car.model.item import Item
from src.com.jalasoft.shopping_car.ui.product_insert_view import ProductInsertView
from src.com.jalasoft.shopping_car.ui.product_show_view import ProductShowView
from src.com.jalasoft.shopping_car.ui.show_dialog import ShowDialog


class CartController:
    def __init__(self, mainView, cartModel):
        self.main_view = mainView
        self.cart_model = cartModel
        self.main_view.initUI(self)
        self.cart_list = {}

    def add_action_listener(self):
        """

        """
        self.central_widget = self.main_view.centralWidget()
        if isinstance(self.central_widget, ProductInsertView):
            self.central_widget.get_save_product_button().clicked.connect(lambda: self.action_product())
        if isinstance(self.central_widget, ProductShowView):
            self.central_widget.get_add_tocart_button().clicked.connect(lambda: self.add_to_cart())
            self.central_widget.get_buy_button().clicked.connect(lambda: self.buy_items())

    def action_product(self):
        if self.central_widget.get_menu() == 'insert':
            self.save_product()
        elif self.central_widget.get_menu() == 'edit':
            self.edit_product()
        elif self.central_widget.get_menu() == 'delete':
            self.delete_product()

    def save_product(self):
        name = self.empty_string(self.central_widget.get_name())
        price = self.empty_string(self.central_widget.get_price())
        quantity = self.empty_string(self.central_widget.get_quantity())
        if (name or price or quantity):
            self.dialog = ShowDialog("warning", "Missing fill fields \nPlease add an Item")
        else:
            pro = Item()
            pro.set_name(self.central_widget.get_name())
            pro.set_price(float(self.central_widget.get_price()))
            pro.set_quantity(int(self.central_widget.get_quantity()))
            self.cart_model.add_item(pro)
            self.dialog = ShowDialog("information", "Item was added")

    def empty_string(self, string):
        return string == ""

    def edit_product(self):
        if self.empty_string(self.central_widget.get_current_name()):
            self.dialog = ShowDialog("warning", "Missing fill fields")
        else:
            self.cart_model.edit_item(str(self.central_widget.get_current_name()),
                                      str(self.central_widget.get_name()), float(self.central_widget.get_price()))
            self.dialog = ShowDialog("information", "Item was edited")

    def delete_product(self):
        name = self.central_widget.get_name()
        if self.empty_string(name):
            self.dialog = ShowDialog("warning", "Missing fill fields \nPlease add an Item name")
        else:
            self.cart_model.delete_product(str(self.central_widget.get_name()))
            self.dialog = ShowDialog("information", "removed Item " + name)

    def load_product(self):
        self.central_widget = self.main_view.centralWidget()
        self.listProduct = self.cart_model.get_items()
        listSize = len(self.listProduct)
        self.central_widget.get_table().setRowCount(listSize)
        index = 0
        for _, item in self.listProduct.items():
            self.central_widget.get_table().setItem(index, 0, QTableWidgetItem(str(item.get_id())))
            self.central_widget.get_table().setItem(index, 1, QTableWidgetItem(item.get_name()))
            self.central_widget.get_table().setItem(index, 2, QTableWidgetItem(str(item.get_price())))
            self.central_widget.get_table().setItem(index, 3, QTableWidgetItem(str(item.get_quantity())))
            index = index + 1

    def add_to_cart(self):
        indexes = self.central_widget.get_table().selectionModel().selectedIndexes()
        id = indexes[0].sibling(indexes[0].row(), indexes[0].column()).data();
        name = indexes[1].sibling(indexes[1].row(), indexes[1].column()).data();
        price = indexes[2].sibling(indexes[2].row(), indexes[2].column()).data();
        # create product and add to cart
        pro = Item()
        pro.set_id(id)
        pro.set_name(name)
        pro.set_price(price)
        self.cart_list[pro.get_name()] = pro
        self.load_cart_table()

    def load_cart_table(self):
        listSize = len(self.cart_list)
        self.central_widget.get_cart_table().setRowCount(listSize)
        index = 0
        for _, prod in self.cart_list.items():
            self.quantity = QComboBox()
            count = self.listProduct[prod.get_name()].get_quantity()
            for i in range(1, count + 1):
                self.quantity.addItem(str(i))
            self.central_widget.get_cart_table().setItem(index, 0, QTableWidgetItem(str(prod.get_id())))
            self.central_widget.get_cart_table().setItem(index, 1, QTableWidgetItem(prod.get_name()))
            self.central_widget.get_cart_table().setItem(index, 2, QTableWidgetItem(str(prod.get_price())))
            self.central_widget.get_cart_table().setCellWidget(index, 3, self.quantity)
            index = index + 1

    def buy_items(self):
        index = 0
        while self.central_widget.get_cart_table().rowCount() > index:
            item_name = self.central_widget.get_cart_table().takeItem(index, 1).text()
            item_quantity = self.central_widget.get_cart_table().cellWidget(index, 3).currentText()
            self.cart_list[item_name].set_quantity(int(item_quantity))
            index += 1

        self.cart_model.buy(self.cart_list)
        self.cart_model.save_records(self.cart_list)
        total_price = self.cart_model.get_total_price(self.cart_list)
        self.cart_list = {}
        self.dialog = ShowDialog("information", f"Thanks for buying the total prices: {total_price}")

    def load_history(self):
        self.central_widget = self.main_view.centralWidget()
        self.listRecordProduct = self.cart_model.get_records_items()
        listSize = len(self.listRecordProduct)
        self.central_widget.get_history_table().setRowCount(listSize)
        index = 0
        for item in self.listRecordProduct:
            self.central_widget.get_history_table().setItem(index, 0, QTableWidgetItem(item["name"]))
            self.central_widget.get_history_table().setItem(index, 1, QTableWidgetItem(str(item["price"])))
            self.central_widget.get_history_table().setItem(index, 2, QTableWidgetItem(str(item["quantity"])))
            self.central_widget.get_history_table().setItem(index, 3, QTableWidgetItem(item["date"]))
            index = index + 1
