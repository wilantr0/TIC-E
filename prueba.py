import time as time
import os as os
print('-------------------------------------------------------------------------------------------------------------')
print('Hola benvingut a aquesta calculadora. No és una calculadora normal, et permet fer operacions de combinatòria.')
print('-------------------------------------------------------------------------------------------------------------')
time.sleep(3)
os.system('cls')


def factorial(n):
    return 1 if (n == 1 or n == 0) else n*factorial(n-1)


def comb():
    m = int(input('Quants elements tenim: '))
    print(' ')
    n = int(input('Quants elements agafem del total? '))
    print(' ')

    if m > n and n > 0:
        ordre = input("Importa l'ordre? ").upper()
        print(' ')

        if ordre == 'SI':
            repe = input('Es repeteixen els elements? ').upper()
            print(' ')

            if repe == 'SI':
                print('Surten un màxim de ' + m**n + ' combinacions')
            elif repe == 'NO':
                print(
                    f'Surten un màxim de {factorial(m)/factorial(m-n)} combinacions')
            else:
                print('Error en la presa de resposta... \n')
                comb()
        elif ordre == 'NO':
            print(
                f'Surten un màxim de {factorial(m)/(factorial(n)*factorial(m-n))} combinacions')
        else:
            print('Error a la presa de resposta... \n')
            comb()
    elif n == m:
        repe = input('Es repeteixen els elements? ').upper()
        print(' ')
        factos = 1
        if repe == 'SI':
            repes = input('Num elements repetits: ').split(', ')
            print(' ')

            for i in range(len(repes)):
                factos *= factorial(int(repes[i]))

            print(f'Surten un màxim de {factorial(m)/factos} combinacions')
        elif repe == 'NO':
            print(f'Surten un màxim de {factorial(m)} combinacions')
        else:
            print('Error en la presa de resposta... \n')
            comb()

    cont = input('Vols continuar? ').upper()

    if cont == 'SI':
        comb()
    else:
        pass


comb()
