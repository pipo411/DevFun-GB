import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    import unittest

    class PruebasMetodosCadenas(unittest.TestCase):

        def validate_name(self):
            self.assertEqual('hola'.upper(), 'HOLA')

        def validate_form(self):
            self.assertTrue('HOLA'.isupper())
            self.assertFalse('Hola'.isupper())

        def nickname(self):
            s = 'Hola mundo'
            self.assertEqual(s.split(), ['Hola', 'mundo'])

    if __name__ == '__main__':
        unittest.main()


if __name__ == '__main__':
    unittest.main()

