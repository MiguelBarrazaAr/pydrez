import pilasengine

class DesafioSuperado(pilasengine.escenas.Escena):

    def iniciar(self, pilas, tiempo, nombreDesafio):
        self.nombreDesafio = str(int(nombreDesafio) + 1)
        self.textoDesafioTerminado = self.pilas.actores.Texto("Desafio "+ str(nombreDesafio) + " terminado " , magnitud=40)
        self.tiempoEnElDesafio = self.pilas.actores.Texto("tiempo: " + tiempo.texto, magnitud=40)
        self.textoDesafioTerminado.y = 100

        self.botonMenuPrincipal = pilas.interfaz.Boton("ir al menu Principal")
        self.botonMenuPrincipal.x = -150
        self.botonMenuPrincipal.y = -150
        self.botonMenuPrincipal.conectar(self.menuPrincipal)

        self.botonSiguienteDesafio = pilas.interfaz.Boton("siguiente desafio")
        self.botonSiguienteDesafio.x = 150
        self.botonSiguienteDesafio.y = -150
        self.botonSiguienteDesafio.conectar(self.siguienteDesafio)

    def siguienteDesafio(self):
        self.pilas.escenas.Desafio(pilas=self.pilas, nombreDesafio=self.nombreDesafio)

    def menuPrincipal(self):
        self.pilas.escenas.MenuPrincipal(pilas=self.pilas)
