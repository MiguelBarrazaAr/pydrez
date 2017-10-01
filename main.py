import pilasengine
from accessible_output import speech

from escenas.menu_principal import MenuPrincipal
from escenas.pantallaJuego import PantallaJuego
from escenas.desafio import Desafio

# iniciamos:
pilas = pilasengine.iniciar(titulo='pydrez 0.1 - alpha', capturar_errores=False, habilitar_mensajes_log=False)
s = speech.Speaker()

def decir(texto, interrumpir=True, visual=False):
    s.output(texto, interrupt=interrumpir)

# vinculamos las pantallas:
pilas.escenas.vincular(MenuPrincipal)
pilas.escenas.vincular(PantallaJuego)
pilas.escenas.vincular(Desafio)

pilas.escenas.MenuPrincipal(pilas=pilas, tts=decir)
#pilas.escenas.PantallaJuego(pilas=pilas, tts=decir)

pilas.ejecutar()
