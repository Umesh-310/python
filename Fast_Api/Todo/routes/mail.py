from typing import List
import smtplib

from fastapi import BackgroundTasks, APIRouter
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
# from dot env
from dotenv import dotenv_values

creddentials = dotenv_values(".env")


class EmailSchema(BaseModel):
    email: List[EmailStr]


class EmailContent(BaseModel):
    email: List[EmailStr]
    massage: str
    subject: str


conf = ConnectionConfig(
    MAIL_USERNAME=creddentials['EMAIL'],  # type: ignore
    MAIL_PASSWORD=creddentials['PASSWORD'],  # type: ignore
    MAIL_FROM="artemis.aku@gmail.com",  # type: ignore
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

router = APIRouter()


@router.post('/email')
async def send_email(content: EmailSchema):

    html = f"""
    <h2>Hello </h2>
    <h3>Umesh Saini</h3> 
    
    <h5>Thank you </h6>
    <h6>@umesh_saini</h6>
    """

    message = MessageSchema(
        subject="hello this is message",
        recipients=content.dict().get("email"),  # type: ignore
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    await fm.send_message(message)

    return JSONResponse(status_code=200, content={"message": "email has been sent"})
