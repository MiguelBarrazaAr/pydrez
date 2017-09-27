from actor.ficha import Ficha

class Caballo(Ficha):

    def nombre(self):
        return "caballo"


    def puedeMoverA(self, columna, fila):
        return True
