numeros = []

for posicao in range(5):
    numeros.append(int(input(f"Digite um valor para a posição {posicao}: ")))

ordenados = sorted(numeros)
maior = max(numeros)
menor = min(numeros)

print("Valores em ordem crescente:", ordenados)
print(f"Maior valor: {maior} — posição original: {numeros.index(maior)}")
print(f"Menor valor: {menor} — posição original: {numeros.index(menor)}")
