# -*- encoding: utf-8 -*-
from .ajedrez_tradicional import ReglasAjedrezTradicional
from sonido import Sonido

class ReglasAjedrezConRio(ReglasAjedrezTradicional):

    def __init__(self, *args, **kwargs):
        ReglasAjedrezTradicional.__init__(self, *args, **kwargs)
        self.definirTablero("rio")
