import streamlit as st

# Titulo 
TITULO = "Análise de Dados Pessoais"
st.title(TITULO)
st.markdown("---")

# Declaração de variáveis

if 'dados_pessoas' not in st.session_state:
    st.session_state.dados_pessoas = []

# Entrada de Dados
n = st.number_input("Quantas pessoas serão digitadas?", min_value=0, step=1, key='num_pessoas')

st.subheader("Entrada de Dados")
dados_coletados = []

for i in range(n):
    st.markdown(f"**Dados da {i+1}ª pessoa:**")
    nome = st.text_input(
        f"Nome da {i+1}ª pessoa:", 
        key=f'nome_{i}'
    )
    idade = st.number_input(
        f"Idade da {i+1}ª pessoa:", 
        min_value=0, 
        step=1, 
        key=f'idade_{i}'
    )
    altura = st.number_input(
        f"Altura (em metros) da {i+1}ª pessoa:", 
        min_value=0.0, 
        format="%.2f", 
        key=f'altura_{i}'
    )
    # Armazenamento de dados 
    if nome and idade >= 0 and altura >= 0.0:
        dados_coletados.append({
            "nome": nome,
            "idade": idade,
            "altura": altura
        })
    st.markdown("---")


# Processamento de Dados
if st.button("Calcular Resultados", type="primary"):

    if not dados_coletados and n > 0:
        st.warning("Preencha todos os campos antes de calcular.")
    elif n == 0:
        st.info("Nenhum dado para processar, defina o número de pessoas.")
    elif len(dados_coletados) != n:
        st.warning(f"Faltam dados: Foram preenchidos {len(dados_coletados)} de {n} registros. Complete todos os campos.")
    else:
        soma_alturas = sum(p['altura'] for p in dados_coletados)
        altura_media = soma_alturas / n
        pessoas_menores_16 = [p for p in dados_coletados if p['idade'] < 16]
        if n > 0:
            porcentagem_menores = (len(pessoas_menores_16) / n) * 100
        else:
            porcentagem_menores = 0.0

# Saída de Dados
        st.header("Resultados da Análise")
        st.write(f"**Altura média:** {altura_media:.2f} m")
        st.write(f"**Pessoas com menos de 16 anos:** {len(pessoas_menores_16)} ({porcentagem_menores:.1f}%)")
        if pessoas_menores_16:
            st.subheader("Nomes das pessoas com menos de 16 anos:")
            nomes_str = "\n".join([f"- {p['nome']}" for p in pessoas_menores_16])
            st.markdown(nomes_str)
        else:
            st.info("Nenhuma pessoa registrada com menos de 16 anos.")