p1=int(input('Digite o primeiro termo da progressão aritimetica :'))
r=int(input('Digite a razão da progressão aritimetica : '))
pa=p1 + 10* r
for ra in range( p1 , pa , r ):
    print(ra)