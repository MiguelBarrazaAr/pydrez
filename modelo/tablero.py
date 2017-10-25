# -*- encoding: utf-8 -*-

class Tablero(object):
    """Representa al tablero"""

    def __init__(self, columnas=8, filas=8):
        """:param columnas: cantidad de columnas que tendra el tablero.
        :type columnas: int
        :param filas: cantidad de filas
        :type filas: int
        """
        self.escaques = [([None]*columnas)]*filas
        self.filas = filas
        self.columnas = columnas
