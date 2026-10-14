numero = int(input("Digite um número inteiro não negativo: "))

if numero < 0:
    print("O fatorial não está definido para números negativos.")
else:
    fatorial = 1
    for fator in range(2, numero + 1):
        fatorial *= fator
    print(f"{numero}! = {fatorial}")
