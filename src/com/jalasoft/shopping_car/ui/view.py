from PyQt5.QtWidgets import QMainWindow, QMenu, QWidget, QFormLayout, QLabel, QLineEdit


class ProductView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        form = QFormLayout()
        form.addRow(QLabel('name'),QLineEdit())
        self.setLayout(form)
        #espaciadores

class View(QMainWindow):
    def __init__(self):
        super().__init__()
        print("view")

    def init_UI(self):  #fondo, size van aqui
        self.setWindowTitle("test")
        self.__initComponent()
        self.show()

    def __initComponent(self):
        menu_bar = self.menuBar()
        product =  menu_bar.addMenu('Product')
        insert = QMenu('Insert', self)
        product.addMenu(insert)
        self.setCentralWidget(self.__getProductView())

    def __getProductView(self):
        proView = ProductView()
        return proView
