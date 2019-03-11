
from src.com.jalasoft.shopping_car.controller.controller import Controller
from src.com.jalasoft.shopping_car.model.model import Model
from src.com.jalasoft.shopping_car.ui.view import View

if __name__=="__main__":
    view = View()
    model = Model()
    controller = Controller (view,model)

