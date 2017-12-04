# -*- encoding: utf-8 -*-
from .tablero import ConfiguradorDeTablero

class TableroRio(ConfiguradorDeTablero):

    def __init__(self):
        self.dimensionTablero = (8, 11)
        self.celdas = {
            "a 6":"agua",
            "c 6":"agua",
            "d 6":"agua",
            "e 6":"agua",
            "f 6":"agua",
            "h 6":"agua",
        }

