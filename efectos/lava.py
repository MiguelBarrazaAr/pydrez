# -*- encoding: utf-8 -*-
from .efecto import EfectoCelda

class FxLava(EfectoCelda):

    def configurarCelda(self, celda):
        """se aplica al iniciarse en una celda"""
        self.celda = celda
        celda.definirTipo("rojo")

    def __str__(self):
        return "lava"