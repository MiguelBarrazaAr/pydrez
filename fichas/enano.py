# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento

class Enano(Comportamiento):

    def _puedeMoverA(self, columna, fila):
        """puede mover un paso hacia cualquier lado."""
        if abs(self.fila - fila) == 1  and abs(self.columna - columna) == 1:
            # se mueve en diagonal:
            return True
        elif self.columna == columna and abs(self.fila - fila) == 1:
            return True
        if self.fila == fila and abs(self.columna - columna) == 1:
            return True
        else:
            return False

    def puedeComerEn(self, celda):
        """Solo come en diagonal"""
        return abs(self.fila - celda.fila) == 1  and abs(self.columna - celda.columna) == 1
