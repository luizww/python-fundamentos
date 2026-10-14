soma=0
impares=0
for c in range(1 , 7):
        numeros=int((input('Digite o {} numero inteiro : '.format(c))))
        if numeros % 2 == 0:
            soma=soma+numeros
        elif numeros % 2 == 1:
              impares=impares+numeros
print('A soma dos numeros pares é igual a {} e a soma dos impares é igual a {}'.format(soma , impares))