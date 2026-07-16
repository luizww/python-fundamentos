distancia=int(input('Qual a distancia da sua viagem em km?'))
perto=(distancia*0.5)
longe=(distancia*0.45)
if distancia <= 200:
    print('O valor da sua passagem é {}'.format(perto))
else:
    print('O valor da sua passagem é {}'.format(longe))