numero = int(input("Digite um número inteiro: "))

if numero < 2:
    print("O número não é primo.")
else:
    divisores = 0
    for candidato in range(1, numero + 1):
        if numero % candidato == 0:
            divisores += 1

    print("O número é primo." if divisores == 2 else "O número não é primo.")
