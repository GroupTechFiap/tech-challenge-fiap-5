import streamlit as st
import pandas as pd
import joblib
import sklearn.compose._column_transformer as ct


if not hasattr(ct, "_RemainderColsList"):
    class _RemainderColsList(list):
        pass
    ct._RemainderColsList = _RemainderColsList


st.set_page_config(
    page_title="Previsão de Risco Educacional",
    page_icon="🎓",
    layout="centered"
)

# Carregar modelo
modelo = joblib.load("modelo_passos_magicos.pkl")

st.title("🎓 Sistema de Previsão de Risco Educacional")
st.markdown("### Associação Passos Mágicos")
st.markdown("---")

st.subheader("📊 Indicadores do Aluno")


iaa = st.slider("Auto Avaliação", 0.0, 10.0, 5.0)
ieg = st.slider("Engajamento", 0.0, 10.0, 5.0)
ips = st.slider("Psicossocial", 0.0, 10.0, 5.0)
ipp = st.slider("Psicopedagógico", 0.0, 10.0, 5.0)
ipv = st.slider("Ponto de Virada", 0.0, 10.0, 5.0)

st.markdown("---")

input_df = pd.DataFrame({
    "Auto Avaliação": [iaa],
    "Engajamento": [ieg],
    "Psicossocial": [ips],
    "Psicopedagógico": [ipp],
    "Ponto de Virada": [ipv]
})

if hasattr(modelo, "feature_names_in_"):
    input_df = input_df.reindex(columns=modelo.feature_names_in_)

if st.button("🔍 Prever Risco"):
    try:
        resultado = modelo.predict(input_df)
        prob = modelo.predict_proba(input_df)

        st.markdown("## 🎯 Resultado")

        if resultado[0] == 1:
            st.error("⚠️ Aluno com ALTO RISCO de defasagem")
        else:
            st.success("✅ Aluno com BAIXO RISCO")


    except Exception as e:
        st.error("Erro na previsão ⚠️")
        st.write(e)