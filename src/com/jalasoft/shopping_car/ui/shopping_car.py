from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QTableWidget, QVBoxLayout, QPushButton
from PyQt5 import QtCore

class Shopping_car(QDialog):
    def __init__(self, *args, **kwargs):
        super(Shopping_car, self).__init__(*args, **kwargs)
        self.setWindowTitle("Shopping Car")
        self.setFixedSize(400, 200)
        self.initUI_car()

    def initUI_car(self):
        vLayout = QVBoxLayout()

        table = QTableWidget()
        row=2  #equal to table rows
        table.setColumnCount(6)
        table.setRowCount(row)
        for add_row in range(row):
            check_item = QTableWidgetItem()
            check_item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            check_item.setCheckState(QtCore.Qt.Checked)
            btn_plus = QPushButton("+")
            btn_plus.clicked.connect(lambda: self.add_amount())
            btn_minus = QPushButton("-")
            btn_minus.clicked.connect(lambda: self.subtract_amount())
            table.setHorizontalHeaderLabels(["Check", "Name ","Price","quantity","+","-"])
            table.setItem(add_row, 0, check_item)
            table.setItem(add_row, 1, QTableWidgetItem("getItemName"))
            table.setItem(add_row, 2, QTableWidgetItem("getItemPrice"))
            table.setItem(add_row, 3, QTableWidgetItem("getcurrentquantity"))
            table.setCellWidget(add_row, 4, btn_plus)
            table.setCellWidget(add_row, 5, btn_minus)
        #
        buy_button = QPushButton("Buy")
        vLayout.addWidget(table)
        vLayout.addWidget(buy_button)
        self.setLayout(vLayout)

    def add_amount(self):
        print("add to quantity")

    def subtract_amount(self):
        print("subtract to quantity")