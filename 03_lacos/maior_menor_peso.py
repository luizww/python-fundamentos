maior=0
menor=0
for p in range( 1 , 6):
    peso=(float(input('Digite seu peso!: ')))
    if p==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print('o maior peso foi {} e o menor foi {}'.format(maior , menor))