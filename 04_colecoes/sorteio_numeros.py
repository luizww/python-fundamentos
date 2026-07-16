import random


numeros = tuple(random.sample(range(1, 11), 5))

print("Números sorteados:", numeros)
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
