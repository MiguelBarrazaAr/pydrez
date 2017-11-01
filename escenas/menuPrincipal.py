# -*- encoding: utf-8 -*-
import pilasengine

from actores.menu import Menu
from tts import leer as tts
from sonido import Sonido

class MenuPrincipal(pilasengine.escenas.Escena):

    def iniciar(self, pilas):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.decir = tts
        opciones = [('Jugar', self.jugar),
                    (u'Desafíos', self.desafios),
                    ('Conectarse', self.conectarse),
                    ('Tutorial', self.tutorial),
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
        self.pilas.escenas.PantallaJuego(pilas=self.pilas)

    def desafios(self):
        self.pilas.escenas.MenuDesafios(pilas=self.pilas)
        #self.pilas.escenas.Desafio(pilas=self.pilas, nombreDesafio='2')

    def conectarse(self):
        print("conectarse")

    def tutorial(self):
        print("tutorial")

    def creditos(self):
        print("creditos")

    def salir(self):
        exit()