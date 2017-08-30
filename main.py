import pilasengine
from accessible_output import speech

#import pantallaJuego
from actor.tablero import Tablero
from logica.ajedrez_basico import armarAjedrezBasico


# iniciamos:
pilas = pilasengine.iniciar(titulo='test')
s = speech.Speaker()

try:
    pilas.forzar_habilitacion_de_audio()
except AttributeError:
    print("Omitiendo forzar la inicializacion, version anterior a 1.4.8")

tablero = Tablero(pilas, alto=8, ancho=8, x=-120, y=-120)
armarAjedrezBasico(pilas, tablero)

def decir(texto, interrumpir=True, visual=False):
  s.output(texto, interrupt=interrumpir)
def mover(x, y, actor):
  actor.x=actor.x+x
  actor.y=actor.y+y


pilas.ejecutar()
