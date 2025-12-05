import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide", page_title="Mapa Eleitoral SG")

st.title("Comparativo Eleitoral - São Gonçalo")

# Seletores
turno = st.selectbox("Selecione o Turno", [1, 2])

# Função auxiliar para carregar HTML


def exibir_html(caminho, altura=500):
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as f:
            html_data = f.read()
        # Exibe o HTML
        components.html(html_data, height=altura, scrolling=False)
    else:
        st.warning(f"Mapa não encontrado: {caminho}")


# Layout
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("2002")
    arquivo = f"eleicao_2002_t{turno}.html"
    exibir_html(arquivo)

with col2:
    st.subheader("2018")
    arquivo = f"eleicao_2018_t{turno}.html"
    exibir_html(arquivo)

with col3:
    st.subheader("Zonas Eleitorais")
    exibir_html("zonas_fixas.html")

