# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento

class Dama(Comportamiento):

    def puedeMoverA(self, columna, fila):
        if self.fila == fila or self.columna == columna:
            # se mueve en vertical:
            return True
        elif abs(self.fila - fila) == abs(self.columna - columna):
            # se mueve en diagonal:
            return True
        else:
            return False
