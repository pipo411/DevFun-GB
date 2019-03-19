from PyQt5.QtWidgets import QDialog, QFormLayout, QPushButton, QLineEdit, QLabel

class AddItem(QDialog):
    def __init__(self, *args, **kwargs):
        super(AddItem, self).__init__(*args, **kwargs)
        self.setWindowTitle("Add Item")
        self.setFixedSize(200, 100)
        self.initUI_addItem()

    def initUI_addItem(self):
        layout = QFormLayout()
        btn_add = QPushButton("ADD")
        btn_add.clicked.connect(lambda: self.add_item_table())
        line_item_name = QLineEdit()
        line_item_price = QLineEdit()
        layout.addRow(QLabel("Item Name: "), line_item_name)
        layout.addRow(QLabel("Item Price: "), line_item_price)
        layout.addRow(btn_add)
        self.setLayout(layout)

    def add_item_table(self):
        print("Item added")