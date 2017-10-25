# -*- encoding: utf-8 -*-
# pilas engine: un motor para hacer videojuegos
#
# Copyright 2010-2014 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

from pilasengine.actores.actor import Actor
from pilasengine import colores


class OpcionConImagen(Actor):
    """Un item discreto, dispara una funcion al seleccionares."""

    def __init__(self, pilas, texto="", x=0, y=0,
                 funcion_a_invocar=None,argumentos=None,fuente=None, imagen=None, escala=None,
                 color_normal=colores.gris,
                 color_resaltado=colores.blanco):
        """Inicializa el actor.

        :param texto: Etiqueta a mostrar
        :param x: Posicion en el eje x
        :param y: Posicion en el eje y
        :param funcion_a_invocar: Manejador, se dispara al seleccionar la opcion
        :param argumentos: Argumentos posicionales para :funcion_a_invocar:
        :param fuente: Tipografía a utilizar.
        """
        Actor.__init__(self, pilas, x=x, y=y, imagen=imagen)
        self.escala = escala
        self.texto = texto
        self.funcion_a_invocar = funcion_a_invocar
        self.argumentos = argumentos
        self.color_normal = color_normal
        self.color_resaltado = color_resaltado
        self.color = self.color_normal
        self.z = -300
        self.centro = ("centro", "centro")

    def resaltar(self, estado=True):
        """Pinta la opcion actual de un color mas claro.

        :param estado: True o False indicando si se tiene que resaltar o deseleccionar la opción.
        """
        if estado:
            self.escala *= 2
        else:
            self.escala /= 2

    def seleccionar(self):
        """Invoca a la funcion que tiene asociada para ejecutar."""

        if self.funcion_a_invocar:
            self.funcion_a_invocar(*self.argumentos)
        else:
            print "Cuidado, la opcion", self, "no tiene funcion asociada."