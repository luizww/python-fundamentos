lista=[ ]
pares=[ ]
impares=[ ]
c=0
while True:
    add=int(input('Digite um valor: '))
    p=input('Deseja continuar? [S/N].').lower()
    if add % 2 == 0 and add not in lista:
        c += 1
        pares.append(add)
        lista.append(add)
    elif add %2 == 1 and add not in lista:
        c += 1
        impares.append(add)
        lista.append(add)
    if p == 'n':
        break
print(f'Voce digitou {c} numeros,eles foram {lista},dentre destes os numeros {pares} são pares e os numeros {impares} são impares')