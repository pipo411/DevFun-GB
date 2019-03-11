import datetime
import time

from pip._vendor.distlib.compat import raw_input


def read_int():
    while True:
        entry = raw_input("Write a whole number: ")
    try:
        entry = int(entry)
        return entry
    except ValueError:
        print
        "The entry is incorrect: write a whole number"


def is_int(var):
    try:
        int(var)
        return True
    except:
        return False


datos = ["123", "asd", "eeee", "----", "-5", ""]
for data in datos:
    print("¿'{}' it is a integer? {}".format(data, is_int(data)))


def is_float(var):
    try:
        float(var)
        return True
    except:
        return False


datos = ["123", "asd", "eeee", "----", "-5", "1.60"]
for data in datos:
    print("¿'{}' is a float? {}".format(data, is_float(data)))


# has exactly a point
def has_exactly_a_point(num):
    num = str(num)
    first_ind = num.find(".")
    if first_ind is -1:
        return False
    return first_ind is num.rfind(".")


pruebas = ["1.2", "1", "1.1.2", "500", "5.0"]
for data in pruebas:
    print("¿'{}' has exactly one point? {}".format(data, has_exactly_a_point(data)))


    # Validating the dates
    class IS_DATE(object):
        def __init__(self, format='%Y-%m-%d', error_message='¡Must be  YYYY-MM-DD!'):
            self.format = format
            self.error_message = error_message

        def __call__(self, value):
            try:
                y, m, d, hh, mm, ss, t0, t1, t2 = time.strptime(value, str(self.format))
                value = datetime.date(y, m, d)
                return (value, None)
            except:
                return (value, self.error_message)

        def formatter(self, value):
            return value.strftime(str(self.format))

        # Validating that the user enters an integer
        def lee_entero(self):
            while True:
                input = raw_input("Write a whole number : ")
            try:
                input = int(Input)
                return Input
            except ValueError:
                print
                "Input is incorrect: write a whole number "
