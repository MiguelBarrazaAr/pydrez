# -*- encoding: utf-8 -*-
from pilasengine.actores.actor import Actor

class Celda(Actor):

    def __init__(self, pilas, x=0, y=0, z=0, color='blanco', columna=0, fila=0, estiloDeCelda="celda"):
        Actor.__init__(self, pilas, x=x, y=y)
        self.z = z
        self.color = color
        self.ficha = None
        self.columna = columna
        self.fila = fila
        self.seleccionado = False
        self.estiloDeCelda = estiloDeCelda
        self.escala = 2.3
        self._efecto = None


        if color == 'blanco':
            self.normal = "imagenes/"+estiloDeCelda+"/blanco.png"
        else:
            self.normal = "imagenes/"+estiloDeCelda+"/negro.png"

        self.imagen = self.normal

    def __repr__(self):
        if self.columna >= 0 and self.columna <= 24:
            return chr(self.columna+97)+str(self.fila+1)
        else:
            return str(self.columna)+str(self.fila)

    def __str__(self):
        if self.columna >= 0 and self.columna <= 24:
            text = chr(self.columna+97)+str(self.fila+1)
        else:
            text = str(self.columna)+str(self.fila)

        if self._efecto is not None:
            text += str(self._efecto)

        return text

    def cambiar(self, nombreDeCelda):
        self.imagen = "imagenes/"+self.estiloDeCelda+"/"+nombreDeCelda+".png"

    def normalizar(self):
        """Regresa la celda a su color base"""
        self.imagen = self.normal

    def estaLibre(self):
        return self.ficha is None

    def tiene_ficha(self):
        return self.ficha is not None

    def seleccionar(self):
        if not self.seleccionado:
            self.cambiar("verde")
            self.seleccionado = True

    def deseleccionar(self):
        """Solo si la celda esta seleccionado permite deseleccionar"""
        if self.seleccionado:
            self.normalizar()
            self.seleccionado = False

    def ponerFicha(self, unaFicha):
        """Posiciona una ficha sobre esta celda.
        si ya tiene una lo elimina."""
        if self.tiene_ficha():
            self.ficha.eliminar()

        self.ficha = unaFicha
        unaFicha.celda = self

    def liberar(self):
        """metodo que se invoca cuando un actor deja esta celda."""
        self.ficha = None

    @property
    def efecto(self):
        return self._efecto

    @efecto.setter
    def efecto(self, efecto):
        if efecto is not None:
            efecto.configurarCelda(self)
        self._efecto = efecto