# -*- encoding: utf-8 -*-
# menuAccesible basado en el actor menu de pilas.

from pilasengine.actores.actor import Actor
from pilasengine import colores
from pilasengine.controles import simbolos

class Menu(Actor):
    """Un actor que puede mostrar una lista de opciones a seleccionar."""

    def __init__(self, pilas, x=0, y=0, opciones=[], fuente=None,
             color_normal=colores.gris, color_resaltado=colores.blanco,
             imagenFondo= None, distancia = 50, escala = 1):
        Actor.__init__(self, pilas, x=x, y=y)
        self.opciones_como_actores = []
        self.iconos_de_opciones = []
        self.imagen = "invisible.png"
        self._verificar_opciones(opciones)
        self.crear_texto_de_las_opciones(opciones, fuente, color_normal , color_resaltado, imagenFondo=imagenFondo, distancia= distancia, escala= escala)
        self.opciones = opciones
        self.seleccionar_primer_opcion()
        self.opcion_actual = 0


        # eventos:
        self.seleccionaOpcion = pilas.evento.Evento("selecciona_opcion")
        self.activaOpcion = pilas.evento.Evento("activa_opcion")
        self.activar()

    def activar(self):
        """Se ejecuta para activar el comportamiento del menú."""
        self.pilas.escena_actual().mueve_mouse.conectar(self.cuando_mueve_el_mouse)
        self.pilas.escena_actual().click_de_mouse.conectar(self.cuando_hace_click_con_el_mouse)
        self.pilas.eventos.pulsa_tecla.conectar(self.interpreta_teclado)

    def desactivar(self):
        """Deshabilita toda la funcionalidad del menú."""
        self.pilas.escena_actual().mueve_mouse.desconectar(self.cuando_mueve_el_mouse)
        self.pilas.escena_actual().click_de_mouse.desconectar(self.cuando_hace_click_con_el_mouse)
        self.pilas.eventos.pulsa_tecla.desconectar(self.interpreta_teclado)

    def crear_texto_de_las_opciones(self, opciones, fuente, color_normal, color_resaltado, imagenFondo, distancia, escala):
        """Genera un actor por cada opcion del menu.

        :param opciones: Una lista con todas las opciones que tendrá el menú.
        """

        for indice, opcion in enumerate(opciones):
            y = self.y - indice * distancia
            if len(opcion) == 2:
                texto, funcion, argumentos = opcion[0], opcion[1], opcion[2:] #No debería de aceptar argumentos
            else:
                if isinstance(opcion[2], list):
                    texto, funcion, argumentos = opcion[1], opcion[2][0], opcion[2][1:]
                    icono = self.pilas.actores.Actor(x=-120, y=y)
                    icono.imagen = opcion[0]
                    self.iconos_de_opciones.append(icono)
                else:
                    texto, funcion, argumentos = opcion[0], opcion[1], opcion[2:]

            opciones = self.pilas.actores.Opcion(texto, x=self.x, y=y, funcion_a_invocar=funcion, argumentos=argumentos, fuente=fuente,
                                            color_normal=color_normal, color_resaltado=color_resaltado)

            if imagenFondo is not None:
                actorImagen = self.pilas.actores.Actor(imagen=imagenFondo, x=self.x, y=y + 3)
                actorImagen.escala = escala

            self.opciones_como_actores.append(opciones)

    def seleccionar_primer_opcion(self):
        """Destaca la primer opción del menú."""
        if self.opciones_como_actores:
            self.opciones_como_actores[0].resaltar()
            try:
                self.iconos_de_opciones[0].escala = [self.escala * 2], .2
            except:
                pass

    def _verificar_opciones(self, opciones):
        """Se asegura de que la lista este bien definida.

        :param opciones: La lista de opciones a inspeccionar.
        """
        for x in opciones:

            if not isinstance(x, tuple) or len(x)<2:
                raise Exception("Opciones incorrectas, cada opcion tiene que ser una tupla.")

    def interpreta_teclado(self, evento):
        """Comportamiento al pulsar tecla"""
        if evento.codigo == self.pilas.simbolos.SELECCION:
            self.seleccionar_opcion_actual()
        elif evento.codigo == self.pilas.simbolos.ABAJO:
            self.mover_cursor(1)
        elif evento.codigo == self.pilas.simbolos.ARRIBA:
            self.mover_cursor(-1)

    def seleccionar_opcion_actual(self):
        """Se ejecuta para activar y lanzar el item actual."""
        opcion = self.opciones_como_actores[self.opcion_actual]
        self.activaOpcion.emitir(texto=opcion.texto)
        opcion.seleccionar()

    def mover_cursor(self, delta):
        """Realiza un movimiento del cursor que selecciona opciones.

        :param delta: El movimiento a realizar (+1 es avanzar y -1 retroceder).
        """
        # Deja como no-seleccionada la opcion actual.
        self._deshabilitar_opcion_actual()

        # Se asegura que las opciones esten entre 0 y 'cantidad de opciones'.
        self.opcion_actual += delta
        self.opcion_actual %= len(self.opciones_como_actores)

        # selecciona una nueva opcion, emite el evento:
        self.seleccionaOpcion.emitir(texto=self.opciones_como_actores[self.opcion_actual].texto)

        # Selecciona la opcion nueva.
        self.opciones_como_actores[self.opcion_actual].resaltar()
        try:
            self.iconos_de_opciones[self.opcion_actual].escala = [self.escala * 2],.3
        except:
            pass

    def __setattr__(self, atributo, valor):
        # Intenta propagar la accion a los actores del grupo.
        try:
            for x in self.opciones_como_actores:
                setattr(x, atributo, valor)
            for x in self.iconos_de_opciones:
                setattr(x , atributo, valor)
        except AttributeError:
            pass

        Actor.__setattr__(self, atributo, valor)

    def cuando_mueve_el_mouse(self, evento):
        """Permite cambiar la opcion actual moviendo el mouse. Retorna True si el mouse esta sobre alguna opcion.

        :param evento: El evento que representa el movimiento del mouse.
        """
        for indice, opcion in enumerate(self.opciones_como_actores):
            if opcion.colisiona_con_un_punto(evento.x, evento.y):
                if indice != self.opcion_actual:
                    self._deshabilitar_opcion_actual()
                    self.opcion_actual = indice
                    self.seleccionaOpcion.emitir(texto=self.opciones_como_actores[indice].texto)
                    self.opciones_como_actores[indice].resaltar()
                    try:
                        self.iconos_de_opciones[self.opcion_actual].escala = [self.escala * 2],.3
                    except:
                        pass
                return True

    def _deshabilitar_opcion_actual(self):
        """Le quita el foco o resaltado a la opción del menú actual."""
        self.opciones_como_actores[self.opcion_actual].resaltar(False)

        try:
            self.iconos_de_opciones[self.opcion_actual].escala = [self.escala],.3
        except:
            pass

    def cuando_hace_click_con_el_mouse(self, evento):
        """Se ejecuta cuando se hace click con el mouse.

        :param evento: objeto que representa el evento click de mouse.
        """
        if self.cuando_mueve_el_mouse(evento):
            self.seleccionar_opcion_actual()
