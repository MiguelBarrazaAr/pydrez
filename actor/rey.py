from actor.ficha import Ficha

class Rey(Ficha):

    def nombre(self):
        return "rey"

    def puedeMoverA(self, columna, fila):
        if abs(self._celda.fila - fila) == 1  and abs(self._celda.columna - columna) == 1:
            # se mueve en diagonal:
            return True
        elif self._celda.columna == columna and abs(self._celda.fila - fila) == 1:
            return True
        if self._celda.fila == fila and abs(self._celda.columna - columna) == 1:
            return True
        else:
            return False
