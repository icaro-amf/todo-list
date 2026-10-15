import os

from fastapi import FastAPI, HTTPException, Depends #importa lib para criar a API e tratar exceções, gerencia as rotas e tudo relativo a API
from pydantic import BaseModel, ConfigDict #lib responsável por fazer a validação de dados in/out da api.
from typing import List, Optional #fastapi exige a declaração de lista e optional para entender o formato do dado passado
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Boolean #importa lib para criar a conexão com o banco de dados e criar as tabelas do banco de dados
from sqlalchemy.orm import sessionmaker, Session, declarative_base #orquestração(orm). transformação de objetos para tabelas no bd e vice versa.

load_dotenv()

db_url = os.getenv("SQLALCHEMY_DATABASE_URL")
engine = create_engine(db_url) #inicia conexão com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #cria uma sessão para conversar com o bd
Base = declarative_base() #instancia a definição de uma classe base para criar as tabelas do banco de dados

class TodoDB(Base): #define os parametros da tabela do banco de dados
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine) #cria a tabela 'todos' com suas colunas no bd, caso nao exista.

class TodoBase(BaseModel): #base para os "todos" que serão manipulados na API
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase): #para criação de um "todo"
    pass

class TodoResponse(TodoBase): #para resposta de um "todo" existente
    id: int #novo
    model_config = ConfigDict(from_attributes=True) #reconstroi o objeto para um dict -> tarefa.titulo vira tarefa[titulo]
        
app = FastAPI(title="To-do List API", description="Primeira API Python, uma to-do list para organização pessoal.")
#app é a instancia do FastAPI criada no código.
def get_db():
    db = SessionLocal() #cria uma sessão para conversar com o bd
    try:
        yield db #entrega a sessão(db) para a função que chamou o get_db() e espera a função terminar para fechar a sessão.
    finally:
        db.close()#encerra conexao

@app.post("/todos/", response_model=TodoResponse, status_code=201) #rota post para criar novo "todo"
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = TodoDB(**todo.model_dump()) 
    db.add(db_todo)
    db.commit()     
    db.refresh(db_todo) 
    return db_todo