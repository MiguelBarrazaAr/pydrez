# -*- encoding: utf-8 -*-
from .ajedrez_tradicional import ReglasAjedrezTradicional
from sonido import Sonido

class ReglasAjedrez8x12(ReglasAjedrezTradicional):

    def __init__(self, *args, **kwargs):
        ReglasAjedrezTradicional.__init__(self, *args, **kwargs)
        self.dimensionTablero = (20, 20)
