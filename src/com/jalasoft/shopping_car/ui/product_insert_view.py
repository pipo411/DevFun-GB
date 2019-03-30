"""
This class create Product Insert window.
"""
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QVBoxLayout, QGroupBox

from src.com.jalasoft.shopping_car.ui.button_template import ButtonTemplate


class ProductInsertView(QWidget):
    """
    display the Product Insert menu.
    """
    def __init__(self, menu):
        super().__init__()
        self.menu = menu
        self.initUI(menu)

    def initUI(self, menu):
        """
        constructor
        :param menu: str menu
        """
        vLayout = QVBoxLayout()

        if menu == 'insert':
            group = self.insert_menu()
            button_message = "Save Product"
        elif menu == "edit":
            group = self.edit_menu()
            button_message = "Edit Product"
        elif menu == "delete":
            group = self.delete_menu()
            button_message = "Delete Product"

        self.save_button = ButtonTemplate(button_message, "palegoldenrod")

        vLayout.addWidget(group)
        vLayout.addWidget(self.save_button)
        self.setLayout(vLayout)

    def insert_menu(self):
        """
        insert menu UI components
        :return: QGroupBox() group
        """
        lbl_product = QLabel("Insert New Product")

        group = QGroupBox()
        form = QFormLayout()

        form.addRow(lbl_product)
        form.addRow(self.name_component(), self.name)
        form.addRow(self.price_component(), self.price)
        form.addRow(self.quantity_component(), self.quantity)

        group.setLayout(form)
        self.save_button = ButtonTemplate("Save Product", "palegoldenrod")

        return group

    def edit_menu(self):
        """
        function edit_menu
        :return: QGroupBox()
        """
        lbl_product = QLabel("Edit Product")

        group = QGroupBox()
        form = QFormLayout()

        form.addRow(lbl_product)
        form.addRow(self.name_actual_component(), self.actual_name)
        form.addRow(self.name_component(), self.name)
        form.addRow(self.price_component(), self.price)
        group.setLayout(form)
        return group

    def delete_menu(self):
        """
        function delete_menu
        :return: QGroupBox()
        """
        lbl_product = QLabel("Delete Product")

        group = QGroupBox()
        form = QFormLayout()

        form.addRow(lbl_product)
        form.addRow(self.name_component(), self.name)
        group.setLayout(form)
        return group

    def name_component(self):
        """
        function name_component
        :return: QLabel
        """
        lbl_name = QLabel("Name: ")
        self.name = QLineEdit()
        self.name.setPlaceholderText("Set the product name")
        return lbl_name

    def price_component(self):
        """
        function price_component
        :return: QLabel
        """
        lbl_price = QLabel("Price: ")
        self.price = QLineEdit()
        self.price.setPlaceholderText("Set the product price")
        return lbl_price

    def quantity_component(self):
        """
        function quantity_component
        :return: QLabel
        """
        lbl_quantity = QLabel("Quantity: ")
        self.quantity = QLineEdit()
        self.quantity.setPlaceholderText("Set the product Quantity")
        return lbl_quantity

    def name_actual_component(self):
        """
        function name_actual_component
        :return: QLabel
        """
        lbl_name = QLabel("Current Product Name: ")
        self.actual_name = QLineEdit()
        self.actual_name.setPlaceholderText("Set the actual product name")
        return lbl_name

    def get_save_product_button(self):
        """
        function return save_button
        :return: QpushButton
        """
        return self.save_button

    def get_name(self):
        """
        function return name
        :return:
        """
        return self.name.text()

    def get_current_name(self):
        """
        function
        :return:
        """
        return self.actual_name.text()

    def get_price(self):
        """

        :return:
        """
        return self.price.text()

    def get_quantity(self):
        """

        :return:
        """
        return self.quantity.text()

    def get_menu(self):
        """

        :return:
        """
        return self.menu
