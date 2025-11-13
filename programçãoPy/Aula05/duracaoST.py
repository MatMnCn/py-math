import streamlit as st #Framework

# Problema duração de Tempo
TITULO = "Calculadora de Duração de Tempo"
st.set_page_config(page_title=TITULO)
st.title(TITULO)

# Entrada de dados
tempo = st.number_input("Insira o tempo em segundos:", min_value=0, step=1, help= "Insira a duração total em segundos para converter em horas,minutos e segundos.")

# Processamento de dados
horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60

# Saída de dados
st.write(f"{horas} horas, {minutos} minutos e {segundos} segundos.")

