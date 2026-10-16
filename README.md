# 📝 To-Do List API

Uma API RESTful simples e eficiente para gerenciamento de tarefas, construída com Python, FastAPI e PostgreSQL.

## 🚀 Tecnologias Utilizadas

* **[FastAPI](https://fastapi.tiangolo.com/):** Framework web rápido e moderno.
* **[SQLAlchemy](https://www.sqlalchemy.org/):** ORM para comunicação com o banco de dados.
* **[PostgreSQL](https://www.postgresql.org/):** Banco de dados relacional.
* **[Pydantic](https://docs.pydantic.dev/):** Validação e serialização de dados.
* **[Uvicorn](https://www.uvicorn.org/):** Servidor ASGI para rodar a aplicação.
* **[python-dotenv](https://pypi.org/project/python-dotenv/):** Gerenciamento de variáveis de ambiente.

## ⚙️ Pré-requisitos

* Python 3.8+ instalado.
* PostgreSQL instalado e rodando na sua máquina.

## 🛠️ Como rodar o projeto

**1. Clone o repositório ou acesse a pasta do projeto:**
```bash
cd todo-list
```

**2. Crie e ative um ambiente virtual:**
```bash
# No Windows:
python -m venv .venv
.\.venv\Scripts\activate

# No Linux/Mac/WSL:
python3 -m venv .venv
source .venv/bin/activate
```

**3. Instale as dependências:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**4. Configure o Banco de Dados:**
* Crie um banco de dados no PostgreSQL chamado `todo_list`.
* Crie um arquivo `.env` na raiz do projeto e adicione a sua URL de conexão:
```env
SQLALCHEMY_DATABASE_URL=postgresql://seu_usuario:sua_senha@localhost:5432/todo_list
```

**5. Execute a aplicação:**
```bash
python -m uvicorn main:app --reload
```

A API estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📖 Documentação da API

O FastAPI gera a documentação automaticamente. Com a API rodando, acesse no seu navegador:

* **Swagger UI (Interativa):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🔗 Endpoints Implementados

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/todos/` | Cria uma nova tarefa |
| `GET` | `/todos/` | Lista todas as tarefas |
| `GET` | `/todos/{id}` | Busca uma tarefa específica |

> **Nota:** Endpoints de atualização (`PUT`) e exclusão (`DELETE`) ainda não foram implementados.

## 📁 Estrutura do Projeto

```
todo-list/
├── main.py              # Ponto de entrada da aplicação
├── database.py          # Configuração do banco de dados
├── models.py            # Modelos SQLAlchemy
├── schemas.py           # Schemas Pydantic (validação)
├── repository.py        # Camada de acesso a dados
├── requirements.txt     # Dependências do projeto
├── .env                 # Variáveis de ambiente (não versionado)
├── .env.example         # Exemplo de variáveis de ambiente
└── .venv/               # Ambiente virtual (não versionado)
```

## 📝 Variáveis de Ambiente

O arquivo `.env` deve conter:

```env
SQLALCHEMY_DATABASE_URL=postgresql://usuario:senha@host:porta/banco
```

Copie `.env.example` para `.env` e ajuste os valores.