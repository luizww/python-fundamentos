numeros=('Zero',' Um','Dois', 'Tres' ,'Quatro', 'Cinco' ,'Seis', 'Sete', 'Oito' ,'Nove' ,'Dez' ,'Onze' ,'Doze', 'Treze', 'Quatorze' ,'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito' ,'Dezenove', 'Vinte')
while True:
    escolha=int(input('Digite um numero entre 0 e 20: '))
    if 0 <= escolha <= 20:
        print(f'Você digitou o número {numeros[escolha]}.')
        break
    else:
        print('Digite um número válido!')
