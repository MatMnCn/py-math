PI = 3.14
# Entrada de Dados
raio = float(input("Digite o valor do raio: "))
# Processamento de Dados
circunferencia = 2 * PI * (raio**2)
area = PI * raio ** 2
# Saida de Dados
print(f''' Circunferencia: {circunferencia:.2f}
      Area: {area:.2f}
      PI:{PI}
      ''')
