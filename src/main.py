from fastapi import FastAPI, HTTPException, Depends #importa lib para criar a API e tratar exceções, gerencia as rotas e tudo relativo a API
from typing import List #fastapi exige a declaração de lista e optional para entender o formato do dado passado
from sqlalchemy.orm import Session

from src.database import engine, get_db, Base
from src.schemas import TodoCreate, TodoResponse
from src.repository import TodoRepository

Base.metadata.create_all(bind=engine) #cria a tabela 'todos' com suas colunas no bd, caso nao exista.

app = FastAPI(title="To-do List API", description="Primeira API Python, uma to-do list para organização pessoal.")
#app é a instancia do FastAPI criada no código.

@app.post("/todos/", response_model=TodoResponse, status_code=201) #rota post para criar novo "todo"
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    repo = TodoRepository(db)
    return repo.create(todo)

@app.get("/todos/", response_model=List[TodoResponse]) #rota get para listar todos os "todos"
def get_all_todos(db: Session = Depends(get_db)):
    repo = TodoRepository(db)
    return repo.get_all()

@app.get("/todos/{todo_id}", response_model=TodoResponse) #rota get para listar um "todo" pelo id
def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    repo = TodoRepository(db)
    todo = repo.get_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}", response_model=TodoResponse) #rota put para atualizar um "todo" pelo id
def update_todo(todo_id: int, db: Session = Depends(get_db)):
    repo = TodoRepository(db)
    new_todo = repo.update_by_id(todo_id)
    if not new_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
 
    return new_todo