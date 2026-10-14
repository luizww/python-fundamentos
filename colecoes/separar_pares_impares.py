lista=[[], []]
for p in range(0 , 7):
    p1=int(input(f'Digite um numero para a {p + 1} posição: '))
    if p1 % 2 == 0:
        lista[0].append(p1)
    else:
        lista[1].append(p1)
lista[0].sort()
lista[1].sort()
print(f'Os numeros pares em ordem crescente são:{lista[0]} e os impares em ordem crescente são:{lista[1]}')