# Validation in a field in a table:
def INPUT(_name, requires):

INPUT(_name='a', requires=IS_INT_IN_RANGE(0, 10))
db.define_table('person', Field('name'))
db.persona.nombre.requires = IS_NOT_EMPTY()

# Multiple validators

db.persona.nombre.requires = [IS_NOT_EMPTY(),
                              IS_NOT_IN_DB(db, 'person.name')]

db.persona.nombre.validate(valor)

IS_NOT_EMPTY(error_message='Cannot be empty ')

# Validator verifies that the value of the field contains only characters in the ranges A-Z, A-Z, or 0-9.
requires = IS_ALPHANUMERIC(error_message='¡Must be alphanumeric!')
# Validator verifies that the value of the field contains a valid date

requires = IS_DATE(format=T('%Y-%m-%d'),
                   error_message='¡Must be  YYYY-MM-DD!')

# Allows you to specify a range

requires = IS_DATE_IN_RANGE(format=T('%Y-%m-%d'),
                            minimum=datetime.date(2008, 1, 1),
                            maximum=datetime.date(2009, 12, 31),
                            error_message='¡Must be  YYYY-MM-DD!')

# Decimal range
INPUT(_type='text', _name='name', requires=IS_DECIMAL_IN_RANGE(0, 10, dot="."))

# Check that the field has the current format for an email address

requires = IS_EMAIL(error_message='¡The Mail is invalid !')

# Verifies that the value of a field is a floating-point number in the specified range, 0 < = value < = 100

requires = IS_FLOAT_IN_RANGE(0, 100, dot=".",
                             error_message='¡Too small or too big !')

# Verifies that the field value is an integer in the defined range, 0 < = value < 100
requires = IS_INT_IN_RANGE(0, 100,
                           error_message='¡Too small or too big !')

# Verify that the text string has a length less than 33 characters:
INPUT(_type='text', _name='nombre', requires=IS_LENGTH(32))

# Validator verifies that the value of the field contains a valid time in the specified format

requires = IS_TIME(error_message='Must be  HH:MM:SS!')


class IS_DATE(object):
    def __init__(self, format='%Y-%m-%d', error_message='¡Must be  YYYY-MM-DD!'):
        self.format = format
        self.error_message = error_message

    def __call__(self, valor):
        try:
            y, m, d, hh, mm, ss, t0, t1, t2 = time.strptime(value, str(self.format))
            value = datetime.date(y, m, d)
            return (value, None)
        except:
            return (valor, self.error_message)

    def formatter(self, value):
        return value.strftime(str(self.format))

    # Validating that the user enters an integer
    def lee_entero():
        while True:
            input = raw_input("Write a whole number : ")
        try:
            input = int(Input)
            return Input
        except ValueError:
            print
            "Input is incorrect: write a whole number "
