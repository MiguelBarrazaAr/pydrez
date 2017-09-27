from actor.ficha import Ficha

class Alfil(Ficha):

    def nombre(self):
        return "alfil"

    def puedeMoverA(self, columna, fila):
        if abs(self._celda.fila - fila) == abs(self._celda.columna - columna):
            return True
        else:
            return False
