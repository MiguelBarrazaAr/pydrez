# -*- encoding: utf-8 -*-
import pilasengine

from actores.menu import Menu
from tts import leer as tts
from sonido import Sonido

class EscenaMenu(pilasengine.escenas.Escena):

    def iniciar(self, pilas):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.decir = tts
        self.menu = Menu(pilas, y = 100 , opciones=self.listaOpciones())
        self.menu.seleccionaOpcion.conectar(self.seleccionarOpcion)
        self.menu.activaOpcion.conectar(self.activarOpcion)
        self.sonidoMover = Sonido("audio/menu_opcion.ogg")
        self.sonidoAbrir = Sonido("audio/menu_abrir.ogg")
        self.activar()
        self.pilas.eventos.pulsa_tecla_escape.conectar(self.cuandoPulsaEscape)

    def cuandoPulsaEscape(self, evento):
        self.pilas.escenas.MenuPrincipal(pilas=self.pilas)

    def activar(self):
        self.decir(u"menú principal: pulse las flechas para navegar por el menú.", False)
        self.sonidoAbrir.reproducir()

    def seleccionarOpcion(self, evento):
        self.sonidoMover.reproducir()
        self.decir(evento.texto)

    def activarOpcion(self, evento):
        self.sonido_activar = Sonido("audio/menu_enter.ogg")
        self.sonido_activar.volumen = 0.3
        self.sonido_activar.reproducir()

    def listaOpciones(self):
        return ["Salir", self.salir]

    def salir(self):
        exit()
