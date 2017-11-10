# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

class Ficha(Actor):

    def __init__(self, pilas):

        self._celda = None
        self.tablero = None
        self.comportamiento = None
        self.nombre = ''
        self.color = ''
        Actor.__init__(self, pilas, x=0, y=0, imagen='invisible.png')


    def __repr__(self):
        if self.color == "blanco":
            return self.nombre[0].upper()
        else:
            return self.nombre[0]

    def __str__(self):
        return self.nombre+" "+self.color

    def definir_tablero(self, tablero):
        self.tablero = tablero

    def definir_comportamiento(self, comportamiento):
        comportamiento.activar(self)
        self.comportamiento = comportamiento

    def eliminar_comportamiento(self):
        self.comportamiento.desactivar()
        self.comportamiento = None

    def _getCelda(self):
        return self._celda

    def _setCelda(self, celda):
        self._celda = celda
        # posiciona sobre la celda:
        self.x = celda.x
        self.y = celda.y

    celda = property(fget=_getCelda, fset=_setCelda, doc="almacena la referencia a la celda en la cual esta la ficha. Si se sobreescribe reposiciona la ficha.")

    def puede_mover(self, celda):
        """Retorna si la ficha puede moverse a la celda indicada por parámetro."""
        if self.comportamiento is None:
            return False
        else:
            if celda.tiene_ficha():
                # si tiene ficha verifica si la puede comer:
                return self.comportamiento.puedeComerEn(celda)
            else:
                # si no tiene ficha retorna si puede mover a esa celda:
                return self.comportamiento.puedeMoverA(columna=celda.columna, fila=celda.fila)

    def eliminar(self):
        self.pilas.log(self.nombre, self.color, "de (", self._celda.columna, ",", self._celda.fila, "), se elimina del juego.")
        self.eliminar_comportamiento()
        self.celda.liberar()
        self._celda = None

    def noTieneComportamiento(self):
        return self.comportamiento is None

    def tieneComportamiento(self):
        return self.comportamiento is not None
