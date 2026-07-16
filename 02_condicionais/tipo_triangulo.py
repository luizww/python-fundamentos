lado_a = float(input("Digite o primeiro lado: "))
lado_b = float(input("Digite o segundo lado: "))
lado_c = float(input("Digite o terceiro lado: "))

forma_triangulo = (
    lado_a + lado_b > lado_c
    and lado_a + lado_c > lado_b
    and lado_b + lado_c > lado_a
)

if not forma_triangulo:
    print("Os valores informados não formam um triângulo.")
elif lado_a == lado_b == lado_c:
    print("Triângulo equilátero.")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("Triângulo isósceles.")
else:
    print("Triângulo escaleno.")
