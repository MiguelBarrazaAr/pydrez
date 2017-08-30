from pilasengine.actores.actor import Actor

from celda import *

class Tablero(Actor):
    """Representa al tablero"""

    def __init__(self, pilas, x=0, y=0, alto=8, ancho=8):
        self._alto = alto
        self._ancho = ancho
        self.distancia = 30
        self.celda = Celda(pilas) * (alto * ancho)
        #self.z = 5
        #self.radio_de_colision = None

        negro = True
        h=0
        w=0
        for c in self.celda:
            c.x=x+w*self.distancia
            c.y=y+h*self.distancia
            c.z=100

            # coloreamos la celda:
            if negro:
                c.colorearNegro()


            w+=1
            # si llegamos al final de la fila volvemos al principio y subimos:
            if w == ancho:
                w=0
                h+=1
                if (ancho%2) == 1:
                    negro = not negro
            else:
                negro = not negro

