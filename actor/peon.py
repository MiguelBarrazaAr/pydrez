# -*- encoding: utf-8 -*-
from actor.ficha import Ficha

class Peon(Ficha):

    def nombre(self):
        return "peon"

    def puedeMoverA(self, columna, fila):
        """los peones podrán caminar 2 pasos si es su primer movimiento, luego solo podrá moverse de a 1 paso siempre hacia adelante.
        come 1 paso en  diagonal."""
        if self.color == "blanco":
            return self._blanco_puedeMoverA(columna, fila)
        else:
            return self._negro_puedeMoverA(columna, fila)

    def _blanco_puedeMoverA(self, columna, fila):
        if self.columna == columna and (self.fila+1) == fila:
            return True
        elif fila == 4 and self.columna == columna:
            return True
        else:
            return False

    def _negro_puedeMoverA(self, columna, fila):
        return False
