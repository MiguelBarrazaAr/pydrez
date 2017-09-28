# -*- encoding: utf-8 -*-

class Comportamiento(object):

    def __init__(self, color):
        self.nombre = self.__class__.__name__.lower()
        self.escala = 0.7
        self.color = color
        self.ficha = None

    def activar(self, ficha):
        self.ficha = ficha
        ficha.imagen = self.ruta_de_imagen()
        ficha.nombre = self.nombre
        ficha.color = self.color
        if self.escala:
            ficha.escala = self.escala

    def desactivar(self):
        self.ficha.imagen = 'invisible.png'
        self.ficha.nombre = 'desconocido'
        self.ficha.color = ''
        self.ficha = None

    def ruta_de_imagen(self):
        return "imagenes/fichas/"+self.color+"/"+self.nombre+".png"

    @property
    def columna(self):
        return self.ficha._celda.columna

    @property
    def fila(self):
        return self.ficha._celda.fila