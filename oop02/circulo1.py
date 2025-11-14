from calculadora import calculadora1

# Entrada de Dados

raio = float(input("Digite o valor do raio"))

# Processamento de Dados
circunferencia = calculadora1.circunferencia(raio)
area = calculadora1.area(raio)
# Saida de Dados
print(f''' Circunferência: {circunferencia:.2f}
      Area: {area:.2f}
      PI: {calculadora1.PI}
      ''')
