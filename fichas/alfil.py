# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento

class Alfil(Comportamiento):

    def puedeMoverA(self, columna, fila):
        if abs(self.fila - fila) == abs(self.columna - columna):
            return True
        else:
            return False
