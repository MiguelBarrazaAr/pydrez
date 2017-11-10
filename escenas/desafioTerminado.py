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
        self.pilas.eventos.click_de_mouse.conectar(self.click_mouse)
        self.pilas.eventos.pulsa_tecla_escape.conectar(self.activar_menu_principal)

