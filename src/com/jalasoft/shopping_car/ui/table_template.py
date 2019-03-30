"""
This class is a template for all the tables
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget


class TableTemplate(QTableWidget):
    """
    class template for the tables
    """
    def __init__(self, horizontal_header_labels, color_header):
        """
        constructor
        """
        super().__init__()
        self.setColumnCount(len(horizontal_header_labels))
        self.setHorizontalHeaderLabels(horizontal_header_labels)

        stylesheet = "::section{Background-color:" + color_header + ";border-radius:14px;}"
        self.horizontalHeader().setStyleSheet(stylesheet)

        self.format = self.horizontalHeader()
        self.format.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.format.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.format.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.format.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
