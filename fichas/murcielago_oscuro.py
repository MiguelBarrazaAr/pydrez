# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento

class Murcielago_oscuro(Comportamiento):


    def puedeMoverA(self, columna, fila):
        if self.fila == fila and abs(self.columna - columna) <= 3:
            # se mueve en vertical:
            return True
        elif self.columna == columna and abs(self.fila - fila) <= 3:
            # se mueve en orizontal:
            return True
        elif abs(self.fila - fila) == abs(self.columna - columna) and abs(self.columna - columna) <= 3 and abs(self.fila - fila) <= 3:
            # se mueve en diagonal:
            return True
        else:
            return False