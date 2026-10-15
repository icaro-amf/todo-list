from fastapi import FastAPI, HTTPException, Depends #importa lib para criar a API e tratar exceções, gerencia as rotas e tudo relativo a API
from typing import List #fastapi exige a declaração de lista e optional para entender o formato do dado passado
from sqlalchemy.orm import Session

from database import engine, get_db, Base
from schemas import TodoCreate, TodoResponse
from repository import TodoRepository

Base.metadata.create_all(bind=engine) #cria a tabela 'todos' com suas colunas no bd, caso nao exista.

app = FastAPI(title="To-do List API", description="Primeira API Python, uma to-do list para organização pessoal.")
#app é a instancia do FastAPI criada no código.

@app.post("/todos/", response_model=TodoResponse, status_code=201) #rota post para criar novo "todo"
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    repo = TodoRepository(db)
    return repo.create(todo)