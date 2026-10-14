numero_1 = int(input("Digite o primeiro número inteiro: "))
numero_2 = int(input("Digite o segundo número inteiro: "))

if numero_1 > numero_2:
    print(f"{numero_1} é maior que {numero_2}.")
elif numero_2 > numero_1:
    print(f"{numero_2} é maior que {numero_1}.")
else:
    print("Os dois números são iguais.")
