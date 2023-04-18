from database import engine, SessionLocal
from fastapi import APIRouter, Depends
from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .auth import current_user, token_exception
import models
import sys
sys.path.append("..")

router = APIRouter(
    prefix='/address',
    tags=['address'],
    responses={404: {"message": "Not Found"}}
)

#


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()  # type: ignore


class Address(BaseModel):
    address1: str
    address2: str
    city: str
    state: str
    country: str
    pincode: str


@router.post("/")
async def create_address(address: Address, user: dict = Depends(current_user), db: Session = Depends(get_db)):
    if user is None:
        raise token_exception("user not found")
    address_model = models.Address()
    address_model.address1 = address.address1  # type: ignore
    address_model.address2 = address.address2  # type: ignore
    address_model.city = address.city  # type: ignore
    address_model.state = address.state  # type: ignore
    address_model.country = address.country  # type: ignore
    address_model.pincode = address.pincode  # type: ignore

    db.add(address_model)
    db.flush()
    user_model = db.query(models.Users).filter(
        models.Users.id == user.get('id')).first()
    user_model.address_id = address_model.id  # type: ignore

    db.add(user_model)
    db.commit()
