import pilasengine

from escenas.menuPrincipal import MenuPrincipal
from escenas.pantallaJuego import PantallaJuego
from escenas.menuPromocion  import MenuPromocion
from escenas.menuDesafios import Desafios
from escenas.desafio import Desafio

# iniciamos:
pilas = pilasengine.iniciar(titulo='pydrez 0.1 - alpha', capturar_errores=False, habilitar_mensajes_log=False)

# vinculamos las pantallas:
pilas.escenas.vincular(MenuPrincipal)
pilas.escenas.vincular(PantallaJuego)
pilas.escenas.vincular(MenuPromocion)
pilas.escenas.vincular(Desafios)
pilas.escenas.vincular(Desafio)

pilas.escenas.MenuPrincipal(pilas=pilas)
#pilas.escenas.PantallaJuego(pilas=pilas)

pilas.ejecutar()
