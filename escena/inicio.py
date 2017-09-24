import pilasengine

class Inicio(pilasengine.escenas.Escena):

    def iniciar(self, pilas, tts):
        self.fondo = pilas.fondos.FondoMozaico("imagenes/fondo/madera.jpg")
        self.decir = tts
        self.menu = pilas.actores.Menu(y = 50 , opciones = [('jugar', self.jugar),('conectarse', self.conectarse),('tutorial', self.tutorial),('creditos', self.creditos),('salir', self.salir)])

    def jugar(self):
        print("jugar")

    def conectarse(self):
        print("conectarse")

    def tutorial(self):
        print("tutorial")

    def creditos(self):
        print("creditos")

    def salir(self):
        exit()