# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento

class Golem(Comportamiento):

    def _puedeMoverA(self, columna, fila):
        if self.fila == fila and self.columna+1 == columna:
            return True
        if self.fila+1 == fila and self.columna == columna:
            return True
        else:
            return False

    def puedeComerEn(self, celda):
        return self.fila-1 == celda.fila and abs(celda.columna-self.columna) == 1
