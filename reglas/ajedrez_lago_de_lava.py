# -*- encoding: utf-8 -*-
from .ajedrez_tradicional import ReglasAjedrezTradicional
from sonido import Sonido
from organizadores.ajedrez_lago_de_lava  import OrganizadorAjedrezLagoDeLava


class ReglasAjedrezConLagoDeLava(ReglasAjedrezTradicional):

    def __init__(self, *args, **kwargs):
        ReglasAjedrezTradicional.__init__(self, *args, **kwargs)
        self.organizador = OrganizadorAjedrezLagoDeLava
        self.definirTablero("lagoDeLava")