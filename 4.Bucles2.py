import random

elements = []
for i in range(100):
    elements.append(random.randint(1, 6))

print(elements)

for k in range(1, 7):
    num = 0
    for i in range(len(elements)-1):
        if elements[i] == elements[i+1] and elements[i] == k:
            num += 1
    print(str(k) + ': ' + str(num))


for j in range(1, 7):
    v = 0
    for i in elements:
        if i == j:
            v += 1

    print('Cuantos '+str(j)+' hay?: '+str(v))
