# -*- encoding: utf-8 -*-
from .menu import EscenaMenu
from os import listdir

class MenuDesafios(EscenaMenu):

    def listaOpciones(self):
        desafios = []
        for desafio in listdir("datos/desafios"):
            desafios = [desafio[:-6]] + desafios
        desafios.sort()
        return map(lambda x: ('Opcion ' + x, self.cargarDesafio, x), desafios)

    def activar(self):
        self.decir(u"Desafíos disponibles: pulse las flechas para elegir un desafío y pulse enter para intentar superarlo.", False)

    def cuandoPulsaEscape(self, evento):
        self.pilas.escenas.MenuPrincipal(pilas=self.pilas)


    def cargarDesafio(self , nombreDesafio):
        self.pilas.escenas.Desafio(pilas=self.pilas, nombreDesafio=nombreDesafio)

    def irAMenuPrincipal():
        self.pilas.escenas.MenuPrincipal(pilas=pilas)


    def salir(self):
        exit()