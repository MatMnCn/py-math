#Framework
import streamlit as st

import math as mt

st.header("Calculadora de Bhaskara")
st.write("Calculadora de raízes \n de uma equção de segundo grau")
st.write("ax² = bx + c = 0")

# Entrada de dados
a = st.number_input("Insira o valor de a:", value=1.0)
b = st.number_input("Insira o valor de b:", value=0.0)
c = st.number_input("Insira o valor de c:", value=0.0)

# Processamento de Dados
if st.button("Calcular raízes"):
    try:

        a = float(a)
        b = float(b)
        c = float(c)

        Delta = b**2 - 4*a*c

        if Delta < 0:
            st.error("A equação não possui raízes reais.")

        elif Delta == 0:
            raiz = (-b + mt.sqrt(Delta)) / (2*a)
            st.success(f"A equação possui uma raiz real: {raiz:.2f}")

        else:
            raiz1 = (-b + mt.sqrt(Delta)) / (2*a)
            raiz2 = (-b - mt.sqrt(Delta)) / (2*a)
            st.balloons()
            st.success(f"A equação possui duas raízes reais: \n Raiz 1 {raiz1} \n Raiz 2: {raiz2}")

    except:
        st.error("Por favor, insira valores numéricos válidos para a, b e c.")