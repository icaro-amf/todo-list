import os
from dotenv import load_dotenv
from sqlalchemy import create_engine #lib para criar a conexão com o banco de dados e criar as tabelas do banco de dados
from sqlalchemy.orm import sessionmaker, declarative_base #orquestração(orm). transformação de objetos para tabelas no bd e vice versa.

load_dotenv()

db_url = os.getenv("SQLALCHEMY_DATABASE_URL")
engine = create_engine(db_url) #inicia conexão com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #cria uma sessão para conversar com o bd
Base = declarative_base() #instancia a definição de uma classe base para criar as tabelas do banco de dados

def get_db():
    db = SessionLocal() #cria uma sessão para conversar com o bd
    try:
        yield db #entrega a sessão(db) para a função que chamou o get_db() e espera a função terminar para fechar a sessão.
    finally:
        db.close() #encerra conexao