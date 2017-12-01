# -*- encoding: utf-8 -*-
from .ajedrez_tradicional import ReglasAjedrezTradicional
from .ajedrez_atomico import ReglasAjedrezAtomico
from .ajedrez_epico import ReglasAjedrezEpico
from .ajedrez_minado import ReglasAjedrezMinado
from .ajedrez_salvaje import ReglasAjedrezSalvaje

from .puzzleAjedrez import PuzzleAjedrez

definiciones = {
    "atomico":ReglasAjedrezAtomico,
    "epico":ReglasAjedrezEpico,
    "minado":ReglasAjedrezMinado,
    "salvaje":ReglasAjedrezSalvaje,
    "tradicional":ReglasAjedrezTradicional,
    "puzzle":PuzzleAjedrez,

}

def generar(clave):
    return definiciones[clave]