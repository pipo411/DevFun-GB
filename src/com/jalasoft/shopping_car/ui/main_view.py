from PyQt5.QtWidgets import QMainWindow, QMenu, QAction

from src.com.jalasoft.shopping_car.ui.product_insert_view import ProductInsertView
from src.com.jalasoft.shopping_car.ui.product_show_view import ProductShowView


class MainView(QMainWindow):

    def __init__(self):
        super().__init__()

    def initUI(self, controller):
        self.__controller = controller
        self.setWindowTitle("Test")
        self.initComponent()
        self.show()

    def initComponent(self):
        menuBar = self.menuBar()
        prodOption = menuBar.addMenu("Register")

        productMenu = QMenu("Product", self)
        prodOption.addMenu(productMenu)

        insertOption = QAction("Insert", self)
        productMenu.addAction(insertOption)
        showOption = QAction("Show", self)
        productMenu.addAction(showOption)

        insertOption.triggered.connect(lambda: self.loadProductInsertView())
        showOption.triggered.connect(lambda: self.loadProductShowView())

        story = menuBar.addMenu("Historial")
        storyMenu = QAction("Show hitorial", self)
        story.addAction(storyMenu)
        storyMenu.triggered.connect(lambda: self.loadHistorialView())


    def loadProductInsertView(self):
        self.setCentralWidget(ProductInsertView())
        self.__controller.addActionListener()

    def loadProductShowView(self):
        self.setCentralWidget(ProductShowView())
        self.__controller.loadProduct()
        self.__controller.addActionListener()

    def loadHistorialView(self):
        pass
        #self.setCentralWidget(HistoryShowView())
        #self.__controller.loadHistory()
        #self.__controller.addActionListener()

