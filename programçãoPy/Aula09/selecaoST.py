import streamlit as st 

#Problema lanchonete 
st.title("Lanchonete do Clodoaldo")
st.header("Meno de opções do Restaurante")
st.subheader("Opções de Lanches")
st.markdown(
    """
    |Código|Descrição do item | Preço  |
    |------|------------------|--------|
    | 1001 | X-Burguer        |R$ 8,00 |
    | 1002 | X-Salada         |R$ 10,00|
    | 1003 | X-Campeâo        |R$ 12,00|
    | 1004 | X-ESP32          |R$ 15,00|
    | 1005 | X-C37            |R$ 18,00|
    """
)
#Entrada de dados
opcao = st.selectbox("Selecione o código do lanche desejado:",
                     options=["1001", "1002", "1003", "1004", "1005"])
codigo = int(opcao) #Converte a string selecionada em numero desejado
quantidade = st.number_input("Digite o quantidade desejada:", min_value=0, step=1)

#Estrutura de controle  de seleção
match codigo:
    case 1001:
        preco = 8.00
    case 1002:
        preco = 10.00
    case 1003:
        preco = 12.00
    case 1004:
        preco = 15.00
    case 1005:
        preco = 18.00
    case _:
        preco = 0.00 #Caso o codigo seja invalido

#Processamento de dados
total = preco * quantidade

#Saida de dados
st.write("Total a pagar: R$" + (str(total)))