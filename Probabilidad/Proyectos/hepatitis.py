noHepatits = set()


def crearSet(sett, length):
    sett = set()
    sett = {i for i in range(1, length + 1)}
    return sett


print(crearSet("hepatitis", 1000))
