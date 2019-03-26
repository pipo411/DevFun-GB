from PyQt5.QtWidgets import QDialog, QMessageBox


class ShowDialog(QDialog):
    def __init__(self):
        super().__init__()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Item was adedd")


