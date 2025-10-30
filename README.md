# 🧠🎤 Pycraft – Integração de Voz com Servidor Minecraft Java

Este projeto demonstra como integrar **reconhecimento de voz em Python** com um **servidor Minecraft Java**, permitindo executar ações dentro do jogo usando comandos falados.

Ao falar um comando, o Python interpreta a voz, converte em texto e executa ações no servidor Minecraft.

---

## 🚀 Funcionalidades

- Comandos de voz em **pt-BR**
- Execução de ações dentro do Minecraft
- Teleporte automático com palavras-chave
- Geração de TNT via comando falado
- Exemplo com integração MCPI

---

## 🧩 Como Funciona

1. O programa escuta sua voz pelo microfone.
2. O áudio é convertido para texto usando a API do Google Speech Recognition.
3. Se a palavra reconhecida corresponder a uma da lista configurada, o Minecraft responde com uma ação.
4. Caso contrário, o texto é exibido no chat do jogo.

---

## 📦 Requisitos

### ✅ Python
- Python 3.8+
- Bibliotecas:
  ```bash
  pip install SpeechRecognition mcpi
