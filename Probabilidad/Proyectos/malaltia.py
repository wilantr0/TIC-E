"""Has de programar una simulació amb Python del següent problema.
Una anàlisi de sang de laboratori té una eficàcia del 95% per detectar una determinada malaltia quan, de fet, és present. Tot i això, la prova també dóna un resultat "fals positiu" per al 1% de les persones sanes analitzades. (És a dir, si es fa la prova a una persona sana, aleshores, amb una probabilitat del resultat de la prova implicarà que té la malaltia). Si el 5% de la població en realitat té la malaltia, quina és la probabilitat que una persona té la malaltia atès que el resultat de la prova és positiu?"""


def crearPoblacio(habitants):
    poblacio = []
    for i in range(1, habitants + 1):
        poblacio.append(i)
    return poblacio


def simulador(simulacions, poblacio, percentatges):
    m = percentatges[0] * (len(poblacio) / 100)

    for i in range(simulacions):
        percentatgeMalalts = poblacio[: int(m)]
        percentatgeNoMalalts = poblacio[int(m) :]

        mp = percentatges[1] * (len(percentatgeMalalts) / 100)
        nmp = percentatges[2] * (len(percentatgeNoMalalts) / 100)

        noMalaltsPositius = percentatgeNoMalalts[: int(nmp)]
        malaltsPositius = percentatgeMalalts[: int(mp)]

        probMalaltsPositius = len(malaltsPositius) / len(poblacio)
        probabilitat = probMalaltsPositius / (
            probMalaltsPositius + len(noMalaltsPositius) / len(poblacio)
        )

    return probabilitat


poblacio = crearPoblacio(10000)
print(simulador(1000, poblacio, [5, 95, 1]))
