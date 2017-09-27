# -*- encoding: utf-8 -*-
from actor.ficha import Ficha

class Peon(Ficha):

    def nombre(self):
        return "peon"

    def puedeMoverA(self, columna, fila):
        """los peones podr�n caminar 2 pasos si es su primer movimiento, luego solo podr� moverse de a 1 paso siempre hacia adelante.
        come 1 paso en  diagonal."""
        if self.color == "blanco":
            return self._blanco_puedeMoverA(columna, fila)
        else:
            return self._negro_puedeMoverA(columna, fila)

    def _blanco_puedeMoverA(self, columna, fila):
        # precondici�n: la propiedad celda no debe ser None
        if self._celda.columna == columna and (self._celda.fila+1) == fila:
            return True
        elif fila == 3 and self._celda.columna == columna:
            return True
        else:
            return False

    def _negro_puedeMoverA(self, columna, fila):
        # precondici�n: la propiedad celda no debe ser None
        if self._celda.columna == columna and (self._celda.fila-1) == fila:
            return True
        elif fila == 4 and self._celda.columna == columna:
            return True
        else:
            return False

