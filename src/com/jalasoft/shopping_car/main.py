import sys

from PyQt5.QtWidgets import QApplication

from src.com.jalasoft.shopping_car.controller.cart_controller import CartController
from src.com.jalasoft.shopping_car.model.shopping_car import Shoppingcar
from src.com.jalasoft.shopping_car.ui.main_view import MainView

if __name__=="__main__":
    app = QApplication(sys.argv)
    view = MainView()
    model = Shoppingcar()
    controller = CartController(view, model)
    sys.exit(app.exec_())

