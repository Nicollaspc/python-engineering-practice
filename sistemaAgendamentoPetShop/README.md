# 🐾 Sistema de Agendamento - Pet Shop

Este é um sistema de gerenciamento de agendamentos desenvolvido em **Python**, focado nos princípios de **Rapid Application Development (RAD)**. O projeto demonstra a manipulação de arquivos de texto de forma segura, lógica de negócios para evitar conflitos de horários e tratamento de exceções.

## 🚀 Funcionalidades

- **Visualização da Agenda**: Leitura em tempo real do arquivo de dados com formatação de data brasileira.
- **Novo Agendamento**: Sistema de escrita em modo *append* com validação de horário (impede agendamentos duplicados no mesmo horário).
- **Cancelamento Inteligente**: Remoção de registros específicos através de filtragem de strings.
- **Limpeza Total**: Função rápida para resetar a agenda do dia.
- **Interface de Terminal Colorida**: Menu interativo com feedback visual (ANSI colors) para melhor experiência do usuário.

## 🛠️ Tecnologias e Conceitos Aplicados

- **Linguagem**: Python 3.10+
- **Bibliotecas Nativas**: `os`, `datetime`.
- **Persistência de Dados**: Manipulação de arquivos `.txt` (modos `r`, `w`, `a`).
- **Tratamento de Erros**: Blocos `try/except` para garantir que o sistema não "crashe" com entradas inválidas ou arquivos ausentes.
- **Lógica de Programação**: Uso de `match/case`, manipulação de listas e fatiamento de strings (`split`).

## 📋 Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório ou copie o código fonte.
3. Execute o arquivo principal:
   ```bash
   python nome_do_seu_arquivo.py