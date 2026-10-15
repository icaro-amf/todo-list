# 📝 To-Do List API

Uma API RESTful simples e eficiente para gerenciamento de tarefas, construída com Python, FastAPI e PostgreSQL. Este projeto inclui operações completas de CRUD.

## 🚀 Tecnologias Utilizadas

* **[FastAPI](https://fastapi.tiangolo.com/):** Framework web rápido e moderno.
* **[SQLAlchemy](https://www.sqlalchemy.org/):** ORM para comunicação com o banco de dados.
* **[PostgreSQL](https://www.postgresql.org/):** Banco de dados relacional.
* **[Pydantic](https://docs.pydantic.dev/):** Validação e serialização de dados.
* **[Uvicorn](https://www.uvicorn.org/):** Servidor ASGI para rodar a aplicação.

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
python -m venv venv
.\venv\Scripts\activate

# No Linux/Mac:
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências:**
```bash
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

## 📖 Documentação da API

O FastAPI gera a documentação automaticamente. Com a API rodando, acesse no seu navegador:

* **Swagger UI (Interativa):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🔗 Endpoints Principais

* `POST /todos/` - Cria uma nova tarefa. ✅
* `GET /todos/` - Lista todas as tarefas. ❌
* `GET /todos/{id}` - Busca uma tarefa específica. ❌
* `PUT /todos/{id}` - Atualiza uma tarefa existente. ❌
* `DELETE /todos/{id}` - Deleta uma tarefa. ❌
