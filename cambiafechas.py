# Python 3.10.2 UTF-8
# Copyright (c) 2022, Noa Velasco

# Selecciona fechas formato d mes aaaa y
# escribe en un documento una a una formato aaaa-mm-dd

import re


archivo = input("Introduce nombre con extensión del archivo: ")
#archivo=("fechas.txt")

meses = {"01": "enero", "02": "febrero", "03": "marzo",
         "04": "abril", "05": "mayo", "06": "junio",
         "07": "julio", "08": "agosto", "09": "septiembre",
         "10": "octubre", "11": "noviembre", "12": "diciembre"}


def recogeFechas(fecha):
    """Crea un patrón con las fechas escritas y devuelve una lista."""
    patron = re.compile(r'(\d*) (\w+) (\d{4})')
    creaLista = re.findall(patron, fecha)
    return creaLista


def get_key(val):
    """
    Compara los meses con los del diccionario.
    Si coinciden (valores), los pasa a números (claves).
    """
    for key, value in meses.items():
        if val.lower() == value:
            return key

    return "No es un mes válido"


with open(archivo, encoding='utf-8') as f:
    cadenaTexto = f.read()


listaFechas = recogeFechas(cadenaTexto)

listaFormat = []

for i in listaFechas:
    dia, mes, anio = i
    if len(dia) == 1:
        dia = "0" + dia

    mesNum = get_key(mes)
    if len(mesNum) == 1:
        mesNum = "0" + mesNum

    listaFormat.append(f"{anio}-{mesNum}-{dia}")

STRING = ''.join([str(item + "\n") for item in listaFormat])
with open("formato_fechas.txt", "w", encoding="utf-8") as ft:
    ft.write(STRING)
