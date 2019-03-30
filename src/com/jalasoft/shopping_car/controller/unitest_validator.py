import unittest

from PyQt5.QtGui import QDoubleValidator

# Validator for Line Edit
class Dialogo(unittest.TestCase):

    def validate_name(self):
        self.assertEqual('hola'.upper(), 'HOLA')

    def validate_form(self):
        self.assertTrue('HOLA'.isupper())
        self.assertFalse('Hola'.isupper())

    def nickname(name, self):
        self.validatorLineEdit.setValidator(QDoubleValidator(-999.0, 999.0, 2, self.validatorLineEdit))


if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
