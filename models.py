from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class TodoDB(Base): #define os parametros da tabela do banco de dados
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)