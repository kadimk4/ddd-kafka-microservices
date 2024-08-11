
from dataclasses import dataclass
from app.domain.entities.base import BaseEntity
from app.domain.values.email import EmailStr

@dataclass
class User(BaseEntity):
    username: str
    email: EmailStr

print('aboba')