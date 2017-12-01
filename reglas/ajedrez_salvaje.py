# -*- encoding: utf-8 -*-
from .ajedrez_tradicional import ReglasAjedrezTradicional
from sonido import Sonido
from organizadores.ajedrez_salvaje  import AjedrezSalvaje

class AjedrezSalvaje(ReglasAjedrezTradicional):

    def __init__(self, *args, **kwargs):
        ReglasAjedrezTradicional.__init__(self, *args, **kwargs)
        self.organizador = AjedrezSalvaje
