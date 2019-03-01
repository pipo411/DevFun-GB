from controller.controller import Controller
from model.model import Model
from view.view import View

if __name__ == '__main__':
    view = View()
    model = Model()
    controller = Controller(view, model)

