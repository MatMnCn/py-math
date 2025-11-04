# Problema terreno
# Declatação de variáveis
largura:float
comprimento:float
# Entrada de dados
Largura = float(input("Digite a largura do terreno: "))
Comprimento = float(input("Digite o comprimento do terreno: "))
valo_r_metro_quadrado = float(input("Digite o valor do metro quadrado: "))
# Processamento de dados
area = Largura * Comprimento
preco = area * valo_r_metro_quadrado
# Saida de dados
print(f"A area do terreno é de: {area}")
print(f"O preço do terreno é de: {preco}")

