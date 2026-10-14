import random
numero=[ 0, 1 , 2 , 3 , 4 , 5]
sorteio=(random.choice(numero))
chute=int(input('Advinhe o numero entre 0 e 5 que o computador gerou '))
if chute==sorteio:
    print('Parábens,você acertou,o numero sorteado foi {}'.format(sorteio))
else:
    print('Que pena!O numero era {}'.format(sorteio))