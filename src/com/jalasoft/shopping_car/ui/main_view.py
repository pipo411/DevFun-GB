"""
Main window.
"""
from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5 import QtCore
from src.com.jalasoft.shopping_car.ui.history_show_view import HistoryShowView
from src.com.jalasoft.shopping_car.ui.product_insert_view import ProductInsertView
from src.com.jalasoft.shopping_car.ui.product_show_view import ProductShowView


class MainView(QMainWindow):
    """
    This class create the menu of the main window.
    """
    def __init__(self):
        """
        constructor
        """
        super().__init__()

    def initUI(self, controller):
        """
        Init
        :param controller:
        """
        self.__controller = controller
        self.setWindowTitle("Test")
        self.resize(1000, 600)
        self.init_component()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.show()

    def init_component(self):
        """
        Create the menu bar
        Product actions:
            add insert menu
            add edit menu
            add delete menu

        Store actions:
            add shopping cart menu
            add store menu

        History actions:
            add show history menu
        """
        self.load_product_insert_view()
        menu_bar = self.menuBar()
        prod_option = menu_bar.addMenu("Product")

        insert_menu = QAction("Insert", self)
        edit_menu = QAction("Edit", self)
        delete_menu = QAction("Delete", self)
        prod_option.addAction(insert_menu)
        prod_option.addAction(edit_menu)
        prod_option.addAction(delete_menu)

        store = menu_bar.addMenu("Store")
        shopping_cart = QAction("Shopping Cart", self)
        store.addAction(shopping_cart)


        insert_menu.triggered.connect(lambda: self.load_product_insert_view())
        edit_menu.triggered.connect(lambda: self.load_product_edit_view())
        delete_menu.triggered.connect(lambda: self.load_product_delete_view())

        shopping_cart.triggered.connect(lambda: self.load_product_show_view())

        story = menu_bar.addMenu("History")
        story_menu = QAction("Show History", self)
        story.addAction(story_menu)
        story_menu.triggered.connect(lambda: self.load_history_view())

    def load_product_insert_view(self):
        """
        function load ProductInsertView for insert option
        """
        self.setCentralWidget(ProductInsertView("insert"))
        self.__controller.add_action_listener()

    def load_product_edit_view(self):
        """
        function load ProductInsertView for edit option
        """
        self.setCentralWidget(ProductInsertView("edit"))
        self.__controller.add_action_listener()

    def load_product_delete_view(self):
        """
        function load ProductInsertView for delete option
        """
        self.setCentralWidget(ProductInsertView("delete"))
        self.__controller.add_action_listener()

    def load_product_show_view(self):
        """
        function load product show
        """
        self.setCentralWidget(ProductShowView())
        self.__controller.load_product()
        self.__controller.add_action_listener()

    def load_history_view(self):
        """
        function load history
        """
        self.setCentralWidget(HistoryShowView())
        self.__controller.load_history()

