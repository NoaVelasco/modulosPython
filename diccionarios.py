# Python 3.10.2 UTF-8
# Copyright (c) 2022, Noa Velasco


def dictiozip(listaClaves, listaValores):
    """
    Devuelve un diccionario a partir de dos listas equivalentes
    en número en las cuales una contiene las claves y la otra los valores.
    """
    diccionario = {clave: valor for (
        clave, valor) in zip(listaClaves, listaValores)}
    return diccionario
