# app/routes/todo_routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from app.api.todo import (
    get_all_todos,
    get_todo_by_id,
    create_new_todo,
    update_existing_todo,
    delete_todo_by_id
)
from app.schemas.todo import TodoCreate, TodoUpdate

router = APIRouter()

@router.get("/api/v1/todos")
def get_todos(db: Session = Depends(get_db)):
    return get_all_todos(db)

@router.get("/api/v1/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    return get_todo_by_id(todo_id, db)

@router.post("/api/v1/todos")
def create_todo(todo_request: TodoCreate, db: Session = Depends(get_db)):
    return create_new_todo(todo_request, db)

@router.put("/api/v1/todos/{todo_id}")
def update_todo(todo_id: int, todo_request: TodoUpdate, db: Session = Depends(get_db)):
    return update_existing_todo(todo_id, todo_request, db)

@router.delete("/api/v1/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return delete_todo_by_id(todo_id, db)
