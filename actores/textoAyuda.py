# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

class TextoAyuda(Actor):

    def iniciar(self):
        self.imagen = "invisible.png"



    def decirAlgo(self):
        print "perro"