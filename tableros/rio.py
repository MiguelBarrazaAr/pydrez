# -*- encoding: utf-8 -*-
from .tablero import ConfiguradorDeTablero

class TableroRio(ConfiguradorDeTablero):

    def __init__(self):
        self.dimensionTablero = (8, 11)
        self.celdas = {
            "5 0":"agua",
            "5 2":"agua",
            "5 3":"agua",
            "5 4":"agua",
            "5 5":"agua",
            "5 7":"agua",
        }

