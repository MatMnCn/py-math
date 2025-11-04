import streamlit as st 
st.title("Problema Terreno")
# Entrada de Dados
st.write("Digite a Largura do terreno em metros:")
largura = st.number_input("Largura (m):")
st.write("Digite o Comprimento do terreno em metros:")
comprimento = st.number_input("Comprimento (m):")
st.write("Digite o valor do metro quadrado em reais:")
valor_m2=st.number_input("Valor do metro quadrado (R$):")
# Processamento de Dados
area = largura * comprimento
preco = area * valor_m2
# Saída de Dados
st.write(f"A área do terreno é de: {area} metros quadrados")

