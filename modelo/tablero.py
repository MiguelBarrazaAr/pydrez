# -*- encoding: utf-8 -*-

class Tablero(object):
    """Representa al tablero"""

    def __init__(self, columnas=8, filas=8):
        """:param columnas: cantidad de columnas que tendra el tablero.
        :type columnas: int
        :param filas: cantidad de filas
        :type filas: int
        """
        self.celdas = {}
        self.filas = filas
        self.columnas = columnas

    def agregar(self, columna, fila, ficha):
        self.celdas[str(columna)+"."+str(fila)] = ficha

    def eliminar(self, columna, fila):
        del self.celdas[str(columna)+"."+str(fila)]

    def valor(self, columna, fila):
        return self.celdas.get(str(columna)+"."+str(fila))

    def celdasActivas(self):
        return self.celdas.keys()

    def estaLibre(self, columna, fila):
        return self.valor(columna, fila) is None
