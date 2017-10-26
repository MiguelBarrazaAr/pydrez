# -*- encoding: utf-8 -*-
import pilasengine

from actores.menu import MenuAccesible
from tts import leer as tts
from os import listdir




class Desafios(pilasengine.escenas.Escena):

    def iniciar(self, pilas):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.decir = tts
        desafios = []
        for desafio in listdir("datos/desafios"):
            desafios = [desafio[:-6]] + desafios
        desafios.sort()
        opciones = map(lambda x: ('Opcion ' + x, self.cargarDesafio, x), desafios)
        self.menu = MenuAccesible(pilas, y = 100 , opciones = opciones, tts=tts)
        self.decir(u"menú de desafios: pulse las flechas para navegar por el menú.", False)
        self.pilas.eventos.pulsa_tecla_escape.conectar(self.activar_menu_principal)

    def activar_menu_principal(self, evento):
        self.pilas.escenas.MenuPrincipal(pilas=self.pilas)


    def cargarDesafio(self , nombreDesafio):
        self.pilas.escenas.Desafio(pilas=self.pilas, nombreDesafio=nombreDesafio)

    def irAMenuPrincipal():
        self.pilas.escenas.MenuPrincipal(pilas=pilas)


    def salir(self):
        exit()