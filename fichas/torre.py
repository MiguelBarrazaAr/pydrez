# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento

class Torre(Comportamiento):

    def puedeMoverA(self, columna, fila):
        if self.fila == fila or self.columna == columna:
            return self.validar_celdas_intermedias(columna, fila)
        else:
            return False

    def validar_celdas_intermedias(self, columna, fila):
        lista = []
        if self.fila == fila:
            for x in range(min(self.columna, columna)+1, max(self.columna, columna)):
                lista.append((x, fila))
        else:
            for x in range(min(self.fila, fila)+1, max(self.fila, fila)):
                lista.append((columna, x))

        return self.validar_celdas(lista)
