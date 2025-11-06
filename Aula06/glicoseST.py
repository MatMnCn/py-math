#Framework
import streamlit as st

# Titulo
TITULO = "Classificação de Níveis de Glicose no Sangue" 
st.set_page_config("Classifcação de Níveis")
st.title(TITULO)

st.markdown("""
    | Nível de glicose | Classificação |
    |------------------|---------------|
    | 0 - 70           | Hipoglicemia  |
    | 71 - 100         | Normal        |
    | 101 - 140        | Pré-diabetes  |
    | 141 ou mais      | Diabetes      |
"""
)

# Entrada de dados
nivel_glicose = st.number_input("Insira o nível de glicose no sangue (mg/dL):", min_value=0)
if st.button("Classificar"):
    if nivel_glicose <= 70:
        st.write("Nivel de glicose foi classificado como: Hipoglicemia")
        st.error("Cuidado! Níveis de glicose muito baixos, procure suporte médico.")
    elif nivel_glicose <= 100:
        st.write("Nivel de glicose foi classificado como: Normal")
        st.balloons()
        st.success("Parabéns! Você está com níveis de glicose saudáveis.")
    elif nivel_glicose <= 140:
        st.write("Nivel de glicose foi classificado como: Pré-diabetico")
        st.error("Fique em alerta com sua glicose.")
    else:
        st.write("Nivel de glicose foi classificado como: Diabetico")
        st.error("Cuidado! Níveis de glicose muito altos, procure suporte médico.")
