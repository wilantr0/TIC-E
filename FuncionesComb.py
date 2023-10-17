def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


def Perm(m):
    return factorial(m)


def PermR(m=[]):
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
