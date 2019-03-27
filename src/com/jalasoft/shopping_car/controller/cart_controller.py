from PyQt5.QtWidgets import QTableWidgetItem, QLineEdit, QComboBox

from src.com.jalasoft.shopping_car.model.item import Item
from src.com.jalasoft.shopping_car.ui.product_insert_view import ProductInsertView
from src.com.jalasoft.shopping_car.ui.product_show_view import ProductShowView


class CartController:
    def __init__(self, mainView, cartModel):
        self.mainView = mainView
        self.cartModel = cartModel
        self.mainView.initUI(self)
        self.cartList = {}

    def addActionListener(self):
        self.centralWidget = self.mainView.centralWidget()
        if isinstance(self.centralWidget, ProductInsertView):
            self.centralWidget.getSaveProductButton().clicked.connect(lambda: self.actionProduct())
        if isinstance(self.centralWidget, ProductShowView):
            self.centralWidget.getAddTocartButton().clicked.connect(lambda: self.addToCart())
            self.centralWidget.getBuyButton().clicked.connect(lambda: self.buyItems())

    def actionProduct(self):
        if self.centralWidget.getMenu() == 'insert':
            self.saveProduct()
        elif self.centralWidget.getMenu() == 'edit':
            self.editProduct()
        elif self.centralWidget.getMenu() == 'delete':
            self.deleteProduct()

    def saveProduct(self):
        pro = Item()
        pro.set_name(self.centralWidget.getName())
        pro.set_price(float(self.centralWidget.getPrice()))
        pro.set_quantity(int(self.centralWidget.getQuantity()))
        self.cartModel.add_item(pro)

    def editProduct(self):
        self.cartModel.edit_item(str(self.centralWidget.getCurrentName()),
                                 str(self.centralWidget.getName()), float(self.centralWidget.getPrice()))

    def deleteProduct(self):
        self.cartModel.delete_product(str(self.centralWidget.getName()))

    def loadProduct(self):
        self.centralWidget = self.mainView.centralWidget()
        self.listProduct = self.cartModel.get_items()
        listSize = len(self.listProduct)
        self.centralWidget.getTable().setRowCount(listSize)
        index = 0
        for _, item in self.listProduct.items():
            self.centralWidget.getTable().setItem(index, 0, QTableWidgetItem(str(item.get_id())))
            self.centralWidget.getTable().setItem(index, 1, QTableWidgetItem(item.get_name()))
            self.centralWidget.getTable().setItem(index, 2, QTableWidgetItem(str(item.get_price())))
            self.centralWidget.getTable().setItem(index, 3, QTableWidgetItem(str(item.get_quantity())))
            index = index + 1

    def addToCart(self):
        indexes = self.centralWidget.getTable().selectionModel().selectedIndexes()
        id = indexes[0].sibling(indexes[0].row(), indexes[0].column()).data();
        name = indexes[1].sibling(indexes[1].row(), indexes[1].column()).data();
        price = indexes[2].sibling(indexes[2].row(), indexes[2].column()).data();
        # create product and add to cart
        pro = Item()
        pro.set_id(id)
        pro.set_name(name)
        pro.set_price(price)
        self.cartList[pro.get_name()] = pro
        self.loadCartTable()

    def loadCartTable(self):
        listSize = len(self.cartList)
        self.centralWidget.getCartTable().setRowCount(listSize)
        index = 0
        for _, prod in self.cartList.items():
            self.quantity = QComboBox()
            count = self.listProduct[prod.get_name()].get_quantity()
            for i in range(1, count + 1):
                self.quantity.addItem(str(i))
            self.centralWidget.getCartTable().setItem(index, 0, QTableWidgetItem(str(prod.get_id())))
            self.centralWidget.getCartTable().setItem(index, 1, QTableWidgetItem(prod.get_name()))
            self.centralWidget.getCartTable().setItem(index, 2, QTableWidgetItem(str(prod.get_price())))
            self.centralWidget.getCartTable().setCellWidget(index, 3, self.quantity)
            index = index + 1

    def buyItems(self):
        index = 0
        while self.centralWidget.getCartTable().rowCount() > index:
            item_name = self.centralWidget.getCartTable().takeItem(index, 1).text()
            item_quantity = self.centralWidget.getCartTable().cellWidget(index, 3).currentText()
            self.cartList[item_name].set_quantity(int(item_quantity))
            index += 1
        self.cartModel.buy(self.cartList)
        self.cartModel.save_sell(self.cartList)
        self.cartList = {}

    def load_history(self):
        self.centralWidget = self.mainView.centralWidget()
        self.listRecordProduct = self.cartModel.get_records_items()
        listSize = len(self.listRecordProduct)
        print(self.listRecordProduct)
        self.centralWidget.getHistoryTable().setRowCount(listSize)
        index = 0
        print(self.listRecordProduct)
        for item in self.listRecordProduct:
            self.centralWidget.getHistoryTable().setItem(index, 0, QTableWidgetItem(item["name"]))
            self.centralWidget.getHistoryTable().setItem(index, 1, QTableWidgetItem(str(item["price"])))
            self.centralWidget.getHistoryTable().setItem(index, 2, QTableWidgetItem(str(item["quantity"])))
            self.centralWidget.getHistoryTable().setItem(index, 3, QTableWidgetItem(item["date"]))
            index = index + 1
