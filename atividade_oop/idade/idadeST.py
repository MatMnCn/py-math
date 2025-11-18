import streamlit as st 
import idadeOOP as p 

nome1 = st.text_input()
idade1 = st.number_input()

nome2 = st.text_input()
idade2 = st.number_input()

if st.button:
    pessoas1 = p.Produto(nome1, idade1)
    pessoas2 = p.Produto(nome2, idade2)