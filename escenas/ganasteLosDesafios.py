# -*- encoding: utf-8 -*-
import pilasengine
from tts import leer
from sonido import Sonido

class GanasteLosDesafios(pilasengine.escenas.Escena):

    def iniciar(self, pilas):
        marronOscuro = pilas.colores.Color(77, 38, 22)
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/fondoJuego.jpg")
        self.textoCreditos = self.pilas.actores.Texto("superaste los desafios",y= 100, magnitud= 30,fuente= "datos/tipografia/anirb___.ttf" )
        self.textoCreditos.y = 0
        self.textoCreditos.color = marronOscuro
        self.pilas.eventos.pulsa_tecla_escape.conectar(self.activar_menu_principal)


    def activar_menu_principal(self, evento=None):
        self.pilas.escenas.MenuPrincipal(self.pilas)