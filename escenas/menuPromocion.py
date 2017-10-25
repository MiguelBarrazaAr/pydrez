# -*- encoding: utf-8 -*-
import pilasengine

from actores.menuConImagen import MenuConImagen
from tts import leer as tts

class MenuPromocion(pilasengine.escenas.Escena):

    def iniciar(self, pilas):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.decir = tts
        piezas  = ['alfil',
        "peon",
        "rey",
        "goleM",
        "enano",
            'caballo',
            'dama',
            'torre']
        opciones = map(lambda x: (x, self.ejecutar, x), piezas)
        self.menu = MenuConImagen(pilas, y = 100 , opciones = opciones, rutaImagenes="imagenes/fichas/blanco/")
        self.decir(u"Elija con a que ficha desea promocionar: pulse las flechas para navegar por las opciones y enter para seleccionar.", False)


    def ejecutar(self, opcion):
        print(opcion)
        exit()
