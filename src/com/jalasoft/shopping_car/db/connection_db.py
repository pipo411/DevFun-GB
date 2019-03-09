import sqlite3

from pylint.test.input.func_w0612 import OS


class ConnectionDB:


    dataBaseName = "ShoppingCar"
    def __init__(self):
        self.exist = OS.path.exits(self.dataBaseName)

    def getConnection(self):
        """

        :return:
        """
        con = sqlite3.connect(self.dataBaseName)
        if not self.exist:
            cu = con.cursor()
            cu.execute('''CREATE TABLE productos
                           (idProduct integer PRIMARY KEY AUTOINCREMENT,
                            Name varchar(200),
                            Cantidad integer)
                            CREATE TABLE venta
                            (idVenta integer,
                            idProduct integer,
                            total integer)
                            CREATE TABLE item
                            (idItem integer,
                            idVenta integer)''')
            return con

    #GUARDAR CAMBIOS
        # con.commit()
