"""Es tenen dues urnes, i cadascuna conté un nombre diferent de boles blanques i vermelles:
Primera urna, U1: 3 boles blanques i 2 vermelles;
Segona urna, U2: 4 boles blanques i 2 vermelles.
Es realitza el següent experiment aleatori:
Es llença una moneda a l'aire i si surt cara es tria una bola de la primera urna, i si surt creu de la segona.
Quina és la probabilitat que surti una bola blanca?"""

import random

urna1 = [0, 0, 1, 1, 1]
urna2 = [0, 0, 1, 1, 1, 1]
counter = 0
simulacions = 1000


def simulacio(simulacions, urnas, counter):
    for i in range(simulacions):
        if random.randint(1, 2) == 1:
            if random.choice(urnas[0]):
                counter += 1
        else:
            if random.choice(urnas[1]):
                counter += 1
    return counter


def probabilitat(resultat, simulacions):
    return resultat / simulacions


resultat = simulacio(simulacions, [urna1, urna2], counter)
print(probabilitat(resultat, simulacions))
