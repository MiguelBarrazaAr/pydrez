# -*- encoding: utf-8 -*-

from .rio import TableroRio
from .lagoDeLava import TableroLagoDeLava

definiciones = {
    "rio":TableroRio,
    "lagoDeLava":TableroLagoDeLava
}

def generar(clave):
    return definiciones[clave]
