# -*- encoding: utf-8 -*-
import pilasengine
from os import listdir

from actores.menu import Menu
from tts import leer as tts
from sonido import Sonido

class ModoJuego(pilasengine.escenas.Escena):

    def iniciar(self, pilas, datos=None):
        marronClaro = pilas.colores.Color(128, 84, 66)
        marronOscuro = pilas.colores.Color(77, 38, 22)
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/fondoJuego.jpg")
        self.decir = tts
        self.datos=datos
        opciones = self.listaOpciones()
        self.menu = Menu(pilas,x = -300 ,y = 170, opciones = opciones,fuente= "datos/tipografia/anirb___.ttf", color_normal=marronOscuro, color_resaltado=marronClaro)
        self.menu.seleccionaOpcion.conectar(self.seleccionarItem)
        self.menu.activaOpcion.conectar(self.activarOpcion)
        self.decir(u"Modo juego: pulse las flechas para elegir un modo de juego.", False)
        self.sonidoMover = Sonido("audio/menu_opcion.ogg")
        self.sonidoAbrir = Sonido("audio/menu_abrir.ogg")
        self.sonidoAbrir.reproducir()

        self.texto = pilas.actores.Texto("", x= 170 ,y=25, ancho=500 , magnitud= 19, fuente= "datos/tipografia/al.ttf")
        self.texto.color = marronOscuro
        self.pilas.eventos.pulsa_tecla_escape.conectar(self.activar_menu_principal)

    def activar_menu_principal(self, evento):
        self.pilas.escenas.MenuPrincipal(pilas=self.pilas)

    def seleccionarItem(self, evento):
        file = open("datos/regla/" + (self.menu.opciones [self.menu.opcion_actual]) [0] + ".regla", "r")
        info = file.read()
        file.close()

        self.sonidoMover.reproducir()
        self.decir(evento.texto)
        self.texto.texto = info
        self.decir(info, False)


    def activarOpcion(self, evento):
        self.sonido_activar = Sonido("audio/menu_enter.ogg")
        self.sonido_activar.volumen = 0.3
        self.sonido_activar.reproducir()

    def listaOpciones(self):
        lista = []
        for f in listdir("datos/regla"):
            lista.append(f[:-6])
        lista.sort()
        return map(lambda x: (x, self.configurarModo, x), lista)

    def activar(self):
        self.decir(u"Modos de juegos disponibles: pulse las flechas para elegir uno,  pulse enter para ver como se juega o pulsa escape para regresar al menu anterior.", False)

    def cuandoPulsaEscape(self, evento):
        self.pilas.escenas.MenuPrincipal(pilas=self.pilas)

    def configurarModo(self , modo):
        self.pilas.datos['modoJuego'] = modo
        self.pilas.escenas.PantallaJuego(pilas=self.pilas)
