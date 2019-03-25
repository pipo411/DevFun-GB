import sys, re
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic


class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("validation.ui", self)
        self.nombre.textChanged.connect(self.validate_name)
        self.price.textChanged.connect(self.validate_price)
        self.boton.clicked.connect(self.validate_form)

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

    def validate_form(self):
        if self.validar_nombre() and self.validar_price():
            QMessageBox.information(self, "Correct Form", "Correct Validation", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Incorrect Form", "Incorrect Validation", QMessageBox.Discard)

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


def clave(name):
    validate = False  # That they will meet the requirements one by one.
    long = len(name)  # Calculates the length of the name
    space = False  # Variable to identify spaces
    capital = False  # Variable to identify uppercase letters
    minuscula = False  # Variable to count identify lowercase letters
    number = False  # Variable to count identify lowercase letters
    y = name.isalnum()  # If alphanumeric returns True
    correct = True  # Verify that there are uppercase, Minuscula, numbers and non-alphanumeric

    for carac in name:  # For cycle that runs through character the name

        if carac.isspace() == True:  # Know If the character is a space
            space = True  # If you find a space you change the value user

        if carac.isupper() == True:  # Know if there is uppercase
            capital = True  # Accumulator or Capital Count

        if carac.islower() == True:  # Know if there are lowercase
            minuscula = True  # Accumulator or lowercase counter

        if carac.isdigit() == True:  # Know if there are numbers
            numeros = True  # Accumulator or Count of numbers

    if space == True:  # There are blank spaces
        print("The name can not contain spaces")
    else:
        validate = True  # The first requirement that there are no spaces

    if long < 8 and validate == True:
        print("Minimum 8 characters")
        validate = False  # Changes to Flase if the minimum character requirement is not met

    if capital == True and minuscula == True and number == True and y == False and validate == True:
        validate = True  # Changes to Flase if the minimum character requirement is not met
    else:
        correct = False  # One or more requirements for uppercase, minuscula, numerals and non-alphanumerics are not fulfilled

    if validate == True and correct == True:
        return True


app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic


class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("combobox.ui", self)
        self.boton.clicked.connect(self.getItem)

        # Add ne item item
        # self.lenguajes.addItem("C++")

        # Deleteun a item
        # self.lenguajes.removeItem(0)

    def getItem(self):
        item = self.lenguajes.currentText()
        self.labelLenguajes.setText("Has seleccionado: " + item)


app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()