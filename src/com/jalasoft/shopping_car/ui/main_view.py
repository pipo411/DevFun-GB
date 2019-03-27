from PyQt5.QtWidgets import QMainWindow, QMenu, QAction

from src.com.jalasoft.shopping_car.ui.history_show_view import HistoryShowView
from src.com.jalasoft.shopping_car.ui.product_insert_view import ProductInsertView
from src.com.jalasoft.shopping_car.ui.product_show_view import ProductShowView


class MainView(QMainWindow):

    def __init__(self):
        super().__init__()

    def initUI(self, controller):
        self.__controller = controller
        self.setWindowTitle("Test")
        self.resize(1000, 600)
        self.initComponent()
        self.show()

    def initComponent(self):
        menuBar = self.menuBar()
        prodOption = menuBar.addMenu("Product")

        insertMenu = QAction("Insert", self)
        editMenu = QAction("Edit", self)
        deleteMenu = QAction("Delete", self)
        prodOption.addAction(insertMenu)
        prodOption.addAction(editMenu)
        prodOption.addAction(deleteMenu)

        store = menuBar.addMenu("Store")
        shoppingCart = QAction("Shopping Cart", self)
        store.addAction(shoppingCart)

        insertMenu.triggered.connect(lambda: self.loadProductInsertView())
        editMenu.triggered.connect(lambda: self.loadProductEditView())
        deleteMenu.triggered.connect(lambda: self.loadProductDeleteView())

        shoppingCart.triggered.connect(lambda: self.loadProductShowView())

        story = menuBar.addMenu("History")
        storyMenu = QAction("Show History", self)
        story.addAction(storyMenu)
        storyMenu.triggered.connect(lambda: self.loadHistoryView())

    def loadProductInsertView(self):
        self.setCentralWidget(ProductInsertView("insert"))
        self.__controller.addActionListener()

    def loadProductEditView(self):
        self.setCentralWidget(ProductInsertView("edit"))
        self.__controller.addActionListener()

    def loadProductDeleteView(self):
        self.setCentralWidget(ProductInsertView("delete"))
        self.__controller.addActionListener()

    def loadProductShowView(self):
        self.setCentralWidget(ProductShowView())
        self.__controller.loadProduct()
        self.__controller.addActionListener()

    def loadHistoryView(self):
        self.setCentralWidget(HistoryShowView())
        self.__controller.load_history()
        # self.__controller.addActionListener()
