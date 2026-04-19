# 🤖 Agente de IA 2026

Um projeto de demonstração de agentes de IA conversacionais em Python, apresentando uma arquitetura monolítica simples.

## 📋 Descrição

Este projeto implementa um agente de IA simples que responde a perguntas sobre carreira em Engenharia de IA, vagas de emprego e tecnologias relacionadas. O agente utiliza expressões regulares para identificar padrões nas mensagens do usuário e fornecer respostas apropriadas.

## 🏗️ Arquitetura

O projeto apresenta uma abordagem monolítica:

### Arquitetura Monolítica
- **Arquivo**: `logica_agenteV1.py`
- **Descrição**: Aplicação Streamlit completa com a lógica do agente integrada
- **Vantagens**: Simples de executar, tudo em um arquivo

*Nota: Arquiteturas full-stack mencionadas anteriormente não estão implementadas no workspace atual.*

## 📦 Dependências

```
streamlit
```

## 🚀 Instalação e Execução

1. Clone ou baixe o projeto
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instale as dependências:
   ```bash
   pip install streamlit
   ```
5. Execute o agente:
   ```bash
   streamlit run logica_agenteV1.py
   ```

## 📝 Uso

- Abra o chat e digite perguntas sobre carreira, vagas ou tecnologias de IA.
- O agente responde com base em regras pré-definidas usando regex.

## ▶️ Como Executar

### Arquitetura Monolítica
```bash
streamlit run logica_agenteV1.py
```

### Arquitetura Full-Stack

1. **Backend (Terminal 1)**:
   ```bash
   cd "Full-Stack Agent"
   uvicorn api_agente:app --reload --host 127.0.0.1 --port 8000
   ```

2. **Frontend (Terminal 2)**:
   ```bash
   cd "Full-Stack Agent"
   streamlit run interface_streamlit.py
   ```

### Interface Simples
```bash
streamlit run main.py
```
*Nota: Requer o backend rodando na porta 8000*

## 📁 Estrutura dos Arquivos

```
├── logica_agente.py          # Classe base do agente lógico
├── logica_agenteV1.py        # App monolítico Streamlit
├── main.py                   # Interface simples (conecta ao backend)
└── Full-Stack Agent/
    ├── api_agente.py         # Backend FastAPI
    └── interface_streamlit.py # Frontend Streamlit com histórico
```

## 🔧 Funcionalidades do Agente

O agente reconhece e responde a:
- **Saudações**: "oi", "olá", "bom dia"
- **Carreira**: "carreira", "estudar", "aprender"
- **Vagas**: "vagas", "emprego", "trabalho"
- **Tecnologia**: "python", "fastapi", "ai", "ia"

## 🛠️ Desenvolvimento

### Classe AgenteLogico
- Localizada em `logica_agente.py`
- Utiliza regex para pattern matching
- Estrutura orientada a objetos
- Fácil de estender com novas regras

### API FastAPI
- Endpoint: `POST /chat`
- Payload: `{"texto": "mensagem do usuário"}`
- Resposta: `{"resposta": "resposta do agente"}`

## 📝 Notas de Desenvolvimento

- Desenvolvido em Python 3.x
- Interface baseada em Streamlit para prototipagem rápida
- Backend FastAPI para APIs REST
- Lógica baseada em regras simples (regex)
- Estado de conversa mantido em sessão Streamlit

## 🤝 Contribuição

Este é um projeto educacional para demonstrar conceitos de:
- Arquitetura de software
- Desenvolvimento full-stack
- Agentes de IA conversacionais
- APIs REST com FastAPI
- Interfaces web com Streamlit

---

Desenvolvido por Abraão & Loren - Mini Curso 2026</content>
<parameter name="filePath">c:\Cursos python\Mini Curso18-04-2026\README.md
