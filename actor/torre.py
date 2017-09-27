from actor.ficha import Ficha

class Torre(Ficha):

    def nombre(self):
        return "torre"

    def puedeMoverA(self, columna, fila):
        if self._celda.fila == fila or self._celda.columna == columna:
            return True
        else:
            return False
