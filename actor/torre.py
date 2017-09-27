from actor.ficha import Ficha

class Torre(Ficha):

    def nombre(self):
        return "torre"

    def puedeMoverA(self, columna, fila):
        return True
