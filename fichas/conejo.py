# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento

class Conejo(Comportamiento):

    def puedeMoverA(self, columna, fila):
        if self.fila == fila and abs(self.columna - columna)%2 == 0:
            # se mueve en vertical:
            return True
        elif self.columna == columna and abs(self.fila - fila)%2 == 0:
            # se mueve en orizontal:
            return True
        else:
            return False
