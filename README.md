# README
En este repositorio guardo los módulos en los que almaceno las funciones que voy creando.  

Algunas funciones en principio son bastante inútiles, ya que contienen los métodos predefinidos para hacer lo mismo, como es el caso de `replindex()` (que ejecuta `lista[i]='nuevo valor'` mediante inputs). En estos casos, me sirven más bien como chuletas para recordar el uso de estos métodos.

- *bucles*
    - *imputnumber*. Se pide un número, por ejemplo edad. Si el input no son dígitos, repite.
    - *devuelve*. Se le da una lista como argumento y muestra los elementos.
- *condicionales* 
    - *correoOK*. Determina si es un correo válido.
- *diccionarios*
    - *dictiozip*. Devuelve un diccionario a partir de dos listas equivalentes en número, en las cuales una contiene las claves y la otra los valores.
- *listas*
    - *replindex*. Cambia el elemento de una lista mediante su número indexado.
    - *replname*. Cambia el elemento de una lista mediante su nombre.
    - *bingo*. Devuelve True si un número está en una lista.
    - *stats*. Imprime varios atributos de una lista.
    - *creador*. Crea listas mediante inputs. Llama a la función con un input para el nombre. Luego la función `adicion()` añade elementos.
    - *adicion*. Añade elementos [str] a una lista ya creada. Sale escribiendo '_esc_'.
    - *elige*. Se le pide al usuario que escriba su opción escogida `mensaje` y si está en la `lista` imprime correcto. Si no, repite.
    - *itemsList*. Imprime los índices y elementos de una lista.
    - ~~*indexElem*. Muestra los índices y elementos de una lista.~~ Usar itemsList.
    - ~~*elemIndex*. Muestra los elementos de una lista y sus índices.~~ Usar itemsList.
    - ~~*cuantoshay*. Con una lista dada, encuentra las veces que aparece un elemento.~~ Mejor usar `lista.count("valor")`.
    - *generaNums*. Se da un límite para generar números aleatorios y crea una lista con ellos tan extensa como se especifique.
    - *cartesian*. Dadas 2 listas, devuelve las permutaciones posibles entre elementos.
- *mates*
    - *multiplicador*. Base para construir otras funciones multiplicadoras:
        - *doble*. x2
        - *triple*. x3
    - *fibo1*. Un generador de secuencias de Fibonacci que está regular. Pendiente de actualizar por otro mejor. 

- *cambiafechas*. Al ejecutar pide un archivo que contenga fechas en formato `d mes aaaa` (p. ej.: '1 enero 2022') y devuelve un documento de texto con solo las fechas en formato `aaaa-mm-dd` ('2022-01-01'), una por línea. 

creado: `220313`
última modificación: `220411`