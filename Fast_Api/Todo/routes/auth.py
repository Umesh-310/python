from fastapi import Depends, status, HTTPException, APIRouter
from pydantic import BaseModel
from typing import Optional
import models
from passlib.context import CryptContext
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError
from starlette.responses import HTMLResponse


SECRET_KEY = "UmA0310esK1211hU3"
ALGORITHM = "HS256"


class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

models.Base.metadata.create_all(bind=engine)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")  # type: ignore

# app = FastAPI()
router = APIRouter(
    prefix='/auth',
    tags=['auth'],
    responses={401: {"user": "Not authorized"}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()  # type: ignore


def get_password_hash(password):
    return bcrypt_context.hash(password)


def verify_password(plain_pass, hashed_pass):
    return bcrypt_context.verify(plain_pass, hashed_pass)


def authenticate_user(username: str, password: str, db):
    user = db.query(models.Users).filter(
        models.Users.username == username).first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False

    return user


def create_access_token(username: str, user_id: int, expires_delta: Optional[timedelta] = None):
    encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)  # type: ignore


def current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")  # type: ignore
        user_id: int = payload.get("id")  # type: ignore
        if username is None or user_id is None:
            raise token_exception("Could not validate credentials")
        return {"username": username, "id": user_id}
    except JWTError:
        raise token_exception("Could not validate credentials")


@router.post("/create/user" , response_class=HTMLResponse)
async def create_new_user(create_user: CreateUser, db: Session = Depends(get_db)):
    create_user_model = models.Users()

    create_user_model.email = create_user.email  # type: ignore
    create_user_model.username = create_user.username  # type: ignore
    create_user_model.first_name = create_user.first_name  # type: ignore
    create_user_model.last_name = create_user.last_name  # type: ignore
    create_user_model.hashed_password = get_password_hash(   # type: ignore
        create_user.password)  # type: ignore
    create_user_model.is_active = True  # type: ignore

    db.add(create_user_model)
    db.commit()
    return {"status": 201, "message": "User create successfully"}


@router.get("/users")
async def get_users(db: Session = Depends(get_db)):
    return db.query(models.Users).all()


@router.post('/login')
async def Login_token(from_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(from_data.username, from_data.password, db)

    if not user:
        raise token_exception("Incorrect username or password")

    token_expires = timedelta(minutes=20)
    token = create_access_token(
        user.username, user.id, expires_delta=token_expires)  # type: ignore
    return {"token": token}

# Exceptions


def token_exception(message: str):
    token_exception_response = HTTPException(
        status_code=status. HTTP_401_UNAUTHORIZED,
        detail=message,
        headers={"WWW-Authenticate": "Bearer"},
    )

    return token_exception_response
