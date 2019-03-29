import re

from PyQt5 import uic
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QDialog, QMessageBox


class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.nombre.textChanged.connect(self.validate_name)
        self.price.textChanged.connect(self.validate_price)
        self.boton.clicked.connect(self.validate_form)

    @staticmethod
    def validate_name(self):
        name = self.name.text()
        validate = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', name, re.I)
        if name == "":
            self.nombre.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validate:
            self.name.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.name.setStyleSheet("border: 1px solid green;")
            return True

    @staticmethod
    def validate_form(self):
        if self.validar_nombre() and self.validar_price():
            QMessageBox.information(self, "Correct Form", "Correct Validation", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Incorrect Form", "Incorrect Validation", QMessageBox.Discard)

    @staticmethod
    def nickname(name):

        long = len(name)  # Calculate the length of the user name
        y = name.isalnum()  # Calculates that the string contains alphanumeric values

        if y == False:  # String contains non-alphanumeric values
            print("The user name can contain only letters and numbers ")

        if long < 6:
            print("The user name must contain at least 6 characters ")

        if long > 12:
            print("User name cannot contain more than 12 characters ")

        if long > 5 and long < 13 and y == True:
            return True  # True If the size is greater than 5 and less than 13

        def validatorChanged(self, index):
            if index == 0:
                self.validatorLineEdit.setValidator(0)
            elif index == 1:
                self.validatorLineEdit.setValidator(QIntValidator(self.validatorLineEdit))
            elif index == 2:
                self.validatorLineEdit.setValidator(QDoubleValidator(-999.0, 999.0, 2, self.validatorLineEdit))

            self.validatorLineEdit.clear()