# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento

class Dama(Comportamiento):

    def puedeMoverA(self, columna, fila):
        if self.fila == fila:
            # se mueve en vertical:
            return self.validar_celdas(map((lambda x: (x, fila)), range(min(self.columna, columna)+1, max(self.columna, columna))))
        elif self.columna == columna:
            # se mueve en orizontal:
            return self.validar_celdas(map((lambda x: (columna, x)), range(min(self.fila, fila)+1, max(self.fila, fila))))
        elif abs(self.fila - fila) == abs(self.columna - columna):
            # se mueve en diagonal:
            lista1 = range(min(self.columna, columna)+1, max(self.columna, columna))
            lista2 = range(min(self.fila, fila)+1, max(self.fila, fila))
            return self.validar_celdas(zip(lista1, lista2))
        else:
            return False
