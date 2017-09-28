# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento

class Caballo(Comportamiento):

    def puedeMoverA(self, columna, fila):
        if abs(self.columna-columna) == 2 and abs(self.fila-fila) == 1:
            return True
        elif abs(self.columna-columna) == 1 and abs(self.fila-fila) == 2:
            return True
        else:
            return False
