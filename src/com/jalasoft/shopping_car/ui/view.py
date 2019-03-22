
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTableWidget, \
    QTableWidgetItem, QPushButton,  QAction

from src.com.jalasoft.shopping_car.ui.add_item import AddItem
from src.com.jalasoft.shopping_car.ui.shopping_car import Shopping_car


class ProductView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vLayout = QVBoxLayout()
        table = QTableWidget()
        row=4  #equal to table rows
        table.setColumnCount(3)
        table.setRowCount(row)
        for add_row in range(row):
            check_item = QTableWidgetItem()
            check_item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            check_item.setCheckState(QtCore.Qt.Unchecked)

            table.setHorizontalHeaderLabels(["Check", "Name ","Price"])
            table.setItem(add_row, 0, check_item)
            table.setItem(add_row, 1, QTableWidgetItem("getItemName["+str(add_row)+"]"))
            table.setItem(add_row, 2, QTableWidgetItem("getItemPrice["+str(add_row)+"]"))


        add_button = QPushButton("Add to car")
        add_button.clicked.connect(lambda: self.shopping_car_dialog())
        vLayout.addWidget(table)
        vLayout.addWidget(add_button)
        self.setLayout(vLayout)
        #

    def shopping_car_dialog(self):
        #enviar la lista de compras , los q estan check
        dialog = Shopping_car(self)
        dialog.show()

class View(QMainWindow):
    def __init__(self):
        super().__init__()
        print("view")

    def init_UI(self):
        self.setWindowTitle("test")
        self.__initComponent()
        self.show()

    def __initComponent(self):
        menu_bar = self.menuBar()
        product =  menu_bar.addMenu('Product')
        action = QAction("Add Item", self)
        product.addAction(action)
        action.triggered.connect(lambda: self.add_item_dialog())
        self.setCentralWidget(self.__getProductView())

    def add_item_dialog(self):
        dialog = AddItem(self)
        dialog.show()

    def __getProductView(self):
        proView = ProductView()
        return proView

