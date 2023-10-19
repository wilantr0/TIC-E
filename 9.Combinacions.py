from FuncionesComb import *

"""Tens 7 amics i desitges formar un comitè de 4 persones per a un projecte.
No obstant això, dos dels teus amics, Juan i María,
no poden treballar junts a causa de diferències personals.
Quantes formes diferents hi ha de seleccionar el comitè?"""
print(Comb(7, 2))

"""Cuantes permutacions diferents es poden formar amb les lletres de la paraula "COMBINATÒRIA"?"""
print(PermR([12, 2, 2, 2]))

"""En un concurs de cuina, hi ha 5 ingredients i els participants han de crear plats de 2 ingredients. Quantes variacions diferents de plats es poden fer?"""
print(Var(5, 2))

"""Tens 5 llibres de matemàtiques i 4 llibres d'història. Quantes formes diferents hi ha d'ordenar els llibres en una prestatgeria si els llibres de la mateixa matèria han d'estar junts?"""
print(Perm(5) * Perm(4) * Perm(2))
