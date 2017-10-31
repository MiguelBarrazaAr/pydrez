# -*- encoding: utf-8 -*-

class Ficha(object):

    def __init__(self, bando, posicion=(0,0)):
        self.nombre = self.__class__.__name__.lower()
        self.saltadora = False
        self.bando = bando
        self.posicion = posicion

    def valor(self):
        """valor que tiene la ficha"""
        return 3

    @property
    def columna(self):
        return self.posicion[0]

    @property
    def fila(self):
        return self.posicion[1]

    def puedeMoverA(self, posicion, tablero):
        """Verifica si la pieza puede llegar a la columna y fila indicada.
        este metodo se debe sobreescribir."""
        return False

    def validar_celdas(self, celdas, tablero):
        """valida una lista de tupla (columna, fila) de celdas que esten libre.
        metodo que se utiliza por las no salteadoras."""
        libre = True
        for x in celdas:
            pass#libre = libre and self.ficha.tablero.obtener_celda(x[0], x[1]).estaLibre()

        return libre
