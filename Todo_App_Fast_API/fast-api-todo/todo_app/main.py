from fastapi import FastAPI

from todo_app.code import (
    create_todo,
    Todo,
    get_all_todo,
    get_todo_by_id,
    delete_todo_by_id,
)

app = FastAPI()


@app.get("/")
def root_read():
    return {"response": "Todo_AppFast_API"}


@app.post("/todo")
def create_todo_api(title: str, description: str, id: int):
    _todo = Todo(id=id, title=title, description=description)
    return create_todo(_todo)


@app.get("/todo")
def get_all_todo_api():
    return get_all_todo()


@app.get("/todo/{id}")
def get_todo_by_id_api(id: int):
    return get_todo_by_id(id)


@app.delete("/todo/{id}")
def delete_todo_by_id_api(id: int):
    return delete_todo_by_id(id)
