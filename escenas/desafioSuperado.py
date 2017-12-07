# -*- encoding: utf-8 -*-
import pilasengine
from tts import leer
from sonido import Sonido

class DesafioSuperado(pilasengine.escenas.Escena):

    def iniciar(self, pilas, tiempo, nombreDesafio):
        marronOscuro = pilas.colores.Color(77, 38, 22)
        self.nombreDesafio = str(int(nombreDesafio) + 1)
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/fondoJuego.jpg")
        self.textoDesafioTerminado = self.pilas.actores.Texto("Desafio "+ str(nombreDesafio) + " terminado " , magnitud=40,fuente= "datos/tipografia/anirb___.ttf" )
        self.tiempoEnElDesafio = self.pilas.actores.Texto("tiempo: " + tiempo.texto, magnitud=40,fuente= "datos/tipografia/anirb___.ttf")
        self.textoDesafioTerminado.y = 100
        self.textoDesafioTerminado.color = marronOscuro
        self.tiempoEnElDesafio.color = marronOscuro

        self.botonMenuPrincipal = pilas.interfaz.Boton("ir al menu Principal")
        self.botonMenuPrincipal.x = -150
        self.botonMenuPrincipal.y = -150
        self.botonMenuPrincipal.conectar(self.menuPrincipal)


        self.botonSiguienteDesafio = pilas.interfaz.Boton("siguiente desafio")
        self.botonSiguienteDesafio.x = 150
        self.botonSiguienteDesafio.y = -150

        self.botonSiguienteDesafio.conectar(self.siguienteDesafio)

        # eventos:
        self.pilas.eventos.pulsa_tecla_escape.conectar(self.menuPrincipal)
        self.pilas.eventos.pulsa_tecla.conectar(self.interpretaTeclado)

        mensaje = "¿Desafio superado!. (pulsa enter para ir al siguiente desafio o escape para ir al menu principal)"
        leer(mensaje, False)
        audio = Sonido("audio/logro.ogg")
        audio.reproducir_esperando()

    def siguienteDesafio(self):
        self.sonido_activar = Sonido("audio/menu_enter.ogg")
        self.sonido_activar.volumen = 0.3
        self.sonido_activar.reproducir_esperando()
        self.pilas.escenas.Desafio(pilas=self.pilas, nombreDesafio=self.nombreDesafio)

    def menuPrincipal(self, evento=None):
        self.pilas.escenas.MenuPrincipal(self.pilas)

    def interpretaTeclado(self, evento):
        if evento.codigo == self.pilas.simbolos.SELECCION:
            self.siguienteDesafio()