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

    def get_all(self):
        return self.db.query(TodoDB).all()

    def get_by_id(self, todo_id: int):
        return self.db.query(TodoDB).filter(TodoDB.id == todo_id).first()

    def update_by_id(self, todo_id: int, att_todo = TodoCreate):
        original = self.db.query(TodoDB).filter(TodoDB.id == todo_id).first()
        if not original:
            return None

        original.title = att_todo.title
        original.description = att_todo.description
        original.completed = att_todo.completed

        self.db.commit()
        self.db.refresh(original)
        return original
