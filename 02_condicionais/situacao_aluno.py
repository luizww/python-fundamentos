nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
media = (nota_1 + nota_2) / 2

if media < 5:
    situacao = "reprovado"
elif media < 7:
    situacao = "em recuperação"
else:
    situacao = "aprovado"

print(f"Média: {media:.1f} — aluno {situacao}.")
