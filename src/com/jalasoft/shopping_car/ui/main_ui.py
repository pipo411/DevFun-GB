import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QWidget, QLineEdit, QPushButton


class main_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.widget = QWidget(self)

        self.btn_Add_Item = QPushButton("Add Item", self)

        self.btn_plu_quantity = QPushButton("+", self)
        self.btn_min_quantity = QPushButton("-", self)
        self.number_quantity = QLineEdit()

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.btn_Add_Item,0,0)
        #recuperar los items para crear sus entradas
        self.layout.addWidget(self.btn_plu_quantity, 2, 1,1,2)
        self.layout.addWidget(self.number_quantity, 2, 2,1,2)
        self.layout.addWidget(self.btn_min_quantity, 2, 3,1,2)

#el UI de los item s deberia ser una clase

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main_window()
    window.resize(720, 500)
    window.show()
    sys.exit(app.exec_())