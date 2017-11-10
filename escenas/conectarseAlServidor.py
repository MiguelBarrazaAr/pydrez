# -*- encoding: utf-8 -*-
import pilasengine

class ConectarseAlServidor(pilasengine.escenas.Escena):

    def iniciar(self, pilas):
        self.texto = pilas.actores.Texto("Escriba La IP del servidor que se quiere conectar")
        self.entrada = pilas.interfaz.IngresoDeTexto()
        self. entrada.y = -60
