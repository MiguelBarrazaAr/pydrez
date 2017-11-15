# -*- encoding: utf-8 -*-
from .menu import EscenaMenu
from os import listdir

class ModoJuego(EscenaMenu):

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