from fastapi import FastAPI
import models
from routes import auth, todo, address, mail
from database import engine


app = FastAPI()

app.include_router(auth.router)
app.include_router(todo.router)
app.include_router(address.router)
app.include_router(mail.router)

models.Base.metadata.create_all(bind=engine)
