numeros=[]
while True:
    add=int(input('Digite um numero para adicionar a lista!'))
    if add not in numeros:
        numeros.append(add)
    else:
        print('Voce digitou um numro repetido,ele não sera adicionado!')
    escolha=str(input('Deseja continuar?[s/n]')).lower() 
    if escolha == 's':
        continue
    elif escolha == 'n':
        break
    else:
        print('Opção invalida!')
        continue
numeros.sort()
print(f'Aqui estão os numeros digitados em ordem crescente!{numeros}')
