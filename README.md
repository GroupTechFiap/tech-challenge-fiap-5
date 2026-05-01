# 🎓 Previsão de Risco Educacional - Passos Mágicos

Aplicação de Machine Learning desenvolvida para identificar alunos com risco de defasagem educacional, apoiando decisões estratégicas da ONG Passos Mágicos.

---

## 📌 Sobre o Projeto

A Associação Passos Mágicos atua há mais de 35 anos na transformação da vida de crianças e jovens em situação de vulnerabilidade social no município de Embu-Guaçu.

Este projeto utiliza dados educacionais (2022–2024) para:

- 📊 Avaliar a evolução dos alunos ao longo das fases (Quartzo, Ágata, Ametista e Topázio)
- 🧠 Considerar fatores acadêmicos, comportamentais e psicossociais
- ⚠️ Identificar alunos em risco de defasagem
- 🎯 Apoiar intervenções pedagógicas preventivas

---

## 🚀 Tecnologias Utilizadas

- Python 3.11  
- Streamlit  
- Scikit-learn  
- Pandas  
- NumPy  
- Joblib  

---

## 🧠 Modelo de Machine Learning

O modelo foi treinado com base nos indicadores do índice INDE:

- Auto Avaliação (IAA)  
- Engajamento (IEG)  
- Psicossocial (IPS)  
- Psicopedagógico (IPP)  
- Ponto de Virada (IPV)  

### 🎯 Objetivo

Classificar alunos em:

- ✅ Baixo risco de defasagem  
- ⚠️ Alto risco de defasagem  

---

## 🖥️ Aplicação

A aplicação foi desenvolvida utilizando Streamlit, permitindo:

- Interface interativa e intuitiva  
- Inserção manual dos indicadores do aluno  
- Predição em tempo real  
- Visualização de probabilidade de risco  
---

## ⚙️ Como Executar Localmente

```bash
git clone https://github.com/GroupTechFiap/tech-challenge-fiap-5.git
cd tech-challenge-fiap-5
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Deploy

Aplicação publicada via Streamlit Cloud:

https://tech-challenge-fiap-5-p9ra3bvgmam5b57i8hlr6r.streamlit.app/

---

## 📊 Estrutura do Projeto

```
tech-challenge-fiap-5/
│
├── app.py
├── modelo_passos_magicos.pkl
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## 🤝 Contribuição

Projeto acadêmico desenvolvido para o Tech Challenge FIAP.
