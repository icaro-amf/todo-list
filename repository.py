from sqlalchemy.orm import Session
from models import TodoDB
from schemas import TodoCreate

class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, todo: TodoCreate) -> TodoDB:
        db_todo = TodoDB(**todo.model_dump())
        self.db.add(db_todo)
        self.db.commit()
        self.db.refresh(db_todo)
        return db_todo