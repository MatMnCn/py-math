import streamlit as st #framework

# Problema senha fixa

st.title("Sistema de Login Simples")

#Declaração de constantes
#Credenciais fixas

USUARIO= "Clodoaldo"
SENHA= "senha123"

#Entrada de Dados
usuario_entrada = st.text_input("Nome do usuario")
senha_entrada = st.text_input("Senha", type="password")

# Estrutura de Controle em looping

botao = st.button("Logar")

#Tentativas
MAX_TENTATIVAS = 3

if "tentativas" not in st.session_state:
    st.session_state.tentativas = 0

if botao is True:
    if st.session_state.tentativas >= MAX_TENTATIVAS:
        st.error("Máximo de Tentativas Atingido, acesso bloqueado...")
    else:
        # Usar o while para controlar as tentativas
        while st.session_state.tentativas < MAX_TENTATIVAS:
            if usuario_entrada == USUARIO and senha_entrada == SENHA:
                st.success("Login Sucedido!")
                st.session_state.tentativas = 0
                break
            else:
                st.session_state.tentativas += 1
                st.error(f"Credenciais Invalidas. Tentativa {st.session_state.tentativas} de {MAX_TENTATIVAS}")
                break