# banco.py

# deposito = adicionr valores positivos, 1 unico usuario, criar variavel

#saque = 3 saques diarioos c limite de R$500/saque

#extrato = mostrar todos os depositos/saque/saldo e formato monetario

Saldo = 0
Valor = 0
Historico = []
def Deposito(Valor_Deposito):
    global Saldo
    Saldo += Valor_Deposito
    Historico.append(("Deposito", Valor_Deposito))
def Saque(Valor_Sacado):
    global Saldo
    Saldo = Saldo - Valor_Sacado
    Historico.append(("Saque", Valor_Sacado))
Limite_Saques = 0
def menu():
    return input("Selecione um de nossos serviços : \n"
          "[1] Deposito \n"
          "[2] Saque \n"
          "[3] Extrato \n"
          "[4] Sair \n")
print("Seja bem vindo ao banco")

while True:
    opcao = menu()
    if opcao == "1":
        Valor = float(input("Qual sera o valor do deposito? \n"
                            "R$: "))
        if Valor <= 0:
            print("O valor deposito deve ser maior que 0.")
            continue
        Deposito(Valor)
        print("Deposito realizado com sucesso! \n"
              "O saldo total da conta é R${:.2f} \n".format(Saldo))
    if opcao == "2":
        Valor = float(input("Qual será o valor para saque? \n"
                            "R$: "))
        if Valor > Saldo:
            print("Não há saldo suficiente, por favor, tente novamente.")
            continue
        if Limite_Saques >= 3:
            print("O limite de saques foi esgotado hoje, tente novamente amanhã.")
            continue
        if Valor > 500:
            print("O valor maximo para saque é de R$500,00. Por favor tente novamente.")
            continue
        if Valor <= 0:
            print("O valor do saque deve ser maior que zero.")
            continue
        else:
            Saque(Valor)
            Limite_Saques += 1
            print("Saque bem sucedido! \n"
                  "O saldo total da conta é R${:.2f} \n".format(Saldo))     
    if opcao == "3":
        if not Historico:
            print("Nenhuma movimentação realizada")
        for Operação, Valor_Operação in Historico:
            print("{} : R${:.2f} ".format(Operação , Valor_Operação))
        print("Saldo atual: R${:.2f}\n".format(Saldo))
    if opcao == "4":
        break