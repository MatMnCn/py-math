import calculadora as c 
# Instanciação do objeto
circulo = c.calcula()
raio = float(input("Digite o valor do raio"))
# Entrada de Dados

raio = float(input("Digite o valor do raio"))

# Processamento de Dados
circunferencia = circulo.circunferencia(raio)
area = circulo.area(raio)
# Saida de Dados
print(f''' Circunferência: {circunferencia:.2f}
      Area: {area:.2f}
      PI: {circulo.PI}
      ''')
