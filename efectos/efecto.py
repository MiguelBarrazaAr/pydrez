# -*- encoding: utf-8 -*-
class EfectoCelda(object):

    def configurarCelda(self, celda):
        """se aplica al iniciarse en una celda"""
        self.celda = celda
        celda.color = "azul"
        celda.cambiar("azul")

    def aplicarFicha(self, ficha):
        """Se aplica cuando una ficha cae en la celda."""
        pass
