import pilasengine

from actores.botonIrAlMenu import BotonIrAlMenuPrincipal
from actores.botonSiguienteDesafio import BotonSiguienteDesafio


class PantallaJuegoTerminado(pilasengine.escenas.Escena):
    def iniciar(self, pilas, tiempo, nombreDesafio):
        self.siguienteDesafio = int(nombreDesafio) + 1
        self.textoDesafioTerminado = self.pilas.actores.Texto("Desafio "+ str(nombreDesafio) + " terminado " , magnitud=40)
        self.tiempoEnElDesafio = self.pilas.actores.Texto("tiempo: " + tiempo.texto, magnitud=40)
        self.textoDesafioTerminado.y = 100
        self.botonMenuPrincipal    = BotonIrAlMenuPrincipal(pilas,-150,-150)
        self.botonSiguienteDesafio = BotonSiguienteDesafio(pilas,x=150,y=-150,siguienteDesafio = str(self.siguienteDesafio))
