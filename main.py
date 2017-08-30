import pilasengine
from accessible_output import speech

#import pantallaJuego
from actor.tablero import Tablero
from actor.reina import Reina

# iniciamos:
pilas = pilasengine.iniciar(titulo='test')
s = speech.Speaker()

try:
    pilas.forzar_habilitacion_de_audio()
except AttributeError:
    print("Omitiendo forzar la inicializacion, version anterior a 1.4.8")

tablero = Tablero(pilas, alto=8, ancho=8)
reina = Reina(pilas)

def decir(texto, interrumpir=True, visual=False):
  s.output(texto, interrupt=interrumpir)
def mover(x, y, actor):
  actor.x=actor.x+x
  actor.y=actor.y+y

def pulsado(evento):
  m=30
  if evento.codigo == "a":
    # mover a la izquierda:
    mover(-m, 0, reina)
    #decir(reina.x)
  elif evento.codigo == "d":
    # mover a la derecha
    mover(m, 0, reina)
    #decir(reina.x)



pilas.eventos.pulsa_tecla.conectar(pulsado)

pilas.ejecutar()
