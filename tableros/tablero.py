# -*- encoding: utf-8 -*-

class ConfiguradorDeTablero(object):

    def __init__(self):
        self.dimensionTablero = (8, 8)
        self.celdas = {}


    def celda(self, columna, fila):
        return celdas.get(str(columna) +" "+ str(fila), None)