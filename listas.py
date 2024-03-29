# Python 3.10.2 UTF-8
# Copyright (c) 2022, Noa Velasco


from random import randint


def replindex(lista):
    """Str. Cambiar el elemento de una lista mediante su número indexado"""

    orden = int(input("index: "))
    valor = input("nuevo valor: ")

    lista[orden] = valor
    return lista


def replname(lista):
    """Str. Cambiar el elemento de una lista mediante su nombre"""
    print(lista)

    buscar = input("elemento a buscar: ")
    valor = input("elemento a reemplazar: ")

    lista[lista.index(buscar)] = valor

    return lista


def bingo(lista):
    """Int. ¿Está el número en la lista?"""
    buscanum = int(input())
    if buscanum in lista:
        print("¡Bingo! :)")
    else:
        print("¡Agua! :(")


def stats(lista):
    """Imprime varios atributos de una lista"""
    print(lista)
    print("La lista contiene", len(lista), "elementos")
    print("Su valor mínimo es", min(lista))
    print("Su valor máximo es", max(lista))
    print("La suma de sus valores es", sum(lista))
    print("La media de sus valores es", sum(lista)/len(lista))  # numpy.mean()
    print("El mediano de sus valores es", sorted(
        lista)[len(lista)//2])  # numpy.median()
    # por hacer: scipy.stats.mode: el valor más repetido


def creador():
    """
    Crea listas [str] mediante inputs.
    Llamar a la función dentro de una variable que será la lista.
    Luego la función adicion() añade elementos.
    """
    nombre = []
    adicion(nombre)
    return nombre


def adicion(lista):
    """Añade elementos [str] a una lista ya creada. Sale escribiendo 'ESC'."""
    bucle = True

    while bucle:
        x = input("Añade un elemento a la lista o escribe 'ESC' para salir: ")
        if x == "ESC":
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
    # while userInput.isdigit() == False:

    print("Correcto.")

# Mejor usar itemsList()
# def indexElem(lista):
#     """Muestra los índices y elementos de una lista."""
#     contador = 0
#     for i in lista:
#         print(f"[{contador}] = {i}")
#         contador += 1


# Mejor usar itemsList()
# def elemIndex(lista):
#     """Muestra los elementos de una lista y sus índices."""
#     for i in range(len(lista)):
#         print(f"{lista[i]} = [{i}]")


def itemsList(lista):
    """Imprime los índices y elementos de una lista."""
    for i in lista:
        print(f"[{lista.index(i)}]: {i}")


# Mejor usar lista.count("buscar")
# def cuantoshay(lista, buscar):
#     """Con una lista dada, encuentra las veces que aparece un elemento"""
#     # También se puede hacer con re.findall:
#     # coincidencias = re.findall(buscar, str(lista))
#     # print("Número de coincidencias:", len(coincidencias))
#     numveces = 0
#     for i in lista:
#         if(i == buscar):
#             numveces += 1
#     # print("Número de coincidencias:", numveces)
#     return numveces


def generaNums():
    """
    Se da un límite para generar números aleatorios
    y crea una lista con ellos tan extensa como se especifique.
    """
    cont = 1
    miLista = []
    limite = int(input("Rango de 1 a"))
    extension = int(input("Extensión de la lista"))

    while cont < extension:
        miLista.append(randint(1, limite))
        cont = cont+1
    return miLista


def cartesian(list1, list2):
    """Dadas 2 listas, devuelve las permutaciones posibles entre elementos."""
    cartesList = [[a, b] for a in list1 for b in list2]
    return cartesList
