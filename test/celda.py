# -*- encoding: utf-8 -*-
# celdaMock

class CeldaMock(object):

    def __init__(self, columna, fila):
        self.columna = columna
        self.fila = fila

def generar(columna, fila):
    # retorna una celda Mock
    columna -= 1
    fila -= 1
    return CeldaMock(columna, fila)
