# -*- encoding: utf-8 -*-
import pilasengine

from actores.menu import Menu
from actores.menuConImagen import MenuConImagen
from tts import leer as tts
from sonido import Sonido

class EscenaMenu(pilasengine.escenas.Escena):

    def configuracion(self):
        """Este metodo se debe sobreescribir si alguna variable de la configuracion se debe modificar"""
        pass

    def iniciar(self, pilas):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/fondoJuego.jpg")
        self.colorResaltado = pilas.colores.Color(128, 84, 66)
        self.colorNormal = pilas.colores.Color(77, 38, 22)
        self.menu_x = 0
        self.menu_y = 0
        self.fuente = "datos/tipografia/anirb___.ttf"
        self.imagenFondo = "imagenes/fondo/boton.jpg"
        self.distancia = 50
        self.configuracion()
        self.decir = tts
        self.menu = Menu(pilas, x=self.menu_x, y=self.menu_y, opciones=self.listaOpciones(), fuente=self.fuente, color_normal=self.colorNormal, color_resaltado=self.colorResaltado , imagenFondo= self.imagenFondo, distancia=self.distancia)
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
