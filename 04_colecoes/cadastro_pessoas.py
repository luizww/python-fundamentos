usuarios= []
while True:
    nome=input("Digite seu nome : ")
    idade=int(input("Digite sua idade : "))
    usuarios.append(nome)
    usuarios.append(idade)
    p=str(input("Deseja continuar? S/N" )).lower()
    if p == "n":
        break
    elif p == "s":
        continue
    else:
        print("Digite uma opção valida")
print(usuarios)
