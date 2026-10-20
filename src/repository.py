from sqlalchemy.orm import Session
from src.model import TodoDB
from src.schemas import TodoCreate

class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, todo: TodoCreate) -> TodoDB:
        db_todo = TodoDB(**todo.model_dump())
        self.db.add(db_todo)
        self.db.commit()
        self.db.refresh(db_todo)
        return db_todo

    def get_all(self):
        return self.db.query(TodoDB).all()

    def get_by_id(self, todo_id: int):
        return self.db.query(TodoDB).filter(TodoDB.id == todo_id).first()