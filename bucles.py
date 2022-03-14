# Python 3.10.2 UTF-8
# Copyright (c) 2022, Noa Velasco

def inputnumber():
    """
    Se pide un número, por ejemplo edad. 
    Si el input no son dígitos, repite. 
    """

    edad = input("Introduce el número: ")

    while(edad.isdigit() == False):  # este permite saber si es número
        edad = input("Introduce el número con cifras: ")

    print("Correcto.")


def devuelve(*varios):
    """Se le da una lista como argumento y muestra los elementos."""

    for elemento in varios:
        yield elemento

#eco = devuelve(lista)
#print(next(eco))
#print(next(eco))
#print(next(eco))

