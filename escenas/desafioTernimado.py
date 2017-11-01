import pilasengine


class PantallaJuegoTerminado(pilasengine.escenas.Escena):
    def iniciar(self, pilas, tiempo, nombreDesafio):
        self.nombreDesafio = int(nombreDesafio)
        self.texto_codigo = self.pilas.actores.Texto("Juego Terminado", magnitud=40)
        self.texto_codigo2 = self.pilas.actores.Texto("tiempo: " + tiempo.texto, magnitud=40)
        self.texto_codigo.y = 100
