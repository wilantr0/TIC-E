class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# REPTE 1: programa que sumi els números del 1 al 10 amb While
count = 0
sum = 0
while count <= 10:
    sum += count
    count += 1
print(sum)
# REPTE 2: programa que sumi els números parells del 1 al 20 amb While
count = 0
sum = 0
while count <= 21:
    if count % 2 == 0:
        sum += count
        count += 1
    else:
        count += 1
print(sum)
# REPTE 3: programa que demana al usuari un valor d'inici i un valor final, i que sumi els valors múltiples de tres de tot l'interval.
min_val = int(input('Valor Minimo: '))
max_val = int(input('Valor Maximo: '))
sum = 0
while min_val <= max_val:
    if min_val % 3 == 0:
        sum += min_val
        min_val += 1
    else:
        min_val += 1

print(sum)
# REPTE 4:Programa que ens demana una contrasenya i que no ens deixa entrar fins que no la escribim correctament.
contraseña = ''
contraseñaCorrecta = input('Contraseña: ')
while contraseña != contraseñaCorrecta:
    contraseña = input(bcolors.WARNING+'Repite la contraseña: '+bcolors.ENDC)

    if contraseña != contraseñaCorrecta:
        print(bcolors.FAIL+'Contraseña Incorrecta. Vuelva a intentralo.'+bcolors.ENDC)
    else:
        print(bcolors.OKGREEN+'Contraseña Correcta. Bienvenido'+bcolors.ENDC)
