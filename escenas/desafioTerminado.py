import pilasengine


class PantallaJuegoTerminado(pilasengine.escenas.Escena):
    def iniciar(self, pilas, tiempo, nombreDesafio):
        self.nombreDesafio = int(nombreDesafio)
        self.textoDesafioTerminado = self.pilas.actores.Texto("Desafio "+ str(nombreDesafio) + " terminado " , magnitud=40)
        self.tiempoEnElDesafio = self.pilas.actores.Texto("tiempo: " + tiempo.texto, magnitud=40)
        self.siguienteDesafio = self.pilas.actores.Texto("Siguiente Desafio [s]", magnitud=15)
        self.salir = self.pilas.actores.Texto("Ir la Menu Principal [esc]", magnitud=15)
        self.textoDesafioTerminado.y = 100
        self.siguienteDesafio.y = -150
        self.siguienteDesafio.x = +150
        self.salir.y = -150
        self.salir.x = -150
        self.pilas.eventos.pulsa_tecla.conectar(self.interpreta_teclado)

    def interpreta_teclado(self, evento):
        if evento.codigo == "a" or evento.codigo == self.pilas.simbolos.IZQUIERDA:
            print("chau")
        if evento.codigo == "d" or evento.codigo == self.pilas.simbolos.DERECHA:
            print("hola")


