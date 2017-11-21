from pilasengine.actores.actor import Actor

class BotonSiguienteDesafio(Actor):

    def iniciar(self, x=0, y=0, siguienteDesafio = '1'):
        self.x = x
        self.y = y
        self.imagen = "invisible.png"
        self.boton = self.pilas.interfaz.Boton("siguente desafio")
        self.boton.x = self.x
        self.boton.y = self.y
        self.boton.conectar(self.cuandoPulsanElBoton)
        self.nombreDesafio = siguienteDesafio


    def cuandoPulsanElBoton(self):
        self.pilas.escenas.Desafio(pilas=self.pilas, nombreDesafio=self.nombreDesafio)