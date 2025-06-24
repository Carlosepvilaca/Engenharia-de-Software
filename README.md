# 📖 API de Livraria com Flask

Uma API RESTful para gerenciamento de uma livraria, permitindo operações de CRUD (Create, Read, Update, Delete) para **livros** e **autores**.  
O projeto é construído com **Flask** e **SQLAlchemy**, com documentação interativa gerada automaticamente via **Flasgger (Swagger UI)**.

---

## 📁 Estrutura do Projeto

A estrutura do projeto segue o padrão **MVC (Model-View-Controller)** para separação de responsabilidades.

```
APIBOOKS-FLASK/
├── app/
│   ├── __init__.py              # Inicialização da aplicação Flask (fábrica de apps)
│   ├── config.py                # Configurações (ex: URI do banco de dados)
│   ├── controllers/
│   │   ├── author_controller.py # Lógica de negócio para Autores
│   │   └── book_controller.py   # Lógica de negócio para Livros
│   ├── models/
│   │   ├── author_model.py      # Modelo de dados do Autor (SQLAlchemy)
│   │   └── book_model.py        # Modelo de dados do Livro (SQLAlchemy)
│   └── routes/
│       ├── author_routes.py     # Endpoints de Autores
│       └── book_routes.py       # Endpoints de Livros
├── tests/
│   ├── conftest.py              # Configurações e fixtures para testes
│   └── test_books.py            # Testes dos endpoints de Livros
├── venv/                        # Ambiente virtual Python
├── .gitignore                   # Arquivos ignorados pelo Git
├── requirements.txt             # Lista de dependências
├── run.py                       # Arquivo principal para execução da aplicação
```

---

## 🛠️ Tecnologias Utilizadas

- **Flask**: Micro-framework web.
- **SQLAlchemy**: ORM para comunicação com o banco de dados.
- **Flasgger**: Geração automática de documentação Swagger.
- **Pytest**: Execução de testes automatizados.
- **SQLite**: Banco de dados leve para desenvolvimento.

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/APIBOOKS-FLASK.git
   cd APIBOOKS-FLASK
   ```

2. **Crie e ative o ambiente virtual**:
   - **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Linux/macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**:
   ```bash
   python run.py
   ```

5. Acesse no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📘 Documentação Interativa

Explore e teste os endpoints através do Swagger UI:

🔗 [http://127.0.0.1:5000/apidocs/](http://127.0.0.1:5000/apidocs/)

---

## 📌 Endpoints da API

### 🔹 Autores `/authors`

| Método HTTP | Endpoint             | Descrição                                          |
|-------------|----------------------|----------------------------------------------------|
| POST        | `/authors`           | Adiciona um novo autor.                            |
| GET         | `/authors`           | Lista todos os autores com seus livros.            |
| GET         | `/authors/<id>`      | Retorna um autor específico por ID.                |
| PUT         | `/authors/<id>`      | Atualiza dados de um autor existente.              |
| DELETE      | `/authors/<id>`      | Remove um autor (caso não tenha livros associados).|

### 🔹 Livros `/books`

| Método HTTP | Endpoint             | Descrição                                  |
|-------------|----------------------|--------------------------------------------|
| POST        | `/books`             | Adiciona um novo livro a um autor.         |
| GET         | `/books`             | Lista todos os livros.                     |
| GET         | `/books/<id>`        | Retorna um livro específico por ID.        |
| PUT         | `/books/<id>`        | Atualiza os dados de um livro.             |
| DELETE      | `/books/<id>`        | Remove um livro do banco de dados.         |

---

## 🧪 Rodando os Testes

Execute os testes automatizados com **Pytest** para garantir a estabilidade da aplicação:

- Rodar todos os testes:
  ```bash
  pytest
  ```

- Rodar com cobertura de código:
  ```bash
  pytest --cov=app
  ```

---

## 📄 Licença

Este projeto é de código aberto e pode ser utilizado livremente para fins de estudo, aprendizado e desenvolvimento.

---