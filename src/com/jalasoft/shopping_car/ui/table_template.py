from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget


class TableTemplate(QTableWidget):
    def __init__(self, horizontalHeaderLabels, colorHeader):
        super().__init__()
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(horizontalHeaderLabels)

        stylesheet = "::section{Background-color:" + colorHeader + ";border-radius:14px;}"
        self.horizontalHeader().setStyleSheet(stylesheet)

        self.format = self.horizontalHeader()
        self.format.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.format.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.format.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.format.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
