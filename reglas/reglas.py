# -*- encoding: utf-8 -*-
from organizadores.ajedrez_basico import AjedrezTradicional

class Reglas(object):

    def __init__(self):
        self.bandos = ['blanco', 'negro']
        self.turno = 0

    def pasar_turno(self):
        self.turno = (self.turno+1)%2

    def turno_actual(self):
        return self.bandos[self.turno]

    def obtener_organizador(self):
        """el organizador por default es el del ajedrez tradicional"""
        return AjedrezTradicional
