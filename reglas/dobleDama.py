# -*- encoding: utf-8 -*-
from .ajedrez_tradicional import ReglasAjedrezTradicional
from sonido import Sonido
from organizadores.doble_dama import OrganizadorDobleDama

class ReglasAjedrezDobleDama(ReglasAjedrezTradicional):

    def __init__(self, *args, **kwargs):
        ReglasAjedrezTradicional.__init__(self, *args, **kwargs)
        self.dimensionTablero = (9,8)
        self.organizador = OrganizadorDobleDama
