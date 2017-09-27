# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

class Ficha(Actor):

    def iniciar(self, color="blanco", celda=None):
        self.imagen = "imagenes/pieza/"+color+"/"+self.nombre()+".png"
        self.color = color
        self.escala = 0.7
        self._celda = celda
        self.tablero = None

    def __str__(self):
        return self.nombre()+" "+self.color

    def definirTablero(self, tablero):
        self.tablero = tablero

    def puedeMoverA(self, columna, fila):
        """ valida si esta ficha puede moverse a otra posición
        este Método debe ser redefinido."""
        return False

    def nombre(self):
        return self.__name__

    def _getCelda(self):
        return self._celda

    def _setCelda(self, celda):
        self._celda = celda
        # posiciona sobre la celda:
        self.x = celda.x
        self.y = celda.y
        self.columna = celda.columna+1
        self.fila = celda.fila+1

    celda = property(fget=_getCelda, fset=_setCelda, doc="almacena la referencia a la celda en la cual esta la ficha. Si se sobreescribe reposiciona la ficha.")

    def moverA(self, columna, fila):
        """Mueve la ficha a otra celda."""
        puedeMover = self.puedeMoverA(columna, fila)
        if puedeMover:
            # realiza el movimiento:
            self.celda.liberar()
            self.tablero.reposicionar(self, columna=columna, fila=fila)

        return puedeMover
