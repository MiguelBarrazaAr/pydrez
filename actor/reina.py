from actor.ficha import Ficha

class Reina(Ficha):

    def nombre(self):
        return "reina"

    def puedeMoverA(self, columna, fila):
        return True
