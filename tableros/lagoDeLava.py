# -*- encoding: utf-8 -*-
from .tablero import ConfiguradorDeTablero

class TableroLagoDeLava(ConfiguradorDeTablero):

    def __init__(self):
        self.dimensionTablero = (8, 9)
        self.celdas = {
            "c 5":"lava",
            "c 4": "lava",
            "c 6":"lava",
            "d 5": "lava",
            "d 4": "lava",
            "d 6": "lava",
            "e 5":"lava",
            "e 4": "lava",
            "e 6":"lava",
            "f 5":"lava",
            "f 4": "lava",
            "f 6":"lava",
        }