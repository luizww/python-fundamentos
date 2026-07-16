peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

if peso <= 0 or altura <= 0:
    print("Peso e altura precisam ser maiores que zero.")
else:
    imc = peso / altura**2
    if imc < 18.5:
        classificacao = "abaixo do peso"
    elif imc < 25:
        classificacao = "peso adequado"
    elif imc < 30:
        classificacao = "sobrepeso"
    elif imc < 40:
        classificacao = "obesidade"
    else:
        classificacao = "obesidade grave"

    print(f"IMC: {imc:.2f} — {classificacao}.")
