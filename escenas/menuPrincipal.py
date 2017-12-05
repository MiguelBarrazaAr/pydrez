# -*- encoding: utf-8 -*-
import pilasengine

from actores.menu import Menu
from tts import leer as tts
from sonido import Sonido

class MenuPrincipal(pilasengine.escenas.Escena):

    def iniciar(self, pilas, datos=None):
        musica = pilas.datos.musica
        if musica is not None:
            musica.reproducir(repetir=True)
        self.pilas.eventos.pulsa_tecla_escape.conectar(self.cuandoPulsaEscape)
        marronClaro = pilas.colores.Color(128, 84, 66)
        marronOscuro = pilas.colores.Color(77, 38, 22)
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/fondoMenu.jpg")
        self.decir = tts
        self.datos=datos
        if datos is None:
            opciones = [('Jugar contra la maquina', self.jugar),
                (u"Desafíos", self.desafios),
                (u"Conectarse a un servidor", self.conectarse),
                (u"Establecerse como servidor", self.levantarServidor),
                (u"Modos de juego para 2 jugadores", self.modoJuego),
                (u'Configuracion', self.configurar),
                (u"Creditos", self.creditos),
                ('Salir', self.salir)]
        else:
            opciones = [('Jugar contra la maquina', self.jugar),
                (u'Continuar Con la partida', self.continuarConPartida),
                (u"Desafíos", self.desafios),
                (u"Conectarse a un servidor", self.conectarse),
                (u"Establecerse como servidor", self.levantarServidor),
                (u"Modos de juego para 2 jugadores", self.modoJuego),
                (u"Creditos", self.creditos),
                ('Salir', self.salir)]

        self.menu = Menu(pilas, y = 170 , opciones = opciones, fuente= "datos/tipografia/anirb___.ttf", color_normal=marronOscuro,color_resaltado=marronClaro)
        self.menu.seleccionaOpcion.conectar(self.seleccionarItem)
        self.menu.activaOpcion.conectar(self.activarOpcion)
        self.decir(u"menú principal: pulse las flechas para navegar por el menú.", False)
        self.sonidoMover = Sonido("audio/menu_opcion.ogg")
        self.sonidoAbrir = Sonido("audio/menu_abrir.ogg")
        self.sonidoCerrar = Sonido("audio/menu_cerrar.ogg")
        self.sonidoAbrir.reproducir()

    def cuandoPulsaEscape(self, evento):
        if self.datos:
            self.sonidoCerrar.reproducir()
            self.continuarConPartida()

    def seleccionarItem(self, evento):
        self.sonidoMover.reproducir()
        self.decir(evento.texto)

    def activarOpcion(self, evento):
        self.sonido_activar = Sonido("audio/menu_enter.ogg")
        self.sonido_activar.volumen = 0.3
        self.sonido_activar.reproducir()

    def jugar(self):
        self.pilas.datos['modoJuego'] = "ajedrezIa"
        self.pilas.escenas.ElegirColor(self.pilas)

    def continuarConPartida(self):
        self.pilas.escenas.PantallaJuego(pilas=self.pilas, datos=self.datos)

    def desafios(self):
        self.pilas.escenas.MenuDesafios(pilas=self.pilas)
        #self.pilas.escenas.Desafio(pilas=self.pilas, nombreDesafio='2')

    def conectarse(self):
        self.pilas.escenas.ConectarseAlServidor(pilas=self.pilas)

    def levantarServidor(self):
        print("tutorial")

    def modoJuego(self):
        self.pilas.escenas.ModoJuego(pilas=self.pilas)

    def creditos(self):
        print("creditos")

    def configurar(self):
        self.pilas.escenas.Configurar(self.pilas)

    def salir(self):
        exit()