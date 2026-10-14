velocidade=int(input('A quantos km/h o carro estava? '))
subtração=(velocidade - 80)
multa=(subtração * 7)
if velocidade > 80:
    print('Você foi multado pois estava a {}Km/h e o limite era de 80Km/h,você foi multado em R${}'.format(velocidade , multa))
else:
    print('Velocidade normal')