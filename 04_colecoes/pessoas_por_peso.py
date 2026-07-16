pessoa=list()
dados=list()
maior = menor = 0
while True:
    pessoa.append(str(input('Qual seu nome?: ')))
    pessoa.append(float(input('Qual seu peso?: ')))
    if len(dados) == 0:
        maior=menor=pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    dados.append(pessoa[:])
    pessoa.clear()
    p3=str(input('Deseja continuar?')).lower()
    if p3 == 'n':
        break
print(f'Ao todo voce cadastrou {len(dados)} pessoas')
print(f'O maior peso foi de {maior}Kg pertencente a :')
for p in dados:
    if p[1] == maior:
        print(p[0])
print(f'O menor peso foi de {menor}Kg pertencente a:')
for m in dados:
    if m[1] == menor:
        print(m[0])