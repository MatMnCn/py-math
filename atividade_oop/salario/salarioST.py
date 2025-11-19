import streamlit as st
from salarioOOP import Funcionario, CalculadoraSalario

st.title("Salário Médio dos Funcionários💸")

st.subheader("Informe os dados:")

nome1 = st.text_input("Nome do 1º funcionário:")
sal1 = st.number_input("Salário do 1º funcionário:", min_value=0.0, step=0.01, format="%.2f")

nome2 = st.text_input("Nome do 2º funcionário:")
sal2 = st.number_input("Salário do 2º funcionário:", min_value=0.0, step=0.01, format="%.2f")

# Botão normal (sem form)
enviar = st.button("Calcular Média")

if enviar:
    f1 = Funcionario(nome1, sal1)
    f2 = Funcionario(nome2, sal2)

    calc = CalculadoraSalario()
    media = calc.media(f1, f2)

    st.success(f"O salário médio entre {nome1} e {nome2} é: R$ {media:.2f}")
