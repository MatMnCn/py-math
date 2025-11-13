#Framework
from streamlit import header, write, text_input, button, number_input, error, success, balloons
from math import sqrt, pow
header("Calculadora de Bhaskara")
write("Calculadora de raízes \n de uma equção de segundo grau")
write("ax² = bx + c = 0")

# Entrada de dados
a = number_input("Insira o valor de a:", value=1.0)
b = number_input("Insira o valor de b:", value=0.0)
c = number_input("Insira o valor de c:", value=0.0)

# Processamento de Dados
if button("Calcular raízes"):
    try:

        a = float(a)
        b = float(b)
        c = float(c)

        Delta = b**2 - 4*a*c

        if Delta < 0:
            error("A equação não possui raízes reais.")

        elif Delta == 0:
            raiz = (-b + sqrt(Delta)) / (2*a)
            success(f"A equação possui uma raiz real: {raiz}")

        else:
            raiz1 = (-b + sqrt(Delta)) / (2*a)
            raiz2 = (-b - sqrt(Delta)) / (2*a)
            balloons()
            success(f"A equação possui duas raízes reais: \n Raiz 1: {raiz1} \n Raiz 2: {raiz2}")

    except ValueError:
        error("Por favor, insira valores numéricos válidos para a, b e c.")
        
    except ZeroDivisionError:
        error("O valor de 'a' não pode ser zero em uma equação de segundo grau.")