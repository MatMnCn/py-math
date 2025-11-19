import streamlit as st
from idadeOOP import Pessoa

st.title("Comparação de Idades👴👶🧒")

nome1 = st.text_input("Nome da primeira pessoa:")
idade1 = st.number_input("Idade da primeira pessoa:", step=1, format="%d")

nome2 = st.text_input("Nome da segunda pessoa:")
idade2 = st.number_input("Idade da segunda pessoa:", step=1, format="%d")

# Botão 
if st.button("Comparar"):
    p1 = Pessoa(nome1, idade1)
    p2 = Pessoa(nome2, idade2)

    resultado = p1.saida(p2)

    st.success(resultado)
