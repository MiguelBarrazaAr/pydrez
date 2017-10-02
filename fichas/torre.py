# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento

class Torre(Comportamiento):

    def puedeMoverA(self, columna, fila):
        if self.fila == fila or self.columna == columna:
            return self.validar_celdas_intermedias(columna, fila)
        else:
            return False

    def validar_celdas_intermedias(self, columna, fila):
        if self.fila == fila:
            lista = map((lambda x: (x, fila)), range(min(self.columna, columna)+1, max(self.columna, columna)))
        else:
            lista = map((lambda x: (columna, x)), range(min(self.fila, fila)+1, max(self.fila, fila)))

        print(lista)
        return self.validar_celdas(lista)
