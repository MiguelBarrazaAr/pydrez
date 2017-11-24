# -*- encoding: utf-8 -*-
import pilasengine
from os import listdir

from actores.menu import Menu
from tts import leer as tts
from sonido import Sonido

class ModoJuego(pilasengine.escenas.Escena):

    def iniciar(self, pilas, datos=None):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.decir = tts
        self.datos=datos
        opciones = self.listaOpciones()
        self.menu = Menu(pilas,y = 70, opciones = opciones)
        self.menu.seleccionaOpcion.conectar(self.seleccionarItem)
        self.menu.activaOpcion.conectar(self.activarOpcion)
        self.decir(u"Modo juego: pulse las flechas para elegir un modo de juego.", False)
        self.sonidoMover = Sonido("audio/menu_opcion.ogg")
        self.sonidoAbrir = Sonido("audio/menu_abrir.ogg")
        self.sonidoAbrir.reproducir()
        self.menu.x = -200
        self.texto = pilas.actores.Texto("", x= 90 ,y=25, ancho=350 , magnitud= 17, fuente= "datos/tipografia/KaushanScript-Regular.otf")

    def seleccionarItem(self, evento):
        file = open("datos/regla/" + (self.menu.opciones [self.menu.opcion_actual]) [0] + ".regla", "r")
        info = file.read()
        file.close()

        self.sonidoMover.reproducir()
        self.decir(evento.texto)
        self.texto.texto = info


    def activarOpcion(self, evento):
        self.sonido_activar = Sonido("audio/menu_enter.ogg")
        self.sonido_activar.volumen = 0.3
        self.sonido_activar.reproducir()

    def listaOpciones(self):
        lista = []
        for f in listdir("datos/regla"):
            lista.append(f[:-6])
        lista.sort()
        return map(lambda x: (x, self.mostrarAyuda, x), lista)

    def activar(self):
        self.decir(u"Modos de juegos disponibles: pulse las flechas para elegir uno,  pulse enter para ver como se juega o pulsa escape para regresar al menu anterior.", False)

    def cuandoPulsaEscape(self, evento):
        self.pilas.escenas.MenuPrincipal(pilas=self.pilas)


    def mostrarAyuda(self , modo):
        print(modo)

    def salir(self):
        exit()