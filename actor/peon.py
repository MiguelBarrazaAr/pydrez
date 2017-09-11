# -*- encoding: utf-8 -*-
from actor.ficha import Ficha

class Peon(Ficha):

    def nombre(self):
        return "peon"

    def puedeMoverA(self, columna, fila):
        return True
