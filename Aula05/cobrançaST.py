import streamlit as st #Framework

# Problema Cobrança 
TITULO = "Caixa de Cobrança"
st.markdown (f"<h1 style='text-align: center;'> {TITULO}</h1>", unsafe_allow_html=True)

# Entrada de dados
preço_unitario_do_produto = st.number_input("Preço unitário do produto:", min_value=0.0, step= 2.0)
quantida_de_comprada = st.number_input("Quantidade comprada:", min_value=0, step=1)
dinheiro_recebido = st.number_input("Dinheiro recebido:", min_value=0.0, step= 2.0)

# Processamento de dados
troco = dinheiro_recebido - (preço_unitario_do_produto * quantida_de_comprada)

# Saída de dados
st.write(f"Seu troco é: R$ {troco:.2f}")
