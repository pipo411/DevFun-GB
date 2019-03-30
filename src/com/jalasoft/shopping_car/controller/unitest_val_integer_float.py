import unittest

# Verify that is Number
class checkNumber(unittest.TestCase):

     def test_int_float(self):
        self.assertEqual(1,1.0)
    # END is test_int_float

# END ChekNumber

if __name__ == '__main__':
    unittest.main()
#ENDIF
