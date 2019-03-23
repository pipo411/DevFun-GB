from PyQt5.QtWidgets import QPushButton


class ButtonTemplate(QPushButton):
    def __init__(self, name, color):
        super().__init__()
        stl = """QPushButton {
            background-color: """+color+""";
            border-width: 2px;
            border-color: darkkhaki;
            border-style: solid;
            border-radius: 10px;
            padding: 3px;
            min-width: 9ex;
            min-height: 2.5ex;
            font: bold 14px;
        }"""
        self.setText(name)
        self.setStyleSheet(stl)
        self.accessibleName()

#CSS revisar over
#https://www.yourhtmlsource.com/stylesheets/namedcolours.html