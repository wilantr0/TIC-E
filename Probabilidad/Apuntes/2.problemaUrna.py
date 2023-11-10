import random as rd


class bcolor:
    ORANGE = "\033[93m"
    ENDC = "\033[0m"

"""
Se tienen dos urnas, y cada una de ellas contiene un número diferente de bolas blancas y rojas:
Primera urna, U1: 3 bolas blancas y 2 rojas;
Segunda urna, U2: 4 bolas blancas y 2 rojas.
Se realiza el siguiente experimento aleatorio:
  Se tira una moneda al aire y si sale cara se elige una bola de la primera urna, y si sale cruz de la segunda.
¿Cuál es la probabilidad de que salga una bola blanca?
"""
u1 = ['b', 'b', 'b', 'r', 'r']
u2 = ['b', 'b', 'b', 'b', 'r', 'r']

