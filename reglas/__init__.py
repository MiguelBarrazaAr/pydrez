# -*- encoding: utf-8 -*-
from .ajedrez_tradicional import ReglasAjedrezTradicional
from .ajedrez_8x12 import ReglasAjedrez8x12
from .ajedrez_atomico import ReglasAjedrezAtomico
from .ajedrez_epico import ReglasAjedrezEpico
from .ajedrez_minado import ReglasAjedrezMinado
from .ajedrez_salvaje import ReglasAjedrezSalvaje
from .ajedrez_con_rio import ReglasAjedrezConRio
from .ajedrez_lago_de_lava import ReglasAjedrezConLagoDeLava


from .puzzleAjedrez import PuzzleAjedrez

definiciones = {
    "ajedrez8x12":ReglasAjedrez8x12,
    "ajedrez_con_rio":ReglasAjedrezConRio,
    "atomico":ReglasAjedrezAtomico,
    "epico":ReglasAjedrezEpico,
    "ajedrez_lago_de_lava":ReglasAjedrezConLagoDeLava,
    "minado":ReglasAjedrezMinado,
    "salvaje":ReglasAjedrezSalvaje,
    "tradicional":ReglasAjedrezTradicional,
    "puzzle":PuzzleAjedrez,

}

def generar(clave):
    return definiciones[clave]