# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

class Celda(Actor):

    def __init__(self, pilas, x=0, y=0, z=0, color='blanco', columna=0, fila=0):
        Actor.__init__(self, pilas, x=x, y=y)
        self.z = z
        self.color = color
        self.ficha = None
        self.columna = columna
        self.fila = fila

        if color == 'blanco':
            self.normal = "imagenes/celda/blanco.png"
        else:
            self.normal = "imagenes/celda/negro.png"

        self.verde = "imagenes/celda/verde.png"
        self.imagen = self.normal


    def colorearVerde(self):
        self.imagen = self.verde

    def colorearNormal(self):
        """Regresa la celda a su color base"""
        self.imagen = self.normal

    def estaLibre(self):
        return self.ficha is not None

    def seleccionar(self):
        if not self.seleccionado:
            self.colorearVerde()
            self.seleccionado = True

    def deseleccionar(self):
        """Solo si la celda esta seleccionado permite deseleccionar"""
        if self.seleccionado:
            self.colorearNormal()
            self.seleccionado = False

    def ponerFicha(self, actor):
        """Posiciona un actor sobre esta celda."""
        self.ficha = actor
        actor.x = self.x
        actor.y = self.y
