"""
This class create the window for the history table.
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout

from src.com.jalasoft.shopping_car.ui.table_template import TableTemplate


class HistoryShowView(QWidget):
    """
    Class create the history table window
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        history table UI
        """
        vLayout = QVBoxLayout()

        self.history_table = TableTemplate(["Product Name", "Price", "Quantity", "Date"], "Moccasin")

        vLayout.addWidget(self.history_table)

        self.setLayout(vLayout)

    def get_history_table(self):
        """
        function return history_table
        :return:   history_table  QTableWidget
        """
        return self.history_table
