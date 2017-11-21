from pilasengine.actores.actor import Actor

class BotonIrAlMenuPrincipal(Actor):

    def iniciar(self, x=0, y=0):
        self.x = x
        self.y = y
        self.imagen = "invisible.png"
        self.boton = self.pilas.interfaz.Boton("ir al menu Principal")
        self.boton.x = self.x
        self.boton.y = self.y
        self.boton.conectar(self.cuandoPulsanElBoton)

    def cuandoPulsanElBoton(self):
        self.pilas.escenas.MenuPrincipal(pilas=self.pilas)