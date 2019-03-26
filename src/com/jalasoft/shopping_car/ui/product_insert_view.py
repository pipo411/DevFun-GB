from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox, QPushButton

from src.com.jalasoft.shopping_car.ui.button_template import ButtonTemplate


class ProductInsertView(QWidget):

    def __init__(self, menu):
        super().__init__()
        self.initUI(menu)

    def initUI(self, menu):
        vLayout = QVBoxLayout()

        self.core_product_menu = {"insert": self.insertMenu(), "edit": self.editMenu(), "delete": self.deleteMenu()}
        group = self.core_product_menu[menu]
        # group = QGroupBox()
        # form = QFormLayout()
        #
        # form.addRow(lblProduct)
        # form.addRow(self.nameComponent(), self.name)
        # form.addRow(self.priceComponent(), self.price)
        # form.addRow(self.quantityComponent(), self.quantity)
        # group.setLayout(form)

        self.saveButton = ButtonTemplate("Save Product", "palegoldenrod")

        vLayout.addWidget(group)
        vLayout.addWidget(self.saveButton)
        self.setLayout(vLayout)

    def insertMenu(self):
        lblProduct = QLabel("Insert Product")

        group = QGroupBox()
        form = QFormLayout()

        form.addRow(lblProduct)
        form.addRow(self.nameComponent(), self.name)
        form.addRow(self.priceComponent(), self.price)
        form.addRow(self.quantityComponent(), self.quantity)
        group.setLayout(form)
        return group

    def editMenu(self):
        lblProduct = QLabel("Edit Product")

        group = QGroupBox()
        form = QFormLayout()

        form.addRow(lblProduct)
        form.addRow(self.nameComponent(), self.name)
        form.addRow(self.priceComponent(), self.price)
        group.setLayout(form)
        return group

    def deleteMenu(self):
        lblProduct = QLabel("Delete Product")

        group = QGroupBox()
        form = QFormLayout()

        form.addRow(lblProduct)
        form.addRow(self.nameComponent(), self.name)
        group.setLayout(form)
        return group

    def nameComponent(self):
        lblName = QLabel("Name: ")
        self.name = QLineEdit()
        self.name.setPlaceholderText("Set the product name")
        return lblName

    def priceComponent(self):
        lblPrice = QLabel("Price: ")
        self.price = QLineEdit()
        self.price.setPlaceholderText("Set the product price")
        return lblPrice

    def quantityComponent(self):
        lblQuantity = QLabel("Quantity: ")
        self.quantity = QLineEdit()
        self.quantity.setPlaceholderText("Set the product Quantity")
        return lblQuantity

    def getSaveProductButton(self):
        return self.saveButton

    def getName(self):
        return self.name.text()

    def getPrice(self):
        return self.price.text()

    def getQuantity(self):
        return self.quantity.text()
   