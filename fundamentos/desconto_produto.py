preço=float(input('Qual o preço bruto do produto?'))
desconto=(preço * 5 / 100)
vf=(preço - desconto)
print('O novo preço do produto é {}'.format(vf))