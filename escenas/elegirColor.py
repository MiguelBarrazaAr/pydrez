# -*- encoding: utf-8 -*-
from .menu import EscenaMenu

class ElegirColor(EscenaMenu):

    def configuracion(self):
        self.menu_y = 190
        self.colorResaltado = self.pilas.colores.Color(0, 0, 0)
        self.colorNormal = self.pilas.colores.Color(255, 255, 255)
        self.distancia = 90
        self.texto = self.pilas.actores.Texto("elija con que color desea jugar:",y= 280,  magnitud= 25, fuente= "datos/tipografia/al.ttf")
        self.texto.color = self.colorResaltado

    def listaOpciones(self):
        colores = ['Blancas', 'Negras']
        return map(lambda x: (x, self.definirColor, x), colores)

    def activar(self):
        self.decir(u'pulse las flechas para elegir con que color desea jugar. pulse enter para confirmar.', False)

    def cuandoPulsaEscape(self, evento):
        self.pilas.escenas.MenuPrincipal(pilas=self.pilas)

    def definirColor(self , color):
        if color == 'Blancas':
            self.pilas.datos.colorPc = 'negro'
        else:
            self.pilas.datos.colorPc = 'blanco'
        self.pilas.escenas.PantallaJuego(self.pilas)

    def salir(self):
        exit()