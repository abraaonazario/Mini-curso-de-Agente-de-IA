import streamlit as st
import re
from datetime import datetime

# --- 1. CONFIGURAÇÃO INICIAL (Sempre no topo) ---
st.set_page_config(page_title="Agente de IA 2026", page_icon="🤖")

# --- 2. INICIALIZAÇÃO DO ESTADO (A solução do erro!) ---
# Aqui garantimos que a gaveta 'messages' exista antes de qualquer outra coisa
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 3. CLASSE DO AGENTE ---
class AgenteLogico:
    def __init__(self, nome: str):
        self.nome = nome
        self.regras = {
            "saudacao": r"\b(oi|olá|ola|bom dia|boa tarde)\b",
            "carreira": r"\b(carreira|estudar|aprender|estudos)\b",
            "vagas": r"\b(vagas|emprego|trabalho|oportunidade)\b",
            "tecnologia": r"\b(python|fastapi|groq|ai|ia)\b"
        }

    def processar_entrada(self, mensagem: str) -> str:
        msg = mensagem.lower()
        if re.search(self.regras["saudacao"], msg):
            return "Olá! Sou seu consultor de Engenharia de IA. Como posso ajudar?"
        elif re.search(self.regras["carreira"], msg):
            return "A trilha ideal em 2026 começa com Lógica e termina em Orquestração de Agentes."
        elif re.search(self.regras["vagas"], msg):
            return "O mercado de IA está focado em quem sabe integrar LLMs em sistemas reais."
        elif re.search(self.regras["tecnologia"], msg):
            return "Python e FastAPI são as ferramentas que estamos usando!"
        return "Ainda não tenho uma regra para isso. Vamos falar sobre 'vagas' ou 'carreira'?"

# --- 4. INTERFACE E EXECUÇÃO ---
st.title("🤖 Agente Conversacional v1.0")
st.caption("Desenvolvido por Abraão & Loren")

agente = AgenteLogico("Agente-v1-Base")

# Exibe o histórico (Agora ele encontra a chave 'messages' com certeza)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Loop de Interação
if prompt := st.chat_input("Escreva aqui..."):
    # 1. Guarda e mostra msg do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Processa e guarda resposta do agente
    resposta = agente.processar_entrada(prompt)
    st.session_state.messages.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.markdown(resposta)