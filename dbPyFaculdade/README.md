# 🗄️ Python Database Practice (SQLAlchemy)

> Projeto inicial de estudo com banco de dados em Python utilizando SQLAlchemy (ORM).

---

## 📌 Sobre o projeto

Este projeto tem como objetivo aprender e praticar a integração de aplicações Python com banco de dados, utilizando o SQLAlchemy como ferramenta de mapeamento objeto-relacional (ORM).

A aplicação cria uma tabela de usuários, insere dados e realiza consultas simples.

---

## 🧠 Conceitos aplicados

* ORM (Object Relational Mapping)
* SQLAlchemy
* Criação de tabelas via código (modelagem)
* Sessões e transações
* Inserção e consulta de dados
* Uso de banco em memória (SQLite)

---

## ⚙️ Tecnologias utilizadas

* Python 3
* SQLite (em memória)
* SQLAlchemy

---

## 📂 Estrutura do projeto

```bash
database-practice/
│
├── main.py
└── README.md
```

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/database-practice.git
```

2. Acesse a pasta:

```bash
cd database-practice
```

3. Instale as dependências:

```bash
pip install sqlalchemy
```

4. Execute o projeto:

```bash
python main.py
```

---

## 💡 O que o código faz

* Cria uma conexão com banco SQLite em memória
* Define uma tabela `usuarios`
* Insere dois registros
* Consulta todos os usuários
* Exibe os dados no terminal

---

## 🧪 Exemplo de saída

```text
Usuario(id=1, nome=Nicollas, idade=19)
Usuario(id=2, nome=Leticia, idade=39)
```

---

## 🚀 Próximos passos

* Criar banco persistente (arquivo `.db`)
* Separar models em arquivos
* Implementar CRUD completo:

  * Create
  * Read
  * Update
  * Delete
* Adicionar validações
* Integrar com API (futuro com Flask ou FastAPI)

---

## 🎯 Objetivo

Construir base sólida em banco de dados com Python, entendendo como aplicações reais manipulam dados de forma estruturada.

---

## ⭐ Observação

Este projeto faz parte da minha jornada de aprendizado em desenvolvimento backend e será evoluído conforme avanço nos estudos.
