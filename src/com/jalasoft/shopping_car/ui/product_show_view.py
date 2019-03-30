"""
This class add the QtWidgets for the store and the car.
"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QAbstractItemView

from src.com.jalasoft.shopping_car.ui.button_template import ButtonTemplate
from src.com.jalasoft.shopping_car.ui.table_template import TableTemplate


class ProductShowView(QWidget):
    """
    class displays the  items  of the store
    """
    def __init__(self):
        """
        constructor
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Start the components
        """
        self.init_component()

    def init_component(self):
        """
        Add the components
        """
        vLayout = QVBoxLayout()

        self.table = TableTemplate(["ID", "Product Name", "Price", "Quantity"], "Skyblue")
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.add_button = ButtonTemplate("Add to Cart", """palegoldenrod""")
        # self.addBuyButton = QPushButton("Buy Items", self)
        self.add_buy_button = ButtonTemplate("Buy Items", """Limegreen""")


        self.cart_table = TableTemplate(["ID", "Product Name", "Unit Price", "Total Price", "Quantity"], "Lightgreen")

        vLayout.addWidget(self.table)
        vLayout.addWidget(self.add_button)
        vLayout.addWidget(self.cart_table)
        vLayout.addWidget(self.add_buy_button)

        self.setLayout(vLayout)

    def get_table(self):
        """
        get table of the store
        :return: table table
        """
        return self.table

    def get_cart_table(self):
        """
        get the table of the shopping car
        :return: table cart_table
        """
        return self.cart_table

    def get_add_tocart_button(self):
        """
        get the button  for add to shopping car
        :return: button add_button
        """
        return self.add_button

    def get_buy_button(self):
        """
        get the button for buy
        :return:button add_buy_button
        """
        return self.add_buy_button
