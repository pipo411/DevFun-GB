from PyQt5.QtWidgets import QWidget, QVBoxLayout

from src.com.jalasoft.shopping_car.ui.table_template import TableTemplate


class HistoryShowView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vLayout = QVBoxLayout()

        self.HistoryTable = TableTemplate(["Product Name", "Price", "Quantity", "Date"], "Moccasin")

        vLayout.addWidget(self.HistoryTable)

        self.setLayout(vLayout)

    def getHistoryTable(self):
        return self.HistoryTable
