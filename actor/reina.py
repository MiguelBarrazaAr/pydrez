from actor.ficha import Ficha

class Reina(Ficha):

    def nombre(self):
        return "reina"

    def puedeMoverA(self, columna, fila):
        if self._celda.fila == fila or self._celda.columna == columna:
            # se mueve en diagonal:
            return True
        elif abs(self._celda.fila - fila) == abs(self._celda.columna - columna):
            return True
        else:
            return False
