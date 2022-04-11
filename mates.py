# Python 3.10.2 UTF-8
# Copyright (c) 2022, Noa Velasco

def multiplicador(n):
    """Base para construir otras funciones multiplicadoras"""

    return lambda a: a * n


doble = multiplicador(2)
triple = multiplicador(3)


def fibo1(n):
    """Imprime la sucesión desde 0 a tantas veces como n."""

    a = 0
    b = 1

    if n <= 0:
        return "Debe ser mayor que 0"

    if n == 1:
        return 0

    if n == 2:
        print(0)
        return 1

    print(0)
    for i in range(2, n):
        suma = a+b
        a = b
        b = suma
        print(a)
    return b
