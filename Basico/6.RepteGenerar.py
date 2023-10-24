import random


def generar(min, max, n):
    elements = []
    for i in range(n):
        elements.append(random.randint(min, max))

    return elements


min = int(input('Valor Minimo: '))
max = int(input('Valor Máximo: '))
n = int(input('Número de valores: '))
print(generar(min, max, n))
