from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox, QPushButton, QComboBox, \
    QTableWidget, QTableWidgetItem, QAbstractItemView

from src.com.jalasoft.shopping_car.ui.button_template import ButtonTemplate
from src.com.jalasoft.shopping_car.ui.table_template import TableTemplate


class ProductShowView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.initComponent()

    def initComponent(self):
        vLayout = QVBoxLayout()

        self.table = TableTemplate(["ID", "Product Name", "Price", "Quantity"], "Steelblue")
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.addButton = ButtonTemplate("Add to Cart", """palegoldenrod""")
        # self.addBuyButton = QPushButton("Buy Items", self)
        self.addBuyButton = ButtonTemplate("Buy Items", """Limegreen""")

        self.cartTable = TableTemplate(["ID", "Product Name", "Unit Price", "Total Price", "Quantity"], "Forestgreen")

        vLayout.addWidget(self.table)
        vLayout.addWidget(self.addButton)
        vLayout.addWidget(self.cartTable)
        vLayout.addWidget(self.addBuyButton)

        self.setLayout(vLayout)

    def getTable(self):
        return self.table

    def getCartTable(self):
        return self.cartTable

    def getAddTocartButton(self):
        return self.addButton

    def getBuyButton(self):
        return self.addBuyButton
