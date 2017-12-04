# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento

class Hipogrifo(Comportamiento):

    def _puedeMoverA(self, columna, fila):
        if abs(self.fila - fila) == abs(self.columna - columna) and abs(self.columna - columna) <= 5 and abs(self.fila - fila) <= 5:
            # se mueve en diagonal:
            return True
        else:
            return False