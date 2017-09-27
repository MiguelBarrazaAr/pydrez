from actor.ficha import Ficha

class Alfil(Ficha):

    def nombre(self):
        return "alfil"

    def puedeMoverA(self, columna, fila):
        return True
