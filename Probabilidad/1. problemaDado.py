import random as rd


class bcolor:
    ORANGE = "\033[93m"
    ENDC = "\033[0m"


"""-Vamos a simular un ejercicio típico de probabilidad. Usaremos siempre el mismo enfoque:
-Escribimos una función aleatoria: devuelve el resultado de simular el experimento una vez.
-El resultado es distinto cada vez que llamamos a la función, y las distintas llamadas son
  independientes (por ahora nos conformaremos con una noción intuitiva de independencia:
  las llamadas son independientes porque el resultado de una llamada no nos ayuda a predecir
  el resultado de llamar una segunda vez).
  Es necesario ser capaces de simular el resultado del experimento usando las funciones
  del módulo random (más adelante estudiaremos otras opciones).
-Recogeremos una muestra de tamaño finito, llamando a la función anterior un número N de veces.
-Si queremos calcular la probabilidad de un suceso A , necesitaremos una función que
  recibe como argumento un elemento x del espacio muestral, y devuelve True si x pertenece
  al suceso A, y False en caso contrario.
-Nuestra aproximación a la probabilidad del suceso A es la proporción de elementos de la
  muestra que pertenecen a A (#casos favorables / tamaño de la muestra)."""

lanzamientos = 10000


def lanzarDado():
    return rd.randint(1, 6)


muestra = []

for i in range(lanzamientos):
    muestra.append(lanzarDado())


def locate(A):
    count = 0
    for i in muestra:
        if A == i:
            count += 1
    return count


for i in range(1, 7):
    print(bcolor.ORANGE, i, bcolor.ENDC, ((locate(i) / lanzamientos) * 100), "%")
