# -*- encoding: utf-8 -*-
from .menu import EscenaMenu

class Configurar(EscenaMenu):

    def configuracion(self):
        self.menu_y = 190
        self.colorResaltado = self.pilas.colores.Color(0, 0, 0)
        self.colorNormal = self.pilas.colores.Color(255, 255, 255)
        self.distancia = 90
        self.texto = self.pilas.actores.Texto("Configuracion de pydrez:",y= 280,  magnitud= 25, fuente= "datos/tipografia/al.ttf")
        self.texto.color = self.colorResaltado

    def listaOpciones(self):
        lista = []
        if self.pilas.datos.musica is None:
            opcion = (u'musica off', self.musicaActivar)
        else:
            opcion = (u'musica on', self.musicaDesactivar)
        lista.append(opcion)

        if self.pilas.datos.fichasFx == "off":
            opcion = (u'Efectos off', self.modificarEfectos, "on")
        else:
            opcion = (u'Efectos on', self.modificarEfectos, "off")
        lista.append(opcion)

        return lista


    def activar(self):
        self.decir(u'pulse las flechas para moverse entre las opciones. pulse enter para modificar o escape para regresar al menu principal.', False)

    def cuandoPulsaEscape(self, evento):
        self.pilas.escenas.MenuPrincipal(pilas=self.pilas)

    def recargar(self):
        self.pilas.escenas.Configurar(self.pilas)

    def musicaActivar(self):
        self.pilas.datos.musica = self.pilas.musica.cargar('audio/presentacion.mp3')
        self.pilas.datos.musica.reproducir()
        self.recargar()

    def musicaDesactivar(self):
        self.pilas.datos.musica.detener()
        self.pilas.datos.musica = None
        self.recargar()

    def modificarEfectos(self, modo):
        self.pilas.datos.fichasFx = modo
        self.recargar()
