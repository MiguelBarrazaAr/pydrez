# -*- encoding: utf-8 -*-
from .tablero import ConfiguradorDeTablero

class TableroLagoDeLava(ConfiguradorDeTablero):

    def __init__(self):
        self.dimensionTablero = (8, 11)
        self.celdas = {
            "c 6":"lava",
            "c 5": "lava",
            "c 7":"lava",
            "d 6": "lava",
            "d 5": "lava",
            "d 7": "lava",
            "e 6":"lava",
            "e 5": "lava",
            "e 7":"lava",
            "f 6":"lava",
            "f 5": "lava",
            "f 7":"lava",
        }