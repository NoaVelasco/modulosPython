# Python 3.10.2 UTF-8
# Copyright (c) 2022, Noa Velasco

def multiplicador(n):
    """Base para construir otras funciones multiplicadoras"""

    return lambda a: a * n


doble = multiplicador(2)
triple = multiplicador(3)
