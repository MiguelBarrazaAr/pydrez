# -*- encoding: utf-8 -*-

from .tuple import tupleToString, stringToTuple

class Tablero(object):
    """Representa al tablero"""

    def __init__(self, columnas, filas, tipo):
        """:param columnas: cantidad de columnas que tendra el tablero.
        :type columnas: int
        :param filas: cantidad de filas
        :type filas: int
        """
        self.celdas = {}
        self._f = filas
        self._c  = columnas

    @property
    def columnas(self):
        return self._c

    @property
    def filas(self):
        return self._f

    def agregar(self, posicion, ficha):
        self.celdas[tupleToString(posicion)] = ficha

    def eliminar(self, posicion):
        del self.celdas[tupleToString(posicion)]

    def obtener(self, posicion):
        if (posicion[0] < 0 or posicion[0] >= self._c) and (posicion[1] < 0 or posicion[1] >= self._f):
            raise Exception("posicion inexistente")
        else:
            return self.celdas.get(tupleToString(posicion))

    def celdasActivas(self):
        return self.celdas.keys()

    def estaLibre(self, posicion):
        return self.obtener(posicion) is None
