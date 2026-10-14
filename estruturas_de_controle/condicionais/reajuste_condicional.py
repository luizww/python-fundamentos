salario = float(input("Qual o valor do seu salário? R$ "))
percentual = 10 if salario > 1250 else 15
novo_salario = salario * (1 + percentual / 100)

print(f"Reajuste aplicado: {percentual}%")
print(f"Novo salário: R$ {novo_salario:.2f}")
