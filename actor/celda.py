# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

class Celda(Actor):

    def __init__(self, pilas, x=0, y=0, z=0, color='blanco'):
        Actor.__init__(self, pilas, x=x, y=y)
        self.z = z
        self.color = color

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
