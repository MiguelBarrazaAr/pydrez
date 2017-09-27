from actor.ficha import Ficha

class Rey(Ficha):

    def nombre(self):
        return "rey"

    def puedeMoverA(self, columna, fila):
        return True
