# def factorial(n):
#     i = 1
#     fact = 1
#     while i < n+1:
#         fact = fact*i
#         i += 1

#     print(fact)


def primo(n):
    i = 1
    primo = []
    while i < n+1:
        par = n % 2
        if par == 0:
            break

        comprove = n % i

        if comprove == 0:
            primo.append(i)
            i += 1
        else:
            i += 1
    if len(primo) == 2:
        print('Es primo')
    else:
        print('No es primo')


# fas = int(input('Numero per fer el factorial: '))

# factorial(fas)

primo(10)
