# -*- encoding: utf-8 -*-
import pilasengine

from actores.menu import Menu
from tts import leer as tts
from sonido import Sonido

class MenuPrincipal(pilasengine.escenas.Escena):

    def iniciar(self, pilas, datos=None):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.decir = tts
        self.datos=datos
        opciones = [('Jugar', self.jugar),
                    (u"Desafíos", self.desafios),
                    (u"Conectarse a un servidor", self.conectarse),
                    (u"Establecerse como servidor", self.levantarServidor),
                    ('Creditos', self.creditos),
                    ('Salir', self.salir)]
        self.menu = Menu(pilas, y = 100 , opciones = opciones)
        self.menu.seleccionaOpcion.conectar(self.seleccionarItem)
        self.menu.activaOpcion.conectar(self.activarOpcion)
        self.decir(u"menú principal: pulse las flechas para navegar por el menú.", False)
        self.sonidoMover = Sonido("audio/menu_opcion.ogg")
        self.sonidoAbrir = Sonido("audio/menu_abrir.ogg")
        self.sonidoAbrir.reproducir()

    def seleccionarItem(self, evento):
        self.sonidoMover.reproducir()
        self.decir(evento.texto)

    def activarOpcion(self, evento):
        self.sonido_activar = Sonido("audio/menu_enter.ogg")
        self.sonido_activar.volumen = 0.3
        self.sonido_activar.reproducir()

    def jugar(self):
        self.pilas.escenas.PantallaJuego(pilas=self.pilas, datos=self.datos)

    def desafios(self):
        self.pilas.escenas.MenuDesafios(pilas=self.pilas)
        #self.pilas.escenas.Desafio(pilas=self.pilas, nombreDesafio='2')

    def conectarse(self):
        self.pilas.escenas.ConectarseAlServidor(pilas=self.pilas)

    def levantarServidor(self):
        print("tutorial")

    def creditos(self):
        print("creditos")

    def salir(self):
        exit()