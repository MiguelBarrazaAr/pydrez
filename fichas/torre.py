# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento

class Torre(Comportamiento):

    def puedeMoverA(self, columna, fila):
        if self.fila == fila or self.columna == columna:
            return True
        else:
            return False
