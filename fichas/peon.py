# -*- encoding: utf-8 -*-
from .comportamiento import Comportamiento
from .dama import Dama

class Peon(Comportamiento):

    def puedeMoverA(self, columna, fila):
        """los peones podrán caminar 2 pasos si es su primer movimiento, luego solo podrá moverse de a 1 paso siempre hacia adelante.
        come 1 paso en  diagonal."""
        if self.bando == "blanco":
            return self._blanco_puedeMoverA(columna, fila)
        else:
            return self._negro_puedeMoverA(columna, fila)

    def _blanco_puedeMoverA(self, columna, fila):
        if self.columna == columna and (self.fila+1) == fila:
            self.validar_promocion(fila, self.ficha.tablero.filas-1)
            return True
        elif fila == 3 and self.columna == columna:
            return self.validar_celdas([(columna, 2)])
        else:
            return False

    def _negro_puedeMoverA(self, columna, fila):
        if self.columna == columna and (self.fila-1) == fila:
            self.validar_promocion(fila, 0)
            return True
        elif fila == (self.ficha.tablero.filas-4) and self.columna == columna:
            return self.validar_celdas([(columna, self.ficha.tablero.filas-3)])
        else:
            return False

    def puedeComerEn(self, celda):
        """los peones solo pueden comer un paso en diagonal hacia adelante"""
        if self.bando == "blanco":
            self.validar_promocion(celda.fila, self.ficha.tablero.filas-1)
            return self.fila+1 == celda.fila and abs(celda.columna-self.columna) == 1
        else:
            self.validar_promocion(celda.fila, 0)
            return self.fila-1 == celda.fila and abs(celda.columna-self.columna) == 1

    def validar_promocion(self, fila, ultimaFila):
        if fila == ultimaFila:
            self.ficha.definir_comportamiento(Dama(self.ficha.color))
