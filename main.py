import pilasengine
from accessible_output import speech

from escena.pantallaJuego import PantallaJuego

# iniciamos:
pilas = pilasengine.iniciar(titulo='pydrez 0.1 - alpha', habilitar_mensajes_log=False)
s = speech.Speaker()

try:
    pilas.forzar_habilitacion_de_audio()
except AttributeError:
    print("Omitiendo forzar la inicializacion, version anterior a 1.4.8")


def decir(texto, interrumpir=True, visual=False):
  s.output(texto, interrupt=interrumpir)
def mover(x, y, actor):
  actor.x=actor.x+x
  actor.y=actor.y+y

pilas.escenas.vincular(PantallaJuego)
pilas.escenas.PantallaJuego(pilas=pilas, tts=decir)
pilas.ejecutar()
