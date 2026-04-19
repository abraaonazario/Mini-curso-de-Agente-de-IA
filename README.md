#  Agente de IA 2026

Um projeto de demonstração de agentes de IA conversacionais em Python, apresentando uma arquitetura monolítica simples.

## 📋 Descrição

Este projeto implementa um agente de IA simples que responde a perguntas sobre carreira em Engenharia de IA, vagas de emprego e tecnologias relacionadas. O agente utiliza expressões regulares para identificar padrões nas mensagens do usuário e fornecer respostas apropriadas.

## 🏗️ Arquitetura

O projeto apresenta uma abordagem monolítica:

### Arquitetura Monolítica
- **Arquivo**: `logica_agenteV1.py`
- **Descrição**: Aplicação Streamlit completa com a lógica do agente integrada
- **Vantagens**: Simples de executar, tudo em um arquivo

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

## 🔧 Funcionalidades do Agente

O agente reconhece e responde a:
- **Saudações**: "oi", "olá", "bom dia"
- **Carreira**: "carreira", "estudar", "aprender"
- **Vagas**: "vagas", "emprego", "trabalho"
- **Tecnologia**: "python", "fastapi", "ai", "ia"

## 🛠️ Desenvolvimento

### Classe AgenteLogico
- Localizada em `logica_agenteV1.py`
- Utiliza regex para pattern matching
- Estrutura orientada a objetos
- Fácil de estender com novas regras

## 📝 Notas de Desenvolvimento

- Desenvolvido em Python 3.x
- Interface baseada em Streamlit para prototipagem rápida
- Lógica baseada em regras simples (regex)
- Estado de conversa mantido em sessão Streamlit

## 🤝 Contribuição

Este é um projeto educacional para demonstrar conceitos de:
- Arquitetura de software
- Agentes de IA conversacionais
- Interfaces web com Streamlit

---

Desenvolvido por Abraão Mini Curso 2026</content>
<parameter name="filePath">c:\Cursos python\Mini Curso18-04-2026\README.md
