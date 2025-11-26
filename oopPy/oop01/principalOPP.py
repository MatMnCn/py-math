import trianguloOOP as tl 

# Instanciando a classe
trianguloX = tl.triangulo()
trianguloY = tl.triangulo()

# Entrada de Dados
print("Digite as medidas do triangulo X:")
trianguloX.a = int(input("Digite a Medida A: "))
trianguloX.b = int(input("Digite a Medida B: "))
trianguloX.c = int(input("Digite a Medida C: "))
print("Digite as medidas do triangulo Y:")
trianguloY.a = int(input("Digite a Medida A: "))
trianguloY.b = int(input("Digite a Medida B: "))
trianguloY.c = int(input("Digite a Medida C: "))

#  Processamento de Dados
areaX = trianguloX.area()
areaY = trianguloY.area()

# Condicional para verificar qual triangulo é maior
if areaX > areaY:
    saida = "A área do triângulo X é maior que a área do triângulo Y"
elif areaX < areaY:
    saida = "A área do triângulo Y é maior que a área do triângulo X"
else:
    saida = "As áreas dos triângulos X e Y são iguais"

# Saída de Dados
print(f"A área do triângulo X é: {areaX:.1f}")
print(f"A área do triângulo Y é: {areaY:.1f}")
print(saida)