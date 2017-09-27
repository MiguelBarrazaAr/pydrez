from actor.ficha import Ficha

class Caballo(Ficha):

    def nombre(self):
        return "caballo"


    def puedeMoverA(self, columna, fila):
        if abs(self._celda.columna-columna) == 2 and abs(self._celda.fila-fila) == 1:
            return True
        elif abs(self._celda.columna-columna) == 1 and abs(self._celda.fila-fila) == 2:
            return True
        else:
            return False
