
while True:
    n1=int(input('digite um numero: '))
    n2=int(input('Digite outro numero: '))
    calculadora=int(input('Selecione uma operação :\n'
                '[1] SOMAR OS DOIS NUMEROS: \n' \
                '[2] SUBTRAIR OS DOIS NUMEROS \n' \
                '[3] MULTIPLICAR OS DOIS NUMEROS\n' \
                '[4] DIVIDIR OS DOIS NUMEROS\n' \
                '[5] COMPARAR OS DOIS NUMEROS\n' \
                '[6] SAIR DO PROGAMA '))
    if calculadora == 1:
        print('A soma entre {} e {} resulta em : {}'.format(n1 , n2 , (n1+n2)))
    elif calculadora == 2:
        print('A subtracão entre {} e {} resulta em : {}'.format(n1 , n2 , (n1 - n2)))
    elif calculadora == 3:
        print('A multiplicação entre {} e {} resulta em : {}'.format(n1 , n2 , n1*n2))
    elif calculadora == 4:
        if n2 == 0:
            print("Não é possível dividir por zero.")
        else:
            print("A divisão entre {} e {} resulta em: {}".format(n1, n2, n1 / n2))
    elif calculadora == 5:
        if n1 > n2:
            print('O primeiro numero {} é maior que o segundo {}.'.format(n1 , n2))
        elif n1 < n2:
            print('O primeiro numero {} é menor que o segundo {}.'.format(n1 , n2))
        else:
            print('Os dois numeros são iguais!')
    elif calculadora == 6:
        break
    else:
        print('Digite uma opção valida!')
