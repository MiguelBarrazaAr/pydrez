# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento

class Alfil(Comportamiento):

    def _puedeMoverA(self, columna, fila):
        if abs(self.fila - fila) == abs(self.columna - columna):
            # mueve en diagonal:
            lista1 = range(min(self.columna, columna)+1, max(self.columna, columna))
            lista2 = range(min(self.fila, fila)+1, max(self.fila, fila))
            if self.columna > columna:
                lista1.reverse()
            if self.fila > fila:
                lista2.reverse()

            return self.validar_celdas(zip(lista1, lista2))
        else:
            return False
