from fastapi import FastAPI
from app.domain.entities.user import User
from app.domain.values.email import EmailStr

app = FastAPI()


@app.get("/{username}/{email}")
def read_root(username: str, email: str):
    email = EmailStr(email)
    user = User(username=username, email=email)
    return user
