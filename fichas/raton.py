# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento
from .dama import Dama

class Raton(Comportamiento):

    def _puedeMoverA(self, columna, fila):

        if self.bando == "blanco":
            return self._blanco_puedeMoverA(columna, fila)
        else:
            return self._negro_puedeMoverA(columna, fila)

    def _blanco_puedeMoverA(self, columna, fila):
        if self.columna == columna and abs(self.fila + fila) == 1:
            return True
        elif fila == 3 and self.columna == columna:
            return self.validar_celdas([(columna, 2)])
        else:
            return False

    def _negro_puedeMoverA(self, columna, fila):
        if self.columna == columna and abs(self.fila - fila) == 1:
            return True
        elif fila == (self.ficha.tablero.filas - 4) and self.columna == columna:
            return self.validar_celdas([(columna, self.ficha.tablero.filas - 3)])
        else:
            return False
