from pydantic import BaseModel, ConfigDict #lib responsável por fazer a validação de dados in/out da api.
from typing import Optional

class TodoBase(BaseModel): #base para os "todos" que serão manipulados na API
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase): #para criação de um "todo"
    pass

class TodoResponse(TodoBase): #para resposta de um "todo" existente
    id: int #novo
    model_config = ConfigDict(from_attributes=True) #reconstroi o objeto para um dict -> tarefa.titulo vira tarefa[titulo]