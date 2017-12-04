# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento

class Rey(Comportamiento):

    def _puedeMoverA(self, columna, fila):
        if abs(self.fila - fila) == 1  and abs(self.columna - columna) == 1:
            # se mueve en diagonal:
            return True
        elif self.columna == columna and abs(self.fila - fila) == 1:
            return True
        if self.fila == fila and abs(self.columna - columna) == 1:
            return True
        else:
            return False
