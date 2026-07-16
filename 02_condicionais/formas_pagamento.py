preco = float(input("Qual o valor do produto? R$ "))
forma = int(
    input(
        "Como deseja pagar?\n"
        "[1] Cartão\n"
        "[2] Dinheiro, Pix ou cheque\n"
        "Escolha: "
    )
)

if forma == 2:
    total = preco * 0.90
    print(f"Total com 10% de desconto: R$ {total:.2f}")
elif forma == 1:
    parcelas = int(input("Em quantas parcelas? "))
    if parcelas == 1:
        total = preco * 0.95
        print(f"Total com 5% de desconto: R$ {total:.2f}")
    elif parcelas == 2:
        print(f"2 parcelas de R$ {preco / 2:.2f}. Total: R$ {preco:.2f}")
    elif 3 <= parcelas <= 12:
        total = preco * 1.20
        print(
            f"{parcelas} parcelas de R$ {total / parcelas:.2f}. "
            f"Total com juros: R$ {total:.2f}"
        )
    else:
        print("Número de parcelas inválido.")
else:
    print("Forma de pagamento inválida.")
