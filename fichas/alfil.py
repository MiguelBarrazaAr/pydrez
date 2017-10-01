# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento

class Alfil(Comportamiento):

    def puedeMoverA(self, columna, fila):
        if abs(self.fila - fila) == abs(self.columna - columna):
            lista1 = range(min(self.columna, columna)+1, max(self.columna, columna))
            lista2 = range(min(self.fila, fila)+1, max(self.fila, fila))
            return self.validar_celdas(zip(lista1, lista2))
        else:
            return False
