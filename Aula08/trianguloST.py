import streamlit as st

# Triângulo
def forma_triangulo(a, b, c):
    return (a < b + c) and (b < a + c) and (c < a + b)

def perimetro(a, b, c):
    return a + b + c

# Trapézio
def area_trapezio(a, b, c):
    return ((a + b) * c) / 2

# Título
st.title("Verificador de Triângulo △")
st.sidebar.title("Cálculo Geométrico")
st.sidebar.markdown("Verifica se três lados formam um triângulo e calcula perímetro ou área.")

# Entradas
A = st.number_input("Digite o valor de A:", format="%.2f", step=0.1)
B = st.number_input("Digite o valor de B:", format="%.2f", step=0.1)
C = st.number_input("Digite o valor de C:", format="%.2f", step=0.1)

# Saída
if st.button("Calcular", icon="📏"):
    if forma_triangulo(A, B, C):
        P = perimetro(A, B, C)
        st.success(f"Os valores formam um triângulo! ✅")
        st.write(f"Perímetro = {P:.1f}")
    else:
        area = area_trapezio(A, B, C)
        st.error("Os valores NÃO formam um triângulo ❌")
        st.write(f"Área do Trapézio ⏢: = {area:.1f}")