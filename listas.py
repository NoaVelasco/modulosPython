# Python 3.10.2 UTF-8
# Copyright (c) 2022, Noa Velasco


def replindex(lista):
    """Str. Cambiar el elemento de una lista mediante su número indexado"""
    
    print(lista)

    orden = int(input("index: "))
    valor = input("nuevo valor: ")

    lista[orden] = valor
    print(lista)


def replname(lista):
    """Str. Cambiar el elemento de una lista mediante su nombre"""
    
    print(lista)

    buscar = input("elemento a buscar: ")
    valor = input("elemento a reemplazar: ")

    lista[lista.index(buscar)] = valor

    print(lista)


def bingo(lista):
    """Int. ¿Está el número en la lista?"""

    buscanum = int(input())
    if buscanum in lista:
        print("True")
    else:
        print("False")


def stats(lista):
    """Imprime varios atributos de una lista"""

    print(lista)
    print("La lista contiene", len(lista), "elementos")
    print("Su valor mínimo es", min(lista))
    print("Su valor máximo es", max(lista))
    print("La suma de sus valores es", sum(lista))
    print("La media de sus valores es", sum(lista)/len(lista))


def creador(nombre):
    """
    Crea listas [str] mediante inputs.
    Llamar a la función con input para el nombre.
    Luego la función adicion() añade elementos.
    """

    nombre = []
    adicion(nombre)
    print(nombre)


def adicion(lista):
    """Añade elementos [str] a una lista ya creada. Sale escribiendo '_esc_'."""

    bucle = True

    while bucle:
        x = input("Añade un elemento a la lista o escribe '_esc_' para salir")
        if x == "_esc_":
            bucle = False
        else:
            lista.append(x)


def elige(lista, mensaje):
    """
    Se le pide al usuario que escriba su opción escogida <mensaje>
    y si está en la <lista> imprime correcto. Si no, repite.
    """

    userInput = input(mensaje).lower()

    while userInput not in lista:
        print("Escríbelo otra vez, por favor.")
        userInput = input(mensaje)

        # otras opciones------------------
        # minúsculas:
        #userInput = input(mensaje).lower()
        # mayúsculas:
        #userInput = input(mensaje).upper()
    # números:
    #while userInput.isdigit() == False:

    print("Correcto.")


def indexElem(lista):
    """Muestra los índices y elementos de una lista."""

    contador = 0
    for i in lista:
        print(f"[{contador}] = {i}")
        contador += 1


def elemIndex(lista):
    """Muestra los elementos de una lista y sus índices."""

    for i in range(len(lista)):
        print(f"{lista[i]} = [{i}]")



def cuantoshay(lista, buscar):
    """Con una lista dada, encuentra las veces que aparece un elemento"""

    numveces = 0
    for i in lista:
        if(i == buscar):
            numveces += 1
    print("Número de coincidencias:", numveces)

