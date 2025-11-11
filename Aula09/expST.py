import streamlit as st 

#Função Porcentagem
def porcentagem(cobaia):
    return (cobaia / total_cobaias) * 100
def qtd(total):
    total += quantidade
    return total
 
#Problema experiencias com cobaias
st.title("Laboratorio de cobaias")

#Declaração de variael
total_cobaias = 0
total_ratos = 0
total_sapos = 0
total_coelhos = 0

#Entrada de dados
n = st.number_input("Digite o numero de experimentos:", min_value=0, step=1)

#Estrutura de controle -PARA -- loop determinado em py
for i in range(n):
    quantidade = st.number_input(f"Experimento {i+1} - quantidades de cobaias utilizadas:",
                                 min_value=1, step=1)
    tipo = st.selectbox(f"Experimento {i+1} - Tipo de cobaia(C:Coelho, R:Rato, S:Sapo):", options=['C', 'R', 'S'])
    
    #Processamento de Dados
    #total_cobaias += quantidade
    total_cob = qtd(total_cobaias)
    if tipo == "C":
        #total_coelhos += quantidade
        total_coelhos = qtd(total_coelhos)
    elif tipo == "R":
        #total_ratos += quantidade
        total_ratos = qtd(total_ratos)
    elif tipo == "S":
        #total_sapos += quantidade 
        total_sapos = qtd(total_sapos)


if total_cobaias>0:
    percentual_coelhos = porcentagem(total_coelhos)
    percentual_ratos = porcentagem(total_ratos)
    percentual_sapos = porcentagem(total_sapos)
else:
    percentual_coelhos = percentual_ratos = percentual_sapos = 0

#saida de dados
st.subheader("Resultados")
st.write("Total de cobaias utilizadas:", total_cobaias)
st.write("Total de coelhos utilizados:", total_coelhos)
st.write("Total de ratos utilizados:", total_ratos )
st.write("Total de sapos utilizados:", total_sapos)

#Percentual 
st.write(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
st.write(f"Percentual de ratos: {percentual_ratos:.2f} %")
st.write(f"Percentual de sapos: {percentual_sapos:.2f} %")