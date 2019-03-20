from PyQt5.QtWidgets import QTableWidgetItem, QLineEdit

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
            self.centralWidget.getSaveProductButton().clicked.connect(lambda: self.saveProduct())
        if isinstance(self.centralWidget, ProductShowView):
            self.centralWidget.getAddTocartButton().clicked.connect(lambda: self.addToCart())
            # self.centralWidget.getBuyButton().clicked().connect(lambda: self.buyItems())

    def saveProduct(self):
        pro = Item()
        pro.set_name(self.centralWidget.getName())
        pro.set_price(self.centralWidget.getPrice())
        pro.set_quantity(self.centralWidget.getQuantity())
        self.cartModel.add_item(pro)

    def loadProduct(self):
        self.centralWidget = self.mainView.centralWidget()
        listProduct = self.cartModel.get_items()
        listSize = len(listProduct)
        self.centralWidget.getTable().setRowCount(listSize)
        index = 0
        for _, item in listProduct.items():
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
            quantity = QLineEdit()
            self.centralWidget.getCartTable().setItem(index, 0, QTableWidgetItem(str(prod.get_id())))
            self.centralWidget.getCartTable().setItem(index, 1, QTableWidgetItem(prod.get_name()))
            self.centralWidget.getCartTable().setItem(index, 2, QTableWidgetItem(str(prod.get_price())))
            self.centralWidget.getCartTable().setCellWidget(index, 3, quantity)
            index = index + 1
        if listSize > 4:
            self.cartModel.buy(self.cartList)

    def buyItems(self):
        self.cartModel.buy(self.cartList)
