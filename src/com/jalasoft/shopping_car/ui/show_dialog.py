"""
This class create the window message.
"""
from PyQt5.QtWidgets import QDialog, QMessageBox

class ShowDialog(QDialog):
    def __init__(self, type, message):
        """
        Start
        :param type: str
        :param message: str
        """
        super().__init__()
        if type == "warning":
            QMessageBox.warning(self, 'Warning', message)
        elif type == "information":
            QMessageBox.information(self, 'Message', message)



