# Python 3.10.2 UTF-8
# Copyright (c) 2022, Noa Velasco

def correoOK(correo):
    """Determina si es un correo válido. V.2"""

    arroba = 0
    punto = False
    letras = 1

    for i in correo:
        if (i == "@"):
            arroba = arroba+1
        elif (i == "."):
            punto = True
        elif (i == "_"):
            pass
        elif i.isalnum() == False:
            letras -= 1

    if arroba == 1 and punto == True and letras > 0:
        print("La dirección es válida")
    else:
        print("No es una dirección válida")
