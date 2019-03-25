from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox, QPushButton

from src.com.jalasoft.shopping_car.ui.button_template import ButtonTemplate


class ProductInsertView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vLayout = QVBoxLayout()
        lblProduct = QLabel("Insert New Product")
        lblName = QLabel("Name: ")
        self.name = QLineEdit()
        self.name.setPlaceholderText("Set the product name")

        lblPrice = QLabel("Price: ")
        self.price = QLineEdit()
        self.price.setPlaceholderText("Set the product price")

        lblQuantity = QLabel("Quantity: ")
        self.quantity = QLineEdit()
        self.quantity.setPlaceholderText("Set the product Quantity")

        group = QGroupBox()
        form = QFormLayout()

        form.addRow(lblProduct)
        form.addRow(lblName, self.name)
        form.addRow(lblPrice, self.price)
        form.addRow(lblQuantity, self.quantity)
        group.setLayout(form)

        self.saveButton = ButtonTemplate("Save Product", "palegoldenrod")

        vLayout.addWidget(group)
        vLayout.addWidget(self.saveButton)
        self.setLayout(vLayout)

    def getSaveProductButton(self):
        return self.saveButton

    def getName(self):
        return self.name.text()

    def getPrice(self):
        return self.price.text()

    def getQuantity(self):
        return self.quantity.text()
