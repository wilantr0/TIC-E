import random


def probabilidad(coincidencias, simulaciones):
    return coincidencias / simulaciones


def coincidencia(alumnes):
    alumnescoin = set(alumnes)
    coincidencias = len(alumnes) - len(alumnescoin)
    return coincidencias


def simulacion(sim, alumn):
    counter = 0
    for simulaciones in range(sim):
        alumnes = []
        for i in range(alumn):
            alumnes.append(random.randint(1, 365))
        coincidencias = coincidencia(alumnes)
        counter += coincidencias
    print(probabilidad(counter, sim))


simulacion(10000, 23)
