import time as time
import os as os

os.system("cls")


def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


def Perm(m):
    return factorial(m)


def PermR(m):
    num = m[0]
    perm = 0

    for i in range(len(m)):
        if i == 0:
            pass
        else:
            perm += factorial(m[i])

    return factorial(num) / perm


def Var(m, n):
    return factorial(m) / factorial(m - n)


def VarR(m, n):
    return m**n


def Comb(m, n):
    return factorial(m) / (factorial(n) * factorial(m - n))


def comb():
    m = int(input("Quants elements tenim: "))
    print(" ")
    n = int(input("Quants elements agafem del total? "))
    print(" ")

    if m > n and n > 0:
        ordre = input("Importa l'ordre? ").upper()
        print(" ")

        if ordre == "SI":
            repe = input("Es repeteixen els elements? ").upper()
            print(" ")

            if repe == "SI":
                print("Surten un màxim de " + VarR(m, n) + " combinacions")
            elif repe == "NO":
                print(f"Surten un màxim de {Var(m, n)} combinacions")
            else:
                print("Error en la presa de resposta... \n")
                comb()
        elif ordre == "NO":
            print(f"Surten un màxim de {Comb(m, n)} combinacions")
        else:
            print("Error a la presa de resposta... \n")
            comb()
    elif n == m:
        repe = input("Es repeteixen els elements? ").upper()
        print(" ")
        if repe == "SI":
            reps = [m]
            rep = int(input("Cuantos elementos se repiten? "))
            for i in range(rep):
                ns = int(
                    input("Cuantas veces se repite el elemento nº " + str(i + 1) + " ")
                )
                reps.append(ns)
            print(f"Surten un màxim de {PermR(reps)} combinacions")
        elif repe == "NO":
            print(f"Surten un màxim de {Perm(m)} combinacions")
        else:
            print("Error en la presa de resposta... \n")
            comb()

    cont = input("Vols continuar? ").upper()

    if cont == "SI":
        comb()
    else:
        os.system("cls")
        print("Adeu, fins la propera!")
        time.sleep(2)
        os.system("cls")


comb()
