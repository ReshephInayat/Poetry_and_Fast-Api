from sqlmodel import SQLModel
from typing import Optional



class Todo(SQLModel):
    id: Optional[int] = None
    title: str
    description: str


data_todo: Todo = Todo(id="1", title="Todo 1", description="Todo 1 Description")

todo_db: list[Todo] = [data_todo]


def create_todo(todo: Todo):
    todo_db.append(todo)
    return todo


def get_all_todo():
    return todo_db


def delete_todo_by_id(todo_id: int):
    for todo in todo_db:
        if todo.id == todo_id:
            todo_db.remove(todo)
            return {"Todo Removed": "Status 200"}
    return {"Error": "404"}


def get_todo_by_id(todo_id: int):
    for todo in todo_db:
        if todo.id == todo_id:
            return todo
    return {"Error": "404"}
