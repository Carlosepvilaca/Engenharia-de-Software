📖 API de Livraria com Flask
Uma API RESTful para gerenciamento de uma livraria, permitindo operações de CRUD (Create, Read, Update, Delete) para livros e autores. O projeto é construído com Flask e SQLAlchemy, com documentação interativa gerada automaticamente via Flasgger (Swagger UI).

📁 Estrutura do Projeto
O projeto segue uma organização baseada no padrão Model-View-Controller (MVC) para separação de responsabilidades.

APIBOOKS-FLASK/
├── app/
│   ├── __init__.py           # Inicialização da aplicação Flask (fábrica de apps)
│   ├── config.py             # Configurações (ex: URI do banco de dados)
│   ├── controllers/
│   │   ├── author_controller.py  # Lógica de negócio para Autores
│   │   └── book_controller.py    # Lógica de negócio para Livros
│   ├── models/
│   │   ├── author_model.py     # Modelo de dados do Autor (SQLAlchemy)
│   │   └── book_model.py       # Modelo de dados do Livro (SQLAlchemy)
│   └── routes/
│       ├── author_routes.py    # Definição das rotas (endpoints) para Autores
│       └── book_routes.py      # Definição das rotas (endpoints) para Livros
├── tests/
│   ├── conftest.py           # Configurações e fixtures para testes
│   └── test_books.py         # Testes para os endpoints de Livros
├── venv/                     # Pasta do ambiente virtual Python
├── .gitignore                # Arquivos e pastas a serem ignorados pelo Git
├── requirements.txt          # Lista de dependências do projeto
└── run.py                    # Ponto de entrada para executar a aplicação


🛠️ Tecnologias Utilizadas
Flask: Micro-framework web para a construção da API.

SQLAlchemy: ORM (Object-Relational Mapper) para interagir com o banco de dados.

Flasgger: Biblioteca para gerar documentação Swagger UI de forma automática.

Pytest: Framework para a escrita e execução de testes automatizados.

SQLite: Banco de dados relacional leve utilizado para desenvolvimento.

🚀 Como Executar o Projeto
1. Clone o repositório (se necessário):

git clone <url-do-seu-repositorio>
cd <nome-da-pasta-do-projeto>


2. Crie e ative um ambiente virtual:

# Criar o ambiente
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no Linux/macOS
source venv/bin/activate


3. Instale as dependências:

pip install -r requirements.txt


4. Execute a aplicação:

python run.py


A aplicação estará rodando em http://127.0.0.1:5000.

📘 Endpoints da API
A melhor forma de explorar e testar a API é através da documentação interativa do Swagger.

Acesse em: http://127.0.0.1:5000/apidocs/

Abaixo está um resumo de todos os endpoints disponíveis.

Recursos de Autores (/authors)
|

| Método HTTP | Endpoint | Descrição |
| POST | /authors | Adiciona um novo autor. |
| GET | /authors | Lista todos os autores e seus livros. |
| GET | /authors/<author_id> | Retorna um autor específico pelo seu ID. |
| PUT | /authors/<author_id> | Atualiza os dados de um autor existente. |
| DELETE | /authors/<author_id> | Remove um autor (se não tiver livros associados). |

Recursos de Livros (/books)
| Método HTTP | Endpoint | Descrição |
| POST | /books | Adiciona um novo livro a um autor. |
| GET | /books | Lista todos os livros. |
| GET | /books/<book_id> | Retorna um livro específico pelo seu ID. |
| PUT | /books/<book_id> | Atualiza os dados de um livro. |
| DELETE | /books/<book_id> | Remove um livro do banco de dados. |

🧪 Rodando os Testes
Para garantir a qualidade e o funcionamento correto da API, execute os testes automatizados.

# Rodar todos os testes
pytest

# Rodar os testes com relatório de cobertura de código
pytest --cov=app


📄 Licença
Este projeto é de código aberto e pode ser utilizado livremente para fins de estudo e desenvolvimento.
