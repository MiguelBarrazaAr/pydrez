# -*- encoding: utf-8 -*-

from .tuple import tupleToString, stringToTuple

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

    def agregar(self, posicion, ficha):
        self.celdas[tupleToString(posicion)] = ficha

    def eliminar(self, posicion):
        del self.celdas[tupleToString(posicion)]

    def valor(self, posicion):
        return self.celdas.get(tupleToString(posicion))

    def celdasActivas(self):
        return self.celdas.keys()

    def estaLibre(self, posicion):
        return self.valor(posicion) is None
