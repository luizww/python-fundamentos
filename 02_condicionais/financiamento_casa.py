vc=float(input('Qual o valor da casa?'))
salario=(int(input('Qual o seu salario?')))
vp=float(input('Qual valor voce deseja pagar nas parcelas?'))
tempo=vc//vp
anos=tempo//12
meses=tempo % 12
if vp <= 30 * salario / 100:
    print('Seu emprestimo foi aprovado!Voce pagara {} durante {} anos e {} meses'.format(vp , anos , meses))
else:
    print('Infelizmente seu emprestimo foi recusado')