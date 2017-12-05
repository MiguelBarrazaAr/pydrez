# -*- encoding: utf-8 -*-
from .menu import EscenaMenu
from os import listdir

class MenuDesafios(EscenaMenu):

    def configuracion(self):
        self.menu_y = 190
        self.colorResaltado = self.pilas.colores.Color(0, 0, 0)
        self.colorNormal = self.pilas.colores.Color(255, 255, 255)
        self.distancia = 50
        self.texto = self.pilas.actores.Texto("       Realiza movimientos siempre comiendo, \n y logra que quede solo una pieza en el tablero\n",y= 280,  magnitud= 25, fuente= "datos/tipografia/al.ttf")
        self.texto.color = self.colorResaltado
        self.escala = 0.5

    def listaOpciones(self):
        desafios = []
        for desafio in listdir("datos/desafios"):
            desafios = [desafio[:-6]] + desafios
        desafios.sort()
        return map(lambda x: ('Desafio ' + x, self.cargarDesafio, x), desafios)

    def activar(self):
        self.decir(u"Desafíos disponibles: pulse las flechas para elegir un desafío y pulse enter para intentar superarlo.", False)

    def cuandoPulsaEscape(self, evento):
        self.pilas.escenas.MenuPrincipal(pilas=self.pilas)


    def cargarDesafio(self , nombreDesafio):
        self.pilas.escenas.Desafio(pilas=self.pilas, nombreDesafio=nombreDesafio)

    def salir(self):
        exit()