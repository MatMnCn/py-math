# Problema Triangulo sem oop

# Entrada de Dados

# TRIANGULO X
print("Inserir as medidas do triângulo X:")

ax = int(input("Digite a medida A:"))
bx = int(input("Digite a medida B:"))
cx = int(input("Digite a medida C:"))

# TRIANGULO Y
print("Inserir as medidas do triângulo Y:")
ay = int(input("Digite a medida A:"))
by = int(input("Digite a medida B:"))
cy = int(input("Digite a medida C:"))

# Processamento de Dados
p = (ax + bx + cx) / 2
areax = (p * (p - ax) * (p - bx) * (p - cx)) ** 0.5
p = (ay + by + cy) / 2
areay = (p * (p - ay) * (p - by) * (p - cy)) ** 0.5

# Condicional para verificar qual triangulo é maior
if areax > areay:
    saida = "A área do triângulo X é maior que a área do triângulo Y"
elif areax < areay:
    saida = "A área do triângulo Y é maior que a área do triângulo X"
else:
    saida = "As áreas dos triângulos X e Y são iguais"

# Saída de Dados
print(f"A área do triângulo X é: {areax:.1f}")
print(f"A área do triângulo Y é: {areay:.1f}")

print(saida)