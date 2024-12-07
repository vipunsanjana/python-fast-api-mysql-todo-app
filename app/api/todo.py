# app/api/todo_api.py

from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

def get_all_todos(db: Session):
    return db.query(Todo).all()

def get_todo_by_id(todo_id: int, db: Session):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

def create_new_todo(todo_request: TodoCreate, db: Session):
    try:
        new_todo = Todo(content=todo_request.content)
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        return new_todo
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred")

def update_existing_todo(todo_id: int, todo_request: TodoUpdate, db: Session):
    try:
        todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        
        todo.content = todo_request.content

        if todo_request.status == "done":
            todo.status = "done"
        else:
            raise HTTPException(status_code=400, detail="Invalid status value")

        db.commit()
        db.refresh(todo)
        return todo
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred")

def delete_todo_by_id(todo_id: int, db: Session):
    try:
        todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")

        db.delete(todo)
        db.commit()
        return {"message": f"Todo deleted successfully. id: {todo_id}"}
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred")
