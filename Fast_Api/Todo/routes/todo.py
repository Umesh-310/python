from .auth import current_user, token_exception
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import Optional
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import sys
sys.path.append("..")

router = APIRouter(
    prefix='/todos',
    tags=['Todos'],
    responses={404: {"Message": "Not Found"}}
)

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="../api_test_F_END")


class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description="1 to 5")
    complete: bool


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()  # type: ignore


@router.get("/test")
async def test(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/")
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


@router.get("/{todo_id}")
async def read_todo(todo_id: int, user: dict = Depends(current_user), db: Session = Depends(get_db)):
    if user is None:
        raise token_exception("Could not validate credentials")

    todo_model = db.query(models.Todos)\
        .filter(models.Todos.id == todo_id)\
        .filter(models.Todos.owner_id == user.get("id"))\
        .first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Item Not Found")


@router.get("/user")
async def read_all_by_user(user: dict = Depends(current_user), db: Session = Depends(get_db)):
    if user is None:
        raise token_exception("Could not validate credentials")

    return db.query(models.Todos).filter(models.Todos.owner_id == user.get("id")).all()\
        # type: ignore


@router.post("/add-todo")
async def create_todo(todo: Todo, user: dict = Depends(current_user), db: Session = Depends(get_db)):
    if user is None:
        raise token_exception("Could not validate credentials")

    todo_model = models.Todos()
    todo_model.title = todo.title  # type: ignore
    todo_model.description = todo.description  # type: ignore
    todo_model.priority = todo.priority  # type: ignore
    todo_model.complete = todo.complete  # type: ignore
    todo_model.owner_id = user.get("id")  # type: ignore

    db.add(todo_model)
    db.commit()
    return {
        "status": 201,
        "message": "Done"
    }


@router.put('/{todo_id}')
async def update_todo(todo_id: int, todo: Todo, user: dict = Depends(get_db), db: Session = Depends(get_db)):
    if user is None:
        raise token_exception("Could not validate credentials")

    todo_model = db.query(models.Todos).filter(
        models.Todos.id == todo_id).filter(models.Todos.owner_id == user.get("id")).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="Item Not Found")

    todo_model.title = todo.title  # type: ignore
    todo_model.description = todo.description  # type: ignore
    todo_model.priority = todo.priority  # type: ignore
    todo_model.complete = todo.complete  # type: ignore
    todo_model.owner_id = user.get("id")  # type: ignore

    db.add(todo_model)
    db.commit()
    return {
        "status": 201,
        "message": "Done"
    }


@router.delete("/{todo_id}")
async def delete_todo(todo_id: int, user: dict = Depends(current_user), db: Session = Depends(get_db)):
    if user is None:
        raise token_exception("user not Login")

    todo_model = db.query(models.Todos).filter(
        models.Todos.id == todo_id).filter(models.Todos.owner_id == user.get("id")).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="Item Not Found")

    db.delete(todo_model)
    db.commit()
    return {
        "status": 203,
        "message": "Done"
    }
